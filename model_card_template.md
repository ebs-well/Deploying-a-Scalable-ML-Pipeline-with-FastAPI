# Model Card  
  
## Model Details  
Jordan Hicks created this model. It is a Random forest Classifier.  
This model is using all the default hyperparameters of scikit-learn 1.0.2  
  
## Intended Use  
This model should be used to predict a person's salary range  
(above or below $50K / year) based off basic census data.  
The inteded users are the general public, who may want to get a feel for  
how how increasing their education level could impact their potential earnings.  

## Training Data  
This dataset was obtained from the Udacity  
"Deploying-a-Scalable-ML-Pipeline-with-FastAPI" github reposiory.  
(https://github.com/udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI)  
This is basic census bureau data containing information about people such as  
their education level, race, gender, and wether they current make above or  
below $50,000 / year.  
The target was not altered from how it appeared in the "salary" column.  
  
The original dataset contains 32,562 rows. Eighty percent of the data was used for  
the training set. During training, a One Hot Encoder and label binarizer were  
used on the categorical features and labels respectively.

## Evaluation Data  
The evaluation data was simply split off from the training data, with  
twenty percent of the total data being sued for the test set. No stratiication  
was used.  
  
## Metrics  
This model was evaluated with the precision, recall, and F1 scores.  
The precision score is 0.7351.  
The recall score is 0.6399.  
The F1 score is 0.6808.  
  
While there are too many unique slices of data to go over here, the accompanying file  
"slice_output.txt" contains the scores for every individual slice.  

## Ethical Considerations  
This model makes salary predictions based partially on a person's  
immutable characteristics, such as race and gender. As such, this model should  
only be used descriptively, and never used prescriptively.  
  
## Caveats and Recommendations  
This model could be used for less casual reasons in the future, but several  
things would need to be changed. The original data would need to have many references  
to a person's race, national origin, gender, etc, compeltely removed from the dataset.  
In addition, he model would need to have some sort of hyperparameter optimization applied.  
While additional improvements could be made, that sould be the minimum for using this model  
for a more rigorous analysis rather than proof of concept.
