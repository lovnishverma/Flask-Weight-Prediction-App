# 📏 Weight Prediction Web App (Flask + Linear Regression)

A **machine learning web application** built with **Flask** to predict human **weight** (in hectograms) based on **gender and height** using a **Linear Regression** model.

---

## 🎯 Objective

Predict human weight using a simple regression model trained on a height/gender dataset. This project demonstrates:

* A clear **ML workflow** (data preprocessing, model training, prediction)
* A clean **Flask web app** for deployment
* **Good code practices** suitable for ML and web developers

---

## 🛠️ Tech Stack

| Technology        | Usage                                |
| ----------------- | ------------------------------------ |
| **Python**        | Core language                        |
| **Flask**         | Web Framework                        |
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
| ...    | ...             | ...             |

**Preprocessing:**

* `Gender`: Encoded as `Male → 1`, `Female → 0`

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

**`requirements.txt`**

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

1️⃣ User inputs:

* **Gender**: `Male` / `Female`
* **Height**: Inches (float)

2️⃣ App predicts:

* **Weight** (in **hectograms** for demonstration)

3️⃣ **Prediction Example:**

```plaintext
Height: 70 inches, Gender: Male
Predicted Weight: 820.4 hg
```

---

## 📂 Project Structure

```
├── app.py                 # Main Flask App with ML logic
├── templates/
│   ├── index.html          # Input form
│   └── result.html         # Prediction result
├── weight-height.csv       # Dataset
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## 📌 Key Highlights (For ML Experts)

✅ **ML pipeline**: Cleanly separated (Load → Preprocess → Train → Predict)
✅ **Model efficiency**: Trained once on startup, not per request
✅ **Type hints**: Used for code clarity
✅ **Proper error handling**
✅ **Demonstrates ML → API integration cleanly**

---

## 🚧 Known Limitations

* Very **small dataset**, model accuracy is basic.
* Converts prediction to **hectograms** artificially for demo purposes.
* No persistent model storage (can be enhanced with `joblib`).

---

## 🔮 Future Enhancements

* Switch to a larger, realistic dataset.
* Use a **persisted model** with `joblib`.
* Provide BMI or health insights.
* Deploy to **Render / Railway / Heroku**.
* Add **unit tests** and CI.

---

## 📄 License

MIT License — Free for educational and commercial use.

---

## 🙌 Acknowledgements

* Dataset inspired by common height-weight sample datasets.
* Flask and scikit-learn for enabling rapid prototyping.

---


