import pytest
import os
import pandas as pd
from ml.data import process_data
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def data_file_path():
    return './data/census.csv'

def test_data_has_correct_columns(data_file_path):
    """
    Load in the original dataset and ensure it has all the expected features.
    """
    data = pd.read_csv(data_file_path)
    expected_cols = {
        'age', 'workclass', 'fnlgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    }

    assert set(data.columns) == expected_cols
    

@pytest.fixture
def test_data():
    return pd.DataFrame({
        'column_1': [5, 4, 3, 2, 1],
        'column_2': [0, 1, 0, 1, 0],
        'label': [0, 1, 0, 1, 0]
    })

def test_two(test_data):
    """
    test_two checks if the function train_model returns a random forest classifier model.
    """
    X_train, y_train, _, _ = process_data(
        test_data,
        categorical_features=['column_2'],
        label='label',
        training=True
    )

    random_forest = train_model(X_train, y_train)

    assert isinstance(random_forest, RandomForestClassifier)

def test_three():
    """
    Test inference of model
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "slice_output.txt")
    with open(data_path, "r") as file:
        file_content = file.read()

    assert len(file_content) > 0, "Output file is empty"