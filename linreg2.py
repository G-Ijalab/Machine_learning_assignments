from time import *
import random
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating datas for linear regression
x=np.array(range(0,100))
y=np.array([random.randint(0,i) for i in range(0,100)])

fig1, axs1 = plt.subplots(1,2)
axs1[0].scatter(x, y)
axs1[0].set_title('Data points')
axs1[1].set_title('GD algorithm')

# Applying gradient descent method minimize loss function and find appropriate m and b values of fitting curve
m=0.0               # slope
b=0.0               # intercept
noi=100             # number of iterations
n=float(len(x))     # length of x
l=0.0001            # learning factor
pred=lambda x,m,b:x*m+b
# Defining gradient algorithm usinf function to implement dynamic plot updation to visualize the process of estimating the approriate m and b values 

def gd_process(frame):
    global m,b
    yp=pred(x,m,b)
    ln=axs1[1].plot(x, yp)
    dm= (-2/n)*sum(x*(y-yp)) # derivative of loss function wrt. m
    db= (-2/n)*sum(y-yp)    # derivative of loss function wrt. b
    # updating m and b values such a way loss fucntion is updated
    m=m-l*dm
    b=b-l*db  
    return ln

animation = FuncAnimation(fig1,gd_process,frames=noi,interval=1,repeat=False)
plt.show()

# Now prompting values from user for predicting dependent variable values with prompted independent variable values

fig2, axs2 = plt.subplots(1,2)
axs2[0].scatter(x, y)
axs2[0].plot(x,pred(x,m,b),'red')
axs2[0].set_title('Data points and fitting curve')
axs2[1].set_title('Prompt and Prediction')

print('Prediction: ')
print("")
x_prompt=int(input('X value : '))
y_pred=m*x_prompt+b
y_ac=y[x_prompt-1]
print("Predicted value : ",y_pred)
print("")
print("Actual value : ",y_ac)
axs2[1].plot(x,pred(x,m,b),'red')
axs2[1].scatter(x_prompt,y_ac)
axs2[1].scatter(x_prompt,y_pred)
plt.show()


