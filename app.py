from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Global model and features initialization to avoid retraining on each request
model: LinearRegression = LinearRegression()
feature_columns: list[str] = ['Height', 'Gender']


def load_dataset(filepath: str = "weight-height.csv") -> pd.DataFrame:
    """
    Load and preprocess the dataset.
    Converts 'Gender' to numeric: Male -> 1, Female -> 0.
    """
    df = pd.read_csv(filepath)
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    return df


def train_model(dataframe: pd.DataFrame) -> None:
    """
    Train the linear regression model on Height and Gender to predict Weight.
    """
    X = dataframe[feature_columns]
    y = dataframe['Weight']
    model.fit(X, y)


def predict_weight(height: float, gender: str) -> float:
    """
    Predict weight given height and gender.
    Converts Gender to numeric internally.
    Returns weight in hectograms for demo purposes.
    """
    gender_numeric = 1 if gender == 'Male' else 0
    input_features = np.array([[height, gender_numeric]])
    predicted_weight = model.predict(input_features)[0]
    # Convert pounds to hectograms (for display)
    return predicted_weight / 10.0


@app.route('/')
def index() -> str:
    """
    Renders the input form page.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict() -> str:
    """
    Handles prediction POST request and renders result.
    """
    try:
        gender = request.form.get('Gender')
        height = float(request.form.get('Height'))
        predicted_weight_hg = predict_weight(height, gender)
        return render_template('result.html', prediction=predicted_weight_hg)
    except (ValueError, TypeError):
        return render_template('result.html', prediction="Invalid input.")


if __name__ == '__main__':
    # Load data and train model once at startup
    dataset = load_dataset()
    train_model(dataset)

    app.run(debug=True)
# This code initializes the Flask app, loads the dataset, trains the model, and sets up routes for prediction.
# The model is trained once at startup to improve performance on subsequent requests.
# The prediction function handles user input and returns the predicted weight in hectograms.
# The app uses templates to render the input form and display results.
