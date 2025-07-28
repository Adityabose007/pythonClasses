import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# sample data
x = np.array([1,2,3,4,5,6]).reshape(-1, 1)  # Reshape for sklearn
y= np.array([15,20,30,44,70,55])



model = LinearRegression()
# Train the data
model.fit(x,y)
#prediction
y_pred = model.predict(x)

y_pred2 = model.predict([[8.5]])
print("The output:", y_pred2)

print("")

#model parameter 
print("Slope: (m):", model.coef_[0])
print("Intercept: (c):", model.intercept_)

#plotting
plt.scatter(x,y , color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Regresion Line')
plt.xlabel("Hours Studied")
plt.ylabel("Score")

plt.title("Linear Regression")
plt.legend()
plt.show()




