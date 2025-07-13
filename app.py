from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load dataset from CSV
dataset = pd.read_csv('data.csv')

# Encode Gender (Male=1, Female=0)
le = LabelEncoder()
dataset['Gender'] = le.fit_transform(dataset['Gender'])

# Features and Labels
X = dataset[['Gender', 'Height']]
y = dataset['Weight']  # Weight is in lbs

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = request.form.get('gender')
        gender_encoded = 1 if gender.lower() == 'male' else 0

        height = float(request.form.get('height'))
        predicted_lbs = model.predict([[gender_encoded, height]])[0]

        # Convert pounds to kilograms
        predicted_kg = predicted_lbs / 2.20462
        result = f"{predicted_kg:.2f} kilograms (kg)"
    except (ValueError, TypeError):
        result = "Invalid input."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
