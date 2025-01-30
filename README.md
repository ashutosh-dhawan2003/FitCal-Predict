## FitCal-Predict

## Overview
Calorie Predictor is a desktop application built using Python and PyQt6 that predicts the number of calories burned based on user inputs such as age, weight, height, exercise duration, heart rate, and body temperature. It leverages a pre-trained machine learning model for predictions.

## Features
- **User-friendly GUI**: Designed using PyQt6 with an intuitive layout.
- **Background Image Support**: Customizable interface with background images.
- **Machine Learning Integration**: Uses a trained model to predict calorie expenditure.
- **Real-time Input Validation**: Ensures users provide valid numerical data.
- **Jupyter Notebook for Model Training**: Includes an `.ipynb` file for training and evaluating the model.

## Technologies Used
- **Python**
- **PyQt6** (for GUI development)
- **NumPy** (for data handling)
- **Pickle** (for loading the trained model)
- **Scikit-learn** (for machine learning model training and evaluation)
- **Matplotlib & Seaborn** (for data visualization in Jupyter Notebook)
- **Pandas** (for data preprocessing)

## Installation
### Prerequisites
Ensure you have Python installed (version 3.8 or higher recommended).

### Install Required Packages
```bash
pip install PyQt6 numpy pickle-mixin pandas scikit-learn matplotlib seaborn jupyter
```

## Usage
1. Clone the repository or download the project files.
2. Ensure the trained model (`calorie_model.pkl`) and background image (`background.jpeg`) exist in the project directory.
3. Run the application:
```bash
python main_gui.py
```
4. Enter the required details (Age, Weight, Height, Duration, Heart Rate, Body Temp, and Gender) and click **Predict Calories**.
5. The predicted calories burned will be displayed on the screen.

## Jupyter Notebook (`1.ipynb`)
This file contains the following:
- **Data Preprocessing**: Cleaning and normalizing dataset.
- **Feature Engineering**: Selecting relevant input features.
- **Model Training**: Training machine learning models (e.g., Linear Regression, Decision Trees, etc.).
- **Model Evaluation**: Using accuracy metrics like RMSE and R².
- **Model Export**: Saving the trained model as `calorie_model.pkl` for use in the GUI application.

### Running the Notebook
To run the notebook, use the following command:
```bash
jupyter notebook 1.ipynb
```
This will open Jupyter Notebook in your browser. Execute the cells sequentially to train and evaluate the model.

## Screenshots

![Screenshot (313)](https://github.com/user-attachments/assets/cf35b60b-f748-4a88-bf67-0fe0c6e76575)

## Future Enhancements
- Improve UI/UX with more interactive elements.
- Support additional input features for better predictions.
- Deploy as a web application for broader accessibility.
- Implement deep learning models for improved accuracy.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or fixes.

## License
This project is licensed under the MIT License.
