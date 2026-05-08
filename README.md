# End-to-end-Machine-Learning-Project-with-MLflow

## Workflows

1. Update config.yaml
2. Upadate schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py


# How to run?

### STEPS:

Clone the repository

'''bash
https://github.com/Kashika3006/End-to-end-Machine-Learning-Project-with-MLflow
'''

### STEP 01- Create a conda environment after opening the repository

'''bash
conda create -m mlproj python=3.8 -y
'''
'''bash
conda activate mlproj
'''

### STEP 02- Install the requirements
'''bash
pip install -r requirements.txt
'''

'''bash
# Finally run the following command
python app.py
'''

Now,
'''bash
open up ypur local host and port
'''

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlfow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Kashika3006/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=Kashika3006 \
MLFLOW_TRACKING_PASSWORD=90f0b537d19fa66b88a76f733599d7dcee7080e9 \

Run this to export as env variables:

'''bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Kashika3006/End-to-end-Machine-Learning-Project-with-MLflow.mlflow 

export MLFLOW_TRACKING_USERNAME=Kashika3006

export 
MLFLOW_TRACKING_PASSWORD=90f0b537d19fa66b88a76f733599d7dcee7080e9

'''


