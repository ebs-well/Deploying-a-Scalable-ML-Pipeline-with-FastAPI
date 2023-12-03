import pytest
# TODO: add necessary import
import os
import pandas as pd
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_data_has_correct_columns():
    """
    Load in the original dataset and ensure it has all the expected features.
    """
    # Your code here
    project_path = "/home/indigon/projects/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)

    expected_cols = {
        'age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    }

    assert set(data.columns) == expected_cols


# TODO: implement the second test. Change the function name and input as needed
def test_slice_output_length():
    """
    Load in the slice_output text file and ensure it has a reasonable minimum length.
    This makes sure that the test data isn't grouped into too few slices.
    """
    # Your code here
    with open('slice_output.txt', 'r') as file:
        lines = sum(1 for line in file)

    minimum = 1300
    assert lines >= minimum


# TODO: implement the third test. Change the function name and input as needed
def test_model_type_is_forest_classifier():
    """
    Makes sure that the type of model being used in the train_model function
    is a random forest classifier, as updates to the code might accidnetally
    make it a regressor instead.
    """
    # Your code here
    sample_x = [[1, 2, 3], [4, 5, 6]]
    sample_y = ['low', 'high']

    model = train_model(sample_x, sample_y)

    assert type(model) == type(RandomForestClassifier())
