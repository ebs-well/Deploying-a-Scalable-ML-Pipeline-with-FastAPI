# Model Card

## Model Details

This model is a Random Forest Classifier using all the default hyperparameters of scikit-learn. The random forest classifier is a meta-estimator that fits several decision tree classifiers on various sub-samples of the dataset and uses averaging to improve predictive accuracy and control overfitting.

## Intended Use

The intended use of this model is to predict a person's salary range (above or below $50K per year) based on basic census data. It is suitable for general public use, providing insight into how increasing education level could impact potential earnings.

## Training Data

The training dataset, obtained from the Udacity "Deploying-a-Scalable-ML-Pipeline-with-FastAPI" GitHub repository, contains basic census bureau data about individuals' education level, race, gender, and salary status. The original dataset contained 32,562 rows, and 80% of the data was used for training. During training, a One Hot Encoder and label binarizer were applied to categorical features and labels, respectively.

## Evaluation Data

The evaluation data was split off from the training data, with 20% of the total data used for the test set. No stratification was applied.

## Metrics

The model was evaluated using precision, recall, and F1 scores. The precision score is 0.7470, the recall score is 0.6246, and the F1 score is 0.6803. Detailed evaluation results for individual slices can be found in the accompanying file "slice_output.txt."

## Ethical Considerations

This model predicts salary based on immutable characteristics such as race and gender. Therefore, it should only be used descriptively and not prescriptively. Careful consideration should be given to potential biases in the dataset, and the model's use should be monitored to ensure fairness and ethical use.

## Caveats and Recommendations

For more rigorous analysis, certain changes would be necessary, such as removing references to race, national origin, and gender from the dataset and applying hyperparameter optimization to the model. While additional improvements are possible, these changes would constitute a minimum requirement for using the model beyond proof of concept.