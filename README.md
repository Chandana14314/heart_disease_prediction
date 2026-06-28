# ❤️ Heart Disease Prediction System

## 📖 Project Description

The Heart Disease Prediction System is a Machine Learning web application developed using **Python**, **Flask**, **HTML**, **CSS**, and **Scikit-learn**.

The application predicts whether a person is at risk of heart disease based on medical information entered by the user.

The trained machine learning model processes the input values and instantly displays the prediction result on the webpage.

---

# 🚀 Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Deployment
- GitHub
- Render

---

# 📁 Project Structure

```
Heart_Disease_Prediction/
│
├── app.py
├── heart.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates/
│      └── index.html
│
├── static/
│      ├── css/
│      ├── js/
│      └── images/
│
└── README.md
```

---

# 📂 File-by-File Explanation

## 1. app.py

### Purpose

This is the main backend file of the project.

It performs the following tasks:

- Creates the Flask application
- Loads the trained machine learning model
- Loads the scaler
- Receives user input from the HTML form
- Converts the input into numerical format
- Sends the data to the machine learning model
- Gets the prediction result
- Displays the prediction on the webpage

Without this file, the website cannot communicate with the machine learning model.

---

## 2. model.pkl

### Purpose

This file stores the trained machine learning model.

Instead of training the model every time the application starts, the saved model is loaded directly using Joblib.

Advantages:

- Faster prediction
- Reduced loading time
- No need for retraining

---

## 3. scaler.pkl

### Purpose

Machine learning models work better when numerical data is scaled.

This file stores the trained StandardScaler.

Whenever the user enters values:

Input Data

↓

Scaler

↓

Machine Learning Model

↓

Prediction

---

## 4. heart.csv

### Purpose

This dataset is used to train the machine learning model.

It contains patient information such as:

- Age
- Gender
- Blood Pressure
- Cholesterol
- Chest Pain Type
- ECG Results
- Maximum Heart Rate
- Exercise Angina

The last column represents whether heart disease is present.

---

## 5. templates/index.html

### Purpose

This file is the frontend of the application.

Responsibilities:

- Displays the webpage
- Collects user input
- Sends input to Flask
- Displays prediction result

The browser loads this file first.

---

## 6. static/css

### Purpose

Contains all CSS styling files.

Used for:

- Colors
- Layout
- Buttons
- Responsive Design
- Animations
- Fonts

Separating CSS keeps the project organized.

---

## 7. static/js

### Purpose

Contains JavaScript files.

Used for:

- Form validation
- Interactive buttons
- Animations
- Dynamic content

---

## 8. static/images

### Purpose

Stores all project images.

Examples:

- Heart images
- Background images
- Icons
- Logos

---

## 9. requirements.txt

### Purpose

Lists all Python libraries required by the project.

Example:

Flask
NumPy
Pandas
Scikit-learn
Joblib
Gunicorn

Install using:

pip install -r requirements.txt

---

## 10. Procfile

### Purpose

Required for deployment on Render.

It tells Render how to start the Flask application.

Example:

web: gunicorn app:app

Meaning:

app.py

↓

Flask App

↓

Gunicorn Server

↓

Render

---

## 11. runtime.txt

### Purpose

Specifies the Python version.

Example:

python-3.12.8

Render installs this Python version before deployment.

---

## 12. README.md

### Purpose

Provides complete project documentation.

Includes:

- Project overview
- Installation guide
- Folder structure
- Features
- Technologies
- Deployment instructions

GitHub automatically displays this file on the repository home page.

---

# 🔄 Project Workflow

```
User Opens Website
        │
        ▼
HTML Form Displays
        │
        ▼
User Enters Medical Details
        │
        ▼
Flask Receives Data
        │
        ▼
Data Validation
        │
        ▼
Data Scaling
        │
        ▼
Machine Learning Model
        │
        ▼
Prediction Generated
        │
        ▼
Result Displayed on Website
```

---

# ▶️ How to Run the Project

### Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/Heart_Disease_Prediction.git
```

---

### Step 2

Move into the project folder

```bash
cd Heart_Disease_Prediction
```

---

### Step 3

Install dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4

Run the application

```bash
python app.py
```

---

### Step 5

Open your browser

```
http://127.0.0.1:5000/
```

---

# 🚀 Deployment

Push the project to GitHub.

Connect the repository to Render.

Render automatically:

- Installs dependencies
- Starts Gunicorn
- Deploys the application
- Provides a public URL

---

# ✨ Features

- Heart Disease Prediction
- Responsive Interface
- Machine Learning Integration
- Flask Backend
- Real-Time Prediction
- Easy Deployment
- User-Friendly Design

---

# 🔮 Future Enhancements

- User Authentication
- Prediction History
- Doctor Recommendation
- PDF Report Download
- Database Integration
- Email Notifications
- Dashboard with Charts

---

# 👩‍💻 Author

**Chandana P**

Bachelor of Technology

Email:
pchandana745@gmail.com

GitHub:
https://github.com/yourusername

---

# 📜 License

This project is created for educational purposes and learning Machine Learning with Flask.

---

⭐ If you like this project, please consider giving it a star on GitHub.
