# TestScorePredictionLinearRegression
This program is designed to predict the outcome of Test 3 based on the scores of Test 1 and Test 2.
It utilizes various regression models to achieve accurate predictions. 
The available regression models used in this program are:

    Linear Regression
    Support Vector Regression (SVR)
    Random Forest Regression
    Gradient Boosting Regression
    Voting Regressor

The voting regressor combines the predictions from multiple models to generate the final prediction. 
The models are trained using the existing data in the 'data.csv' file.     
    data_orig.csv: This dataset contains actual real-world data for Test 1, Test 2, and Test 3. It serves as the original dataset.
    data.csv: This dataset is a combination of 30% artificially generated data and 70% of the original data. It is used to augment the training data for improved model performance.
NOTE: This is a simple demo of regression models, it does not consider factors such as the hours of study per day, etc. hence , it should not be treated  anything other than a regression program.
