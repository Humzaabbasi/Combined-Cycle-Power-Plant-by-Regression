#REGRESSion

#import
import pandas as pd
#import data set
df=pd.read_excel("C:\\Users\\DELL\\Desktop\\Introduction to Data Science\\Regression\\Folds5x2_pp.xlsx")
print (df)
x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


# Spliting Dataset Into Training Set And Test Set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=(0))

#Fitting Gradient Boosting To The Training Set
from sklearn.ensemble import GradientBoostingRegressor
regressor = GradientBoostingRegressor()
regressor.fit(x_train, y_train)

# Predicting The Test Set Result
y_pred = regressor.predict(x_test)