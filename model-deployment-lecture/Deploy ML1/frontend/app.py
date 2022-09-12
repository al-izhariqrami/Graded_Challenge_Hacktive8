import streamlit as st
import requests

st.title("Pendeteksi Churn Pelanggan")
tenure = st.number_input("Tenure")
OnlineSecurity = st.selectbox("Online Security", [0, 1, 2])
TechSupport	 = st.selectbox("Tech Support", [0, 1, 2])
Contract = st.selectbox("Contract", [0, 1, 2])
MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")
# inference
data = {'tenure': tenure,
        'OnlineSecurity': OnlineSecurity,
        'TechSupport': TechSupport,
        'Contract': Contract,
        'MonthlyCharges':MonthlyCharges,
        'TotalCharges': TotalCharges}

#URL = "http://127.0.0.1:5000/predict" # sebelum push backend
URL = "https://izhar-ml2-backend.herokuapp.com/predict" # setelah push backend

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['class_name'])
elif r.status_code == 400:
    st.title("ERROR BOSS")
    st.write(res['message'])