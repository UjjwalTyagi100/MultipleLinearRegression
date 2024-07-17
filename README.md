# Multiple Linear Regression

This repository contains a Python implementation of Multiple Linear Regression using the 50_Startups.csv dataset. The goal is to predict the profit of a startup based on various features such as R&D Spend, Administration, Marketing Spend, and the State in which the startup operates.

## Project Overview
The project follows these key steps:

## Importing Libraries:
Essential libraries for data manipulation, numerical operations, and visualization.
## Loading the Dataset:
Reading the dataset from a CSV file.
## Encoding Categorical Data:
Transforming categorical data into a numerical format using OneHotEncoder.
## Splitting the Dataset:
Dividing the data into training and test sets.
## Training the Model: 
Building and training the Multiple Linear Regression model on the training set.
## Making Predictions:
Using the trained model to predict the results for the test set and displaying them.

## Dataset
The dataset used in this project is 50_Startups.csv, which includes the following columns:
-> R&D Spend
-> Administration
-> Marketing Spend
-> State
-> Profit

## Requirements
-> pandas
-> numpy
-> matplotlib
-> scikit-learn

## Results
The script will output the predicted profits alongside the actual profits for the test set, allowing you to compare the model's performance.

## Conclusion
This project demonstrates how to implement Multiple Linear Regression using Python and scikit-learn. It covers data preprocessing, model training, and prediction, providing a comprehensive example of how to work with real-world data.