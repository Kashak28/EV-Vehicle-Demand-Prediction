# 🚗 EV Vehicle Demand Prediction using Machine Learning & FastAPI

## 📌 Project Overview

This project predicts future Electric Vehicle (EV) adoption using Machine Learning. It analyzes historical EV registration data, performs feature engineering, trains a Random Forest Regressor with hyperparameter tuning, and forecasts EV demand for the next 36 months at the county level.

The project also includes a FastAPI-based REST API that allows users to obtain EV demand predictions through HTTP requests.

---

## 🚀 Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Outlier detection and treatment using IQR
- Feature engineering for time-series forecasting
- Lag feature creation
- Rolling statistics
- Growth rate and trend calculation
- Random Forest Regression model
- Hyperparameter tuning using RandomizedSearchCV
- Model evaluation using MAE, RMSE, and R² Score
- 36-month EV demand forecasting
- Feature importance visualization
- FastAPI REST API for real-time predictions
- Model serialization using Joblib

---

## 📊 Dataset

The dataset contains historical monthly EV registration information including:

- County
- State
- Date
- Battery Electric Vehicles (BEVs)
- Plug-in Hybrid Electric Vehicles (PHEVs)
- Electric Vehicle Total
- Non-Electric Vehicle Total
- Total Vehicles
- Percent Electric Vehicles

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Jupyter Notebook

---

## 🧠 Machine Learning Pipeline

1. Load dataset
2. Clean missing values
3. Detect and cap outliers
4. Convert data types
5. Feature engineering
6. Create lag features
7. Create rolling averages
8. Calculate percentage growth
9. Generate cumulative EV growth
10. Train Random Forest Regressor
11. Hyperparameter tuning using RandomizedSearchCV
12. Evaluate model
13. Forecast EV adoption
14. Save trained model
15. Serve predictions through FastAPI

---

## 📈 Model Features

The model uses the following features:

- months_since_start
- county_encoded
- ev_total_lag1
- ev_total_lag2
- ev_total_lag3
- ev_total_roll_mean_3
- ev_total_pct_change_1
- ev_total_pct_change_3
- ev_growth_slope

Target Variable:

- Electric Vehicle (EV) Total

---

## 📊 Model Evaluation

The model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🌐 FastAPI

The project includes a REST API built using FastAPI.

### Start the API

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home

```
GET /
```

Returns the API status.

### Predict EV Demand

```
POST /predict
```

Example Request

```json
{
  "months_since_start": 97.0,
  "county_encoded": 270.0,
  "ev_total_lag1": 1.0,
  "ev_total_lag2": 1.0,
  "ev_total_lag3": 1.0,
  "ev_total_roll_mean_3": 1.0,
  "ev_total_pct_change_1": 0.0,
  "ev_total_pct_change_3": 0.0,
  "ev_growth_slope": 1.0
}
```

Example Response

```json
{
  "predicted_ev_count": 1
}
```

---

## 📂 Project Structure

```
EV-Vehicle-Demand-Prediction/
│
├── EV Forecasting.ipynb
├── app.py
├── forecasting_ev_model.pkl
├── requirements.txt
├── README.md
└── preprocessed_ev_data.csv
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/EV-Vehicle-Demand-Prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn app:app --reload
```

---

## 💡 Future Improvements

- Accept county names instead of encoded values
- Deploy the API on Render or Azure
- Build an interactive Streamlit dashboard
- Integrate real-time EV registration data
- Add charging station and population data for improved forecasting

---

## 📌 Real-World Applications

- Government EV policy planning
- Charging infrastructure development
- Power grid demand forecasting
- Automotive market analysis
- Smart city planning

---

## 👨‍💻 Author

**Kashak Tripathi**

B.Tech Computer Science & Engineering

Machine Learning | Data Science | Python | FastAPI
