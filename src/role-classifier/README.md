## Role-Stereotypes Feature Extraction

This directory provides the step by step guide of setting up and classifying role-stereotypes to one of the six categories i.e. `Service Provider`, `Information Holder`, `Interfacer`, `Controller`, `Coordinator` and `Structurer`.

### Installation  Setups
- Clone this repository locally using `git clone` command. Afterwards, `cd` to `Classification Package`.
- Create a python virtual environment. On `macOS` or `Linux` you can use the following commands: `python3 -m venv env`, aftewards, activate the newly created virtual environment using `source env/bin/activate`.
- Now you can install the required packages using `pip install -r requirements.txt`
- That's it, now we can move on to train and classify our dataset.

### Classification 
To classify your feature dataset, you should first train the model. You can do this by running the `train.py` file. 
- The ground-truth dataset for training the model (default classifier: `Random Forest`) is available in `data/train` directory.
- Run: `python src/train.py`
- The output of the trained model will be stored in `model` directory.
- The next step is to classify our dataset.
    -   First, place the dataset to be classified in `data/test/` directory. Also, edit the `features_test` name in `src/main_classifier.py` to match the file name of the dataset to be classified.
    - Now, run `python src/main_classifier`. The output of the classified dataset will be stored in `data/result`