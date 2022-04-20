# Typecassting
Q1.
import pandas as pd
import numpy as np
data1=pd.read_csv('F:/Assignments/Assignment 4 data pre processing/DataSets/OnlineRetail.csv',encoding='unicode__escape')
data1.head()
data1.head(10)
data1.dtypes
data1['UnitPrice']=data1['UnitPrice'].astype('int64') #here float gets converted to int64
data1['UnitPrice'].dtypes

from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan, strategy='mean')
data1['CustomerID']=pd.DataFrame(mean_imputer.fit_transform(data1[['CustomerID']]))
data1['CustomerID'].isnull().sum()   #here nan in customerid is replaced by mean of the customerid
data1['CustomerID']=data1['CustomerID'].astype('int64')
data1['CustomerID'].dtypes

# Duplication
Q2.
duplicate=data1.duplicated()
sum(duplicate)
data2=data1.drop_duplicates()

Q3.
import matplotlib.pyplot as plt
import numpy as np
plt.hist(data1.Quantity);plt.show()
plt.boxplot(data1.Quantity);plt.show()
plt.hist(data1.UnitPrice);plt.show()
plt.boxplot(data1.UnitPrice);plt.show()
plt.hist(data1.CustomerID);plt.show()
plt.boxplot(data1.CustomerID);plt.show()
























