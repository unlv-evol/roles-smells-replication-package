'''
Configuration file for the performance evaluation of the machinelearning algorithms
'''

from sklearn import svm, naive_bayes
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE, ADASYN
import os
# the base path of the experiment
base_path = os.path.dirname(os.path.abspath(__file__))
# labeled_data = "01-new_version_features_label-20180814.csv" # K-9 Mail
labeled_data = "data/train/three-cases-20190301.csv"  # Three cases

resample = 'none'
classifier = 'random-forest'
single_role = 'ST'  # {CO, CT, SP, ST, IH, IT}


def get_data_exp():
    return r"{}\{}".format(base_path, labeled_data)


'''
Get the sampling technique
'''


def get_resample_config(features, labels):
    if resample == 'SMOTE':
        # print("Resampling using SMOTE")
        return SMOTE().fit_sample(features, labels)
    elif resample == 'ADASYN':
        # print("Resampling using ADASYN")
        return ADASYN().fit_sample(features, labels)
    elif resample == 'none':
        # print("Not using Resampling")
        return features, labels
    else:
        print('ERR: config not found')
        return None


'''
get the classifier algorithm and also its parameters
'''


def get_classifier():
    if classifier == 'random-forest':
        print('USING: RANDOM FOREST CLASSIFIER=======================')
        return RandomForestClassifier(n_jobs=2, n_estimators=1000)
    elif classifier == 'svm-linear':
        print('USING: SVM LINEAR CLASSIFIER=======================')
        return svm.SVC(kernel='linear', C=1)
    elif classifier == 'multinomial-nb':
        print('USING: MULTINOMIAL NAIVE BAYES CLASSIFIER=======================')
        return naive_bayes.MultinomialNB()
    else:
        print('ERR: not supported yet')
        return None


'''
'''


def get_binary_data():
    filenames = labeled_data.split(".")
    filename = "{}\{}-{}.{}".format(base_path,
                                    filenames[0], single_role, filenames[1])
    return filename


def get_importance_feature_path():
    filenames = labeled_data.split(".")
    filename = "{}\{}-{}-feature-{}.{}".format(
        base_path, filenames[0], single_role, resample, filenames[1])
    return filename


def get_label():
    if single_role == 'IH':
        return ['Information Holder']
    elif single_role == 'ST':
        return ['Structurer']
    elif single_role == 'SP':
        return ['Service Provider']
    elif single_role == 'CT':
        return ['Controller']
    elif single_role == 'CO':
        return ['Coordinator']
    elif single_role == 'IT':
        return ['Interfacer']
    else:
        print("not Found")
        return None
