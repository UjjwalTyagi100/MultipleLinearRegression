# Multiple Linear Regression:-

'''
      Importing the libraries

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
      Importing the dataset

'''

dataset = pd.read_csv(r"C:\Users\ujjwa\Documents\50_Startups.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

'''
      Encoding categorical data

'''

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder' , OneHotEncoder() , [-1])] , remainder = 'passthrough') 
x = np.array(ct.fit_transform(x))

'''
      Splitting the dataset into the Training set and Test set

'''

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.2 , random_state = 0)

'''
      Training the Multiple Linear Regression model on the Training set

'''

from sklearn.linear_model import LinearRegression
regressor = LinearRegression() # Will built our Linear regression model
regressor.fit(x_train , y_train) # Will train our Linear regression model

'''
      Predicting the Test set results

'''

y_predict = regressor.predict(x_test)
np.set_printoptions(precision = 2) 

print(np.concatenate((y_predict.reshape(len(y_predict) , 1) , y_test.reshape(len(y_test) , 1)) , 1))