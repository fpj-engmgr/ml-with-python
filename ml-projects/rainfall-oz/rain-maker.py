# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import jaccard_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
from sklearn.metrics import confusion_matrix, accuracy_score
import sklearn.metrics as metrics

WDOFILE = '/Users/fpj/Development/python/ml-projects/rainfall-oz/data/weatherOZ.csv'
# Load the data
df = pd.read_csv(WDOFILE)
print("Dataframe shape: ", df.shape)
print("Dataframe columns: \n", df.columns)
print("Dataframe head: \n", df.head(5))
