import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("housing_data.csv", skiprows=1)
data.columns = ["Area", "Bedrooms", "Bathrooms", "Price"]

print(data.head())

# Scatter Plot
plt.scatter(data['Area'], data['Price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# Bar Graph
plt.bar(data['Bedrooms'], data['Price'])
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Bedrooms vs Price")
plt.show()
