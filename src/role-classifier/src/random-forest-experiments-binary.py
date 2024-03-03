from pprint import pprint

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef, make_scorer, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import cross_validate, StratifiedKFold, LeaveOneOut
import numpy as np
# import plotly.graph_objs as go
# import plotly

import categorical_util as cu
import config_metrics as cfg

df = pd.read_csv(cfg.get_binary_data(), converters={'isStaticClass' : bool})

# get features and labels
features = df.drop(columns=['index', 'fullpathname', 'classname', 'label'])
# print(features)
# print(features.dtypes)

labels = df.loc[:, 'label']
# print(labels)

# features_replace = cu.get_replace_map(features)
features_replace = cu.get_one_hot_encoding(features)
# print(features_replace.dtypes)
# print(features_replace.columns)

# takes the features and labels based on config
features, labels = cfg.get_resample_config(features_replace, labels)

# classifier
clf = cfg.get_classifier()

# calculate the score
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=50)

print("Precision\tRecall\tF1-score\tMCC")
importance_list = list()
count = 0
for train_index, test_index in skf.split(features, labels):
# for train_index, test_index in skf.split(features_replace, labels):
    # get training data
    # features_train, features_test = features[train_index], features[test_index]
    # labels_train, labels_test = labels[train_index], labels[test_index]
    features_train = features.iloc[train_index]
    features_test = features.iloc[test_index]
    labels_train = labels.iloc[train_index]
    labels_test = labels.iloc[test_index]
    clf.fit(features_train, labels_train)
    labels_predicted = clf.predict(features_test)

    # pprint(labels_test.tolist())
    # pprint(labels_predicted.tolist())

    # create the confusion matrix
    # conf_matrix = confusion_matrix(labels_test, labels_predicted, labels=[cfg.single_role, 'Other'])
    # print(conf_matrix)

    # calculates the score
    p_score = precision_score(labels_test, labels_predicted, average='weighted', labels=cfg.get_label())
    r_score = recall_score(labels_test, labels_predicted, average='weighted', labels=cfg.get_label())
    f_score = f1_score(labels_test, labels_predicted, average='weighted', labels=cfg.get_label())
    mcc_score = matthews_corrcoef(labels_test, labels_predicted)
    # print the scores
    print("%0.2f\t%0.2f\t%0.2f\t%0.2f"% (p_score, r_score, f_score, mcc_score))
    # get the feature importance
    add_row = zip(clf.feature_importances_)
    importance_list.append(add_row)
    # if count == 0:
    #     break

ildf = pd.DataFrame(importance_list, columns=features_replace.columns)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(ildf)

ildf.to_csv(cfg.get_importance_feature_path(), sep=',')