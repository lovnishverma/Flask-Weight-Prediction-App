# 📏 Weight Prediction Web App (Flask + Linear Regression)

A **machine learning web application** built with **Flask** to predict human **weight** (in kilograms) based on **gender and height** using a **Linear Regression** model.

---

## 🎯 Objective

Predict human weight using a simple regression model trained on a height/gender dataset. This project demonstrates:

✅ A clear **Machine Learning workflow** (data preprocessing, model training, prediction)

✅ A clean, minimal **Flask web app** for deployment

✅ **Best practices** suitable for beginner ML + web developers

---

## 🛠️ Tech Stack

| Technology        | Usage                                |
| ----------------- | ------------------------------------ |
| **Python**        | Core programming language            |
| **Flask**         | Web framework                        |
| **Pandas**        | Data processing                      |
| **scikit-learn**  | Machine Learning (Linear Regression) |
| **HTML (Jinja2)** | Frontend templates                   |

---

## 📊 Dataset Details

**File:** `weight-height.csv`
**Columns:** `Gender`, `Height (inches)`, `Weight (pounds)`

| Gender | Height (inches) | Weight (pounds) |
| ------ | --------------- | --------------- |
| Male   | 73.84           | 241.89          |
| Male   | 68.78           | 162.31          |
| Female | 65.00           | 135.00          |

### ⚙️ Preprocessing:

* **Gender** encoded as: `Male → 1`, `Female → 0`
* **Weight (pounds)** is converted to **kilograms** for final output.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/lovnishverma/Flask-Weight-Prediction-App.git
cd Flask-Weight-Prediction-App
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**

```
Flask
pandas
scikit-learn
numpy
```

### 3️⃣ Run the App

```bash
python app.py
```

### 4️⃣ Open in Browser

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🖥️ App Workflow

### 🔹 Input:

* **Gender**: `Male` / `Female`
* **Height**: Inches (numeric)

### 🔹 Output:

* **Predicted Weight**: Shown in **kilograms (kg)**

---

## 📂 Project Structure

```
├── app.py               # Main Flask App with ML logic
├── templates/
│   └── index.html        # Input form UI
├── weight-height.csv     # Dataset (Height in inches, Weight in pounds)
├── requirements.txt      # Dependencies
└── README.md             # Project Documentation
```

---

## 🔍 Example Prediction

**Input:**

```
Gender: Male
Height: 70 inches
```

**Output:**

```
Predicted Weight: 90.56 kg
```

---

## 📌 Key Highlights (For ML Practitioners)

✅ **Proper ML pipeline:** Load → Encode → Train → Predict
✅ **Model efficiency:** Trained once at app startup, not per request
✅ **Type-safe, readable code**
✅ **Good error handling** for invalid inputs
✅ **Clean ML-to-API integration with Flask**

---

## 🚧 Known Limitations

* No persistent model storage (`joblib` recommended for production)
* Small sample dataset; accuracy is purely for demonstration
* Only height and gender used; lacks other health indicators

---

## 🔮 Future Enhancements

* Use a larger, more realistic dataset
* Store trained model via `joblib`
* Provide BMI and health category alongside prediction
* Deploy to **Render / Railway / Heroku**
* Add unit tests and CI/CD workflows

---

## 📄 License

**MIT License** — Free to use for educational and commercial purposes.

---

## 🙌 Acknowledgements

* Inspired by classic height-weight datasets.
* Built using **Flask** and **scikit-learn** for rapid prototyping.

---
