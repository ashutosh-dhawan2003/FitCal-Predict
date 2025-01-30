import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QPixmap, QPalette, QBrush
from PyQt6.QtCore import Qt
import numpy as np
import pickle

# Load trained model
model_filename = "calorie_model.pkl"  # Ensure model.pkl is correct
with open(model_filename, "rb") as file:
    model = pickle.load(file)

class CaloriePredictor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calorie Predictor")
        self.setGeometry(100, 100, 800, 600)  

        # Set background image
        palette = QPalette()
        pixmap = QPixmap("background.jpeg")  # Ensure this image exists
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.inputs = {}
        self.labels = ["Age", "Weight", "Height", "Duration", "Heart Rate", "Body Temp"]
        
        # Add input fields
        for label in self.labels:
            lbl = QLabel(f"<b>{label}</b>")
            lbl.setStyleSheet("color: white; font-size: 16px;")
            input_field = QLineEdit()
            input_field.setStyleSheet("background-color: rgba(255, 255, 255, 0.8); color: black; padding: 5px; font-size: 14px;")
            self.inputs[label] = input_field
            layout.addWidget(lbl)
            layout.addWidget(input_field)
        
        # Add Gender Selection (0 = Male, 1 = Female)
        gender_lbl = QLabel("<b>Gender</b>")
        gender_lbl.setStyleSheet("color: white; font-size: 16px;")
        self.gender_box = QComboBox()
        self.gender_box.addItems(["Male", "Female"])
        self.gender_box.setStyleSheet("background-color: rgba(255, 255, 255, 0.8); color: black; padding: 5px; font-size: 14px;")
        
        layout.addWidget(gender_lbl)
        layout.addWidget(self.gender_box)

        # Predict button
        self.predict_button = QPushButton("Predict Calories")
        self.predict_button.setStyleSheet("background-color: #ff5733; color: white; padding: 10px; font-size: 16px; border-radius: 5px;")
        self.predict_button.clicked.connect(self.predict_calories)
        layout.addWidget(self.predict_button)
        
        # Result label
        self.result_label = QLabel("Predicted Calories: ")
        self.result_label.setStyleSheet("color: yellow; font-size: 18px;")
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)

    def predict_calories(self):
        try:
            user_data = []
            print("---- USER INPUTS ----")  # Debugging

            for label in self.labels:
                text = self.inputs[label].text().strip()
                print(f"{label}: '{text}'")  # Debugging
                
                if text == "":
                    raise ValueError(f"❌ Missing input for {label}")

                user_data.append(float(text))  # Convert input to float

            # Handle Gender (Male = 0, Female = 1)
            gender_value = 0 if self.gender_box.currentText() == "Male" else 1
            user_data.append(gender_value)
            print("✅ Processed User Data:", user_data)  

            # Convert input to NumPy array
            input_array = np.array([user_data])
            print("📊 Input Array Shape:", input_array.shape)

            prediction = model.predict(input_array)[0]
            print("🔥 Prediction:", prediction)

            self.result_label.setText(f"Predicted Calories: {prediction:.2f}")

        except ValueError as ve:
            self.result_label.setText("Invalid Input: Enter numeric values")
            print("❌ ValueError:", ve)

        except Exception as e:
            self.result_label.setText("Error in Prediction")
            print("❌ Unexpected Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaloriePredictor()
    window.showMaximized()
    sys.exit(app.exec())
