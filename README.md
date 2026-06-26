# 🚗 EV Vehicle Demand Prediction using Machine Learning & FastAPI

## 📌 Project Overview

EV Vehicle Demand Prediction is a Machine Learning project that forecasts future Electric Vehicle (EV) adoption using historical EV registration data. The project performs data preprocessing, feature engineering, time-series forecasting, and model optimization using Random Forest Regression.

To make predictions accessible in real time, the trained model is deployed through a FastAPI REST API and hosted on Render with interactive Swagger documentation.

---

## 🚀 Features

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Outlier detection and treatment using IQR
* Time-series feature engineering
* Lag feature creation
* Rolling statistics and trend analysis
* Growth rate calculation
* Random Forest Regression model
* Hyperparameter tuning using RandomizedSearchCV
* Model evaluation using MAE, RMSE, and R² Score
* 36-month EV demand forecasting
* Feature importance visualization
* FastAPI REST API deployment
* Cloud deployment on Render
* Interactive Swagger API documentation

---

## 📊 Dataset

The dataset contains historical EV registration information including:

* County
* State
* Date
* Battery Electric Vehicles (BEVs)
* Plug-in Hybrid Electric Vehicles (PHEVs)
* Electric Vehicle Total
* Non-Electric Vehicle Total
* Total Vehicles
* Percent Electric Vehicles

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib
* Jupyter Notebook
* Render

---

## 🧠 Machine Learning Pipeline

1. Load and preprocess dataset
2. Handle missing values
3. Detect and cap outliers using IQR
4. Convert and validate data types
5. Perform feature engineering
6. Generate lag features
7. Calculate rolling averages
8. Compute growth metrics
9. Train Random Forest Regressor
10. Hyperparameter tuning with RandomizedSearchCV
11. Evaluate model performance
12. Forecast future EV demand
13. Save trained model using Joblib
14. Serve predictions through FastAPI

---

## 📈 Model Features

### Input Features

* months_since_start
* county_encoded
* ev_total_lag1
* ev_total_lag2
* ev_total_lag3
* ev_total_roll_mean_3
* ev_total_pct_change_1
* ev_total_pct_change_3
* ev_growth_slope

### Target Variable

* Electric Vehicle (EV) Total

---

## 📊 Model Evaluation

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🏆 Project Outcomes

* Built a Random Forest Regression model for EV demand forecasting.
* Engineered lag-based and rolling-window features to improve predictive performance.
* Forecasted EV adoption trends for the next 36 months.
* Developed a FastAPI REST API for real-time predictions.
* Successfully deployed the model on Render.
* Enabled API testing through interactive Swagger documentation.

---

## 🌍 Live Deployment

### Live API

https://ev-forecast-api.onrender.com

### Swagger Documentation

https://ev-forecast-api.onrender.com/docs

### GitHub Repository

https://github.com/Kashak28/EV-Vehicle-Demand-Prediction

---

## 🌐 API Endpoints

### Home Endpoint

```http
GET /
```

Returns API status.

### Prediction Endpoint

```http
POST /predict
```

### Example Request

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

### Example Response

```json
{
  "predicted_ev_count": 1
}
```

---

## 📂 Project Structure

```text
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

## ▶️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Kashak28/EV-Vehicle-Demand-Prediction.git
cd EV-Vehicle-Demand-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Server

```bash
uvicorn app:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## 💡 Future Improvements

* Accept county names instead of encoded values
* Build an interactive Streamlit dashboard
* Integrate real-time EV registration data
* Add charging station and population data for improved forecasting
* Deploy on Azure Cloud for enterprise-scale usage

---

## 📌 Real-World Applications

* Government EV policy planning
* Charging infrastructure development
* Power grid demand forecasting
* Automotive market analysis
* Smart city planning
* Sustainable transportation research

---

## 👨‍💻 Author

**Kashak Tripathi**

B.Tech Computer Science & Engineering, PSIT Kanpur

Machine Learning | Data Science | Python | FastAPI | Scikit-learn
