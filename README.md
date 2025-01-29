# FitCal-Predict
Project Overview

This project aims to predict the number of calories burnt based on various physical activities and individual characteristics. The model is trained using machine learning techniques, specifically an XGBoost Regressor.

Dataset

The project utilizes two datasets:

Exercise Data: Contains information on various physical activities.

Calories Data: Includes the corresponding calorie expenditure.

The datasets are merged into a single DataFrame for model training.

Technologies Used

Python

Pandas (Data manipulation)

NumPy (Numerical operations)

Matplotlib & Seaborn (Data visualization)

Scikit-Learn (Machine learning utilities)

XGBoost (Regressor for predictions)

Model Training

The dataset is preprocessed and split into training and testing sets using train_test_split(). The XGBoost Regressor is trained on the dataset, and predictions are made on the test data.

Performance Metrics

To evaluate the model, the following metrics are used:

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

R² Score (Converted to accuracy percentage)

How to Run

Install dependencies:

pip install numpy pandas matplotlib seaborn scikit-learn xgboost

Run the Jupyter Notebook or Python script to train the model and evaluate performance.

The model will output predictions and performance metrics.

Accuracy Calculation

The accuracy of the model is calculated using:

accuracy = (1 - (mse / np.var(y_test))) * 100
print(f"Model Accuracy: {accuracy:.2f}%")

Contribution

Feel free to fork the repository and make improvements. Pull requests are welcome!
