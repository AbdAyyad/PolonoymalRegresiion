# Polynomial Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# fitting regressor to dataset
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

# build polynomial regressor
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# visualising linear data
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('truth of bluff (Linear Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(x_poly), color='blue')
plt.title('truth of bluff (Polynomial Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()
