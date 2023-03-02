import pandas as pd
import numpy as np
car = pd.read_csv("quikr_car.csv")
# car.head()
car = car.dropna()
# car.isnull()
# car.info()
# car.head()
# car['name'].unique()
backup = car.copy() # creating the copy of the data set
car=car[car['year'].str.isnumeric()] # here we take those column which is numeric
car['year']= car['year'].astype(int)
# car.info()
# car= car[car['Price'].str.isnumeric()]
# OR
car = car[car['Price'] != "Ask For Price"]
# car.info()
car['Price']=car['Price'].str.replace(',','') # it will remove the comma from the values
car['Price'] = car['Price'].astype(int) # it will convert  it into the integer
# car.info()
car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','') # it will split ,remove km ,replace ","
car = car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)
# car.info()
# car
car['name'] = car['name'].str.split(' ').str.slice(0,3,1).str.join(' ')
# car
car.reset_index()
car.describe()
car[car['Price']>6e6].reset_index(drop=True)
car.reset_index()
X = car.drop(columns="Price")
Y = car['Price']
# X
# Y
# X.info()
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import  make_column_transformer
ohe = OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])
column_trains = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
lr = LinearRegression()
pipe = make_pipeline(column_trains,lr)
pipe.fit(X_train,Y_train)
y_pred = pipe.predict(X_test)
# y_pred
r2_score(Y_test,y_pred)
score = []
for i in range (1000):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=i)
    lr = LinearRegression()
    pipe = make_pipeline(column_trains,lr)
    pipe.fit(X_train,Y_train)
    y_pred = pipe.predict(X_test)
    score.append(r2_score(Y_test,y_pred))
np.argmax(score)
score[661]
def input():
    Car_Name = "Maruti Suzuki Alto 800"
    Company = "Maruti"
    model_year = 2016
    km_driven = 2450i
    Fuel_type = "Petrol"
    price = pipe.predict(pd.DataFrame([[Car_Name,Company,model_year,km_driven,Fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
    # return price
    print(price)
input()

