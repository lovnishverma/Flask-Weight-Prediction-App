from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load dataset
dataset = pd.read_csv('weight-height.csv')

# Encode Gender
le = LabelEncoder()
dataset['Gender'] = le.fit_transform(dataset['Gender'])  # Male=1, Female=0

# Features and Labels
X = dataset[['Gender', 'Height']]
y = dataset['Weight']

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
        prediction = model.predict([[gender_encoded, height]])[0]
        result = f"{prediction:.2f} hectograms (hg)"
    except (ValueError, TypeError):
        result = "Invalid input."

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
