# simple linear regression - univariate regression
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib

# To intialise a 2D array with one column and mulitple rows 
x=np.array([1,2,3,4,5,6,7,8]).reshape(-1,1) # independent variable

# To intialise a 1D array 
y=np.array([2,4,6,8,10,5,14,16]) # dependent variable

# Creating a model
model=LinearRegression()

# finding the fitting curve values
model.fit(x,y)

m=model.coef_
c=model.intercept_
# y=mx+c
# plots

# Testing the prediction
x_new=np.array([6,7]).reshape(-1,1)
y_pred=x_new*m+c
print(y_pred)





