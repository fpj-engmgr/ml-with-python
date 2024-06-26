import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

FILE_PATH = '/Users/fpj/Development/python/ml-with-python/linear-regression/data/'
FILE_NAME = 'FuelConsumptionCo2.csv'
DATA_FILE = FILE_PATH + FILE_NAME

df = pd.read_csv(DATA_FILE)

# take a look at the dataset
#print(df.head())

# summarize the data
#print(df.describe())

# create a dataset of the features we are interested in
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
#cdf.head(9)

#viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
#viz.hist()
#plt.show()

#lt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("FUELCONSUMPTION_COMB")
#plt.ylabel("Emission")
#plt.show()

#plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("Engine size")
#plt.ylabel("Emission")
#plt.show()

#plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("CYLINDERS")
#plt.ylabel("Emission")
#plt.show()

# Create the training and test datasets
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# simple regression model
#plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
#plt.xlabel("Engine size (training)")
#plt.ylabel("Emission")
#plt.show()

# model the data with sklearn
print("\nSimple linear regression model")
print("\nTraining with ENGINESIZE")
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

# plot the fit line over the data
#plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
#plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
#plt.xlabel("Engine size")
#plt.ylabel("Emission")
#plt.show()

# evaluate the model
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )

# lets do the training model with FUELCONSUMPTION_COMB
print("\nTraining with FUELCONSUMPTION_COMB")
train_x = np.asanyarray(train[['FUELCONSUMPTION_COMB']])
test_x = np.asanyarray(test[['FUELCONSUMPTION_COMB']])
regr.fit(train_x, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ', regr.intercept_)
test_y_ = regr.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_))

