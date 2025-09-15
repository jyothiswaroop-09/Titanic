## 🚢 Titanic Survival Prediction
This project uses the famous Titanic dataset to predict whether a passenger survived or not, based on features such as age, gender, class, and family relations.
It applies data preprocessing, feature engineering, and machine learning models to achieve accurate predictions.
```
📂 Project Structure
├── data/
│   ├── train.csv      # Training dataset
│   ├── test.csv       # Test dataset
│   └── gender_submission.csv
├── notebooks/
│   └── Titanic_EDA.ipynb   # Exploratory Data Analysis
│   └── Model_Training.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── utils.py
├── artifacts/              # Saved models, preprocessing objects
├── requirements.txt
└── README.md

📊 Dataset
The dataset is provided by Kaggle Titanic Competition.
train.csv → Training data with survival labels
test.csv → Test data without survival labels
gender_submission.csv → Sample submission format

Features:
PassengerId – Unique ID
Pclass – Ticket class (1, 2, 3)
Name – Passenger’s name
Sex – Gender
Age – Age in years
SibSp – # of siblings/spouses aboard
Parch – # of parents/children aboard
Ticket – Ticket number
Fare – Passenger fare
Cabin – Cabin number
Embarked – Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
Target: Survived (0 = No, 1 = Yes)

⚙️ Installation
Clone the repo: git clone https://github.com/your-username/titanic-survival-prediction.git
cd titanic-survival-prediction

Install dependencies:
pip install -r requirements.txt

🚀 Usage
Run preprocessing & model training
python src/data_preprocessing.py
python src/model_training.py
Run Jupyter Notebook
jupyter notebook notebooks/Titanic_EDA.ipynb

📈 Models Implemented
Logistic Regression
Random Forest
XGBoost
Support Vector Machine

Evaluation Metrics:
Accuracy
Precision, Recall, F1-Score
Confusion Matrix

📊 Results
Model	Accuracy
Logistic Regression	78%
Random Forest	82%
XGBoost	84%
SVM	80%
✅ Best Performing Model: XGBoost (84% Accuracy)

🖥️ Dashboard (Optional)
If you deploy with Streamlit/Flask, you can add an interactive dashboard to test predictions. Example:

streamlit run app.py
```
👨‍💻 Author
Jyothi Swaroop GitHub: jyothiswaroop-09 Email: swaroop.motupalii@gmail.com

