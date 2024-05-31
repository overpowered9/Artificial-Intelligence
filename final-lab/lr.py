import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv('./FuelConsumptionCo2.csv')

print(df.head())

X = df[['ENGINESIZE']]
y = df['CO2EMISSIONS']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

intercept = model.intercept_
coefficients = model.coef_
print(f'Intercept: {intercept}')
print(f'Coefficients: {coefficients}')
enginecc=2.5
engine_size_2_5 = np.array([[enginecc]])
predicted_co2_2_5 = model.predict(engine_size_2_5)
print(f'Predicted CO2 emissions for a vehicle with a {enginecc}-liter engine: {predicted_co2_2_5[0]}')

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R2): {r2}')
