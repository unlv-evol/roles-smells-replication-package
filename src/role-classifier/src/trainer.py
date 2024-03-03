'''
Provide training and create a model file using Random Forest + SMOTE
'''

import pickle

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import categorical_util as cu
import config_metrics as cfg
import os


base_path = os.path.dirname(os.path.abspath(__file__))

features_file = os.path.join(base_path, 'data/train/three-cases-20190301.csv')

model_file = os.path.join(base_path, 'model/model.sav')

df = pd.read_csv(features_file, converters={'isStaticClass': bool})
features = df.drop(columns=['index', 'fullpathname', 'classname', 'label'])
labels = df.loc[:, 'label']

# one hot encoding
features_replace = cu.get_one_hot_encoding(features)
# print(features_replace.dtypes)

# SMOTE resampling
features, labels = cfg.get_resample_config(features_replace, labels)

# model initiation
model = RandomForestClassifier(n_jobs=2, n_estimators=1000)
# training
model.fit(features, labels)

# save model into file
pickle.dump(model, open(model_file, 'wb'))
