import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("housing_data.csv", skiprows=1)
data.columns = ["Area", "Bedrooms", "Bathrooms", "Price"]

X = data[["Area", "Bedrooms", "Bathrooms"]]
y = data["Price"]

model = LinearRegression()
model.fit(X, y)

st.title("🏠 House Price Predictor")

area = st.number_input("Enter Area")
bedrooms = st.number_input("Enter Bedrooms")
bathrooms = st.number_input("Enter Bathrooms")

if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bedrooms, bathrooms]],
                              columns=["Area", "Bedrooms", "Bathrooms"])
    
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ₹ {int(prediction[0])}")
