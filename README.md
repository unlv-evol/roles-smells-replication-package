## Empirical Investigation of the Relationship Between Design Smells and Role Stereotypes

The repository contains data, code and tools used to generate graph, charts and statistical for our study on the relationship between design smells and role stereotypes.
### Abstract (Short)
During the development of software systems, poor design and implementation choices can have a detrimental impact on the maintainability of the software. Design smells, recurring patterns of poorly designed fragments in software, are indicative of these issues.This paper employs an exploratory approach, combining statistical analysis and unsupervised learning methods, to comprehend the relationship between design smells and role-stereotypes and how this connection varies across different desktop and mobile applications. The study utilizes a dataset comprising 11,350 classes across 30 Java projects mined from GitHub. Overall, the findings reveal several design smells that co-occur more frequently across the entire role-stereotype categories. Specifically, three (3) out of six (6) role-stereotypes considered in this study are more susceptible to design smells. Through unsupervised learning methods, it is observed that certain pairs or groups of role-stereotypes are prone to similar types of design smells compared to others. The results of this paper can guide software teams in implementing various design smell prevention and correction mechanisms, as well as ensuring the conceptual integrity of classes during their design and maintenance.


### Directory Structure
The directory structure is illustrated below:
```
.
├── LICENSE
├── README.md
├── .gitignore
├── data
├── results
├── requirements.txt
├── PaReco.py
├── src
│   ├── bin
│   ├── helpers
│   ├── popc
│   ├── role-classifier
│   ├── role-feature-extractor
│   ├── notebooks
│   ├── extract_ds_metrics.py
│   └── extract_ds2csv.py
└── 
```
- ``data``: Input data for analysis
- ``results``: Output of the analysis. It is also used for ploting graphs and performing statistical tests
- ``requirements.txt``: Contain essential dependencies. Note: additional dependencies are located in the sub ``src`` directories. Those are specific to a given module
- ``src``: Source code
    - ``bin``: Useful bash/shell scripts
    - ``helper``: Helper functions
    - ``notebooks``: All the notebooks used to perform different analysis
    - ``popc``: POPC clustering source code
    - ``role-feature-extractor``: This is a parse tool written in Java. It process **srcML** files and returns a **csv** with 21 role stereotype features.
    - ``role-classifier``: Role stereotype classification code. It also contain sample data for *test*, *train* and *validate*
    - ``extract_ds_metrics.py``: Useful script to extract design smell metrics
    - ``extract_ds2csv.py``: Useful script to convert design smell *.ini* files to *csv*, ready for further analysis.

As you might have already noticed, this replication package a number of useful tools. Let take an example of the ``role-classifier`` module. To use this module, let us demonstrate how to up and classify role-stereotypes to one of the six categories i.e. `Service Provider`, `Information Holder`, `Interfacer`, `Controller`, `Coordinator` and `Structurer`.

### Installation  Setups
- Clone this repository locally using `git clone` command. Afterwards, `cd` to `src/role-classifier`.
- Create a python virtual environment. On `macOS` or `Linux` you can use the following commands: `python3 -m venv env`, aftewards, activate the newly created virtual environment using `source env/bin/activate`. Now you can install the required packages using `pip install -r requirements.txt`
- That's it, now we can move on to train and classify our dataset.

### Classification 
To classify your feature dataset, you should first train the model. You can do this by running the `train.py` file. 
- The ground-truth dataset for training the model (default classifier: `Random Forest`) is available in `data/train` directory.
- Run: `python src/train.py`
- The output of the trained model will be stored in `model` directory.
- The next step is to classify our dataset.
    -   First, place the dataset to be classified in `data/test/` directory. Also, edit the `features_test` name in `src/main_classifier.py` to match the file name of the dataset to be classified.
    - Now, run `python src/main_classifier`. The output of the classified dataset will be stored in `data/result`

### Reproducing Graphs Illustrated in The Paper
To reproduce the graphs in the paper, use the `5.0-analysis-all.ipynd` notebook located in the `notebook` directory.

## Issues 
If you are interested in utilizing this replication package and encounter any issues, please don't hesitate to report them to the corresponding author of this study