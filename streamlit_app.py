import streamlit as st
import requests

st.title("🚗 EV Vehicle Demand Prediction")

months_since_start = st.number_input("Months Since Start", value=97.0)
county_encoded = st.number_input("County Encoded", value=270.0)
ev_total_lag1 = st.number_input("EV Total Lag 1", value=1.0)
ev_total_lag2 = st.number_input("EV Total Lag 2", value=1.0)
ev_total_lag3 = st.number_input("EV Total Lag 3", value=1.0)
ev_total_roll_mean_3 = st.number_input("Rolling Mean 3", value=1.0)
ev_total_pct_change_1 = st.number_input("Pct Change 1", value=0.0)
ev_total_pct_change_3 = st.number_input("Pct Change 3", value=0.0)
ev_growth_slope = st.number_input("Growth Slope", value=1.0)

if st.button("Predict EV Demand"):

    payload = {
        "months_since_start": months_since_start,
        "county_encoded": county_encoded,
        "ev_total_lag1": ev_total_lag1,
        "ev_total_lag2": ev_total_lag2,
        "ev_total_lag3": ev_total_lag3,
        "ev_total_roll_mean_3": ev_total_roll_mean_3,
        "ev_total_pct_change_1": ev_total_pct_change_1,
        "ev_total_pct_change_3": ev_total_pct_change_3,
        "ev_growth_slope": ev_growth_slope
    }

    response = requests.post(
        "https://ev-forecast-api.onrender.com/predict",
        json=payload
    )

    if response.status_code == 200:
        prediction = response.json()["predicted_ev_count"]
        st.success(f"Predicted EV Count: {prediction:.2f}")
    else:
        st.error("Prediction failed")