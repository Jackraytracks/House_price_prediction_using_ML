import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Replace with your dataset
data = pd.DataFrame({
    'area': [1000, 1500, 2000, 1200],
    'bedrooms': [2, 3, 4, 2],
    'bathrooms': [1, 2, 2, 1],
    'price': [50, 70, 100, 60]  # in Lakhs
})

X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
