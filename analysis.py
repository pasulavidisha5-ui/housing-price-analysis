import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("housing_data.csv", skiprows=1)
data.columns = ["Area", "Bedrooms", "Bathrooms", "Price"]

# Features and target
X = data[["Area", "Bedrooms", "Bathrooms"]]
y = data["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

# User input
area = int(input("Enter Area: "))
bedrooms = int(input("Enter Bedrooms: "))
bathrooms = int(input("Enter Bathrooms: "))

# Proper input format (no warning)
input_data = pd.DataFrame([[area, bedrooms, bathrooms]], 
                          columns=["Area", "Bedrooms", "Bathrooms"])

# Prediction
prediction = model.predict(input_data)

print("Estimated House Price:", int(prediction[0]))
