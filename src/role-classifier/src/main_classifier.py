import pickle
from pprint import pprint

import pandas as pd
import categorical_util as cu
import numpy as np
import os

base_path = os.path.dirname(os.path.abspath(__file__))
# model_file = 'MODEL_PATH/MODEL_FILE_NAME.sav'
model_file = os.path.join(base_path, 'model/model.sav')

# features_test = 'FEATURES_FILE_PATH/FEATURES_FILE_NAME.csv'
features_test = os.path.join(base_path, 'data/test/features_test.csv')

# df = pd.read_csv(features_test, converters={'isStaticClass': bool}, index_col='index')
df = pd.read_csv(features_test, converters={'isStaticClass': bool})
# pprint(df)
# print(df.dtypes)

features = df.drop(columns=['Fullpathname', 'Classname', 'numInnerClasses'])
# print(features.dtypes)

# one hot encoding
features_replace = cu.get_one_hot_encoding(features)
# pprint(len(features_replace))
# pprint(features_replace.dtypes)

# check if one hot encoding for class publicity all exists
if 'classPublicity_public' not in features_replace.columns:
    add_features = pd.DataFrame(0, index=np.arange(len(features_replace)), columns=['classPublicity_public']).astype(
        'category')
    features_replace = features_replace.join(add_features)

if 'classPublicity_private' not in features_replace.columns:
    add_features = pd.DataFrame(0, index=np.arange(len(features_replace)), columns=['classPublicity_private']).astype(
        'category')
    features_replace = features_replace.join(add_features)

if 'classPublicity_protected' not in features_replace.columns:
    add_features = pd.DataFrame(0, index=np.arange(len(features_replace)), columns=['classPublicity_protected']).astype(
        'category')
    features_replace = features_replace.join(add_features)

if 'classPublicity_default' not in features_replace.columns:
    add_features = pd.DataFrame(0, index=np.arange(len(features_replace)), columns=['classPublicity_default']).astype(
        'category')
    features_replace = features_replace.join(add_features)

# replace any NAN with 0
# features_replace.fillna(0, inplace=True)
#features_replace.to_csv("features_replace.csv", sep=',', index=True)
# pprint(features_replace.columns[features_replace.isnull().any()])

# drop 'Unnamed: 27' column
# features_replace = features_replace.drop(['Unnamed: 27'], axis=1)

model = pickle.load(open(model_file, 'rb'))
labels_predicted = model.predict(features_replace)

df.loc[:, 'pred_label'] = pd.Series(
    labels_predicted, index=features_replace.index)

# pprint(df)

# result_path = "RESULT_PATH/RESULT_FILE_NAME.csv"
result_path = os.path.join(base_path, "data/result/test_data_classified.csv")

df.to_csv(result_path, sep=',', index=True)
