'''
Performance measure using Random Forest algorithm, SMOTE resampling, score for each role stereotype
'''
from pprint import pprint
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import matthews_corrcoef, make_scorer, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_validate, StratifiedKFold, LeaveOneOut
import numpy as np
import categorical_util as cu
import config_metrics as cfg
import metrics_util as mu


'''
The main function
'''
df = pd.read_csv(cfg.get_data_exp(), converters={'isStaticClass' : bool})

# get features and labels
features = df.drop(columns=['index', 'fullpathname', 'classname', 'library', 'label'])
# print(features)
# print(features.dtypes)

labels = df.loc[:, 'label']
# print(labels)

# features_replace = cu.get_replace_map(features)
features = cu.get_one_hot_encoding(features)
# print(features_replace.dtypes)
# print(features_replace.columns)

# classifier
clf = cfg.get_classifier()
print("Resampling method: {}".format(cfg.resample))

# calculate the score
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=50)

# print("Precision\tRecall\tF1-score\tMCC")
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
    
    # takes the features and labels based on config
    features_train, labels_train = cfg.get_resample_config(features_train, labels_train)

    clf.fit(features_train, labels_train)
    labels_predicted = clf.predict(features_test)

    # pprint(labels_test.tolist())
    # pprint(labels_predicted.tolist())

    # create the confusion matrix
    # conf_matrix = confusion_matrix(labels_test, labels_predicted, labels=['Coordinator', 'Controller', 'Information Holder', 'Interfacer', 'Service Provider', 'Structurer'])
    # print(conf_matrix)
    # mu.calculate_mcc(conf_matrix)

    # classification report
    # report = classification_report(labels_test, labels_predicted)
    # print(report)

    # calculates the score
    p_score = precision_score(labels_test, labels_predicted, average='weighted')
    r_score = recall_score(labels_test, labels_predicted, average='weighted')
    f_score = f1_score(labels_test, labels_predicted, average='weighted')
    mcc_score = matthews_corrcoef(labels_test, labels_predicted)
    # print the scores
    print("%0.2f\t%0.2f\t%0.2f\t%0.2f"% (p_score, r_score, f_score, mcc_score))
    