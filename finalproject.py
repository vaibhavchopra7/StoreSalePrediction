#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd       #pandas library for data
import matplotlib.pyplot as plt   #matlpotlib library for visualization (but not used here (see LLD document))
import numpy as np     # numpy library for manipulation           
datatrain=pd.read_csv(r"C:\Users\welcome\Desktop\Train.csv")   #datasets..
datatest=pd.read_csv(r"C:\Users\welcome\Desktop\Test.csv")
datatest_filled=pd.read_excel(r"C:\Users\welcome\Desktop\dummy_test.xlsx")
op=datatest.iloc[:,[0,6,4,5,10,1,2,7]].values    #op dataset used for evaluate results wrt given input
x1=datatrain.iloc[:,[4,5,10]].values          # training dataset independent variables
y1=datatrain.iloc[:,-1].values                # training dataset dependent variable
x2=datatest.iloc[:,[4,5,10]].values           # testing dataset 

from sklearn.preprocessing import LabelEncoder     #data preprocessing
b=LabelEncoder()                                    #label encorder encode the strings into lables(num)
x1[:,0]=b.fit_transform([i for i in x1[:,0]])
x2[:,0]=b.transform([i for i in x2[:,0]])
c=LabelEncoder()
x1[:,-1]=c.fit_transform([i for i in x1[:,-1]])
x2[:,-1]=c.fit_transform([i for i in x2[:,-1]])


from sklearn.linear_model import LinearRegression              #Algorithm part
from sklearn.preprocessing import PolynomialFeatures
re=PolynomialFeatures(degree=7) 
Repoly=LinearRegression().fit(re.fit_transform(x1),y1)
while(True):
        print("ENTER Id's (Item_identifier & Outlet_identifier) here ",end=" ")
        a=list(map(str,input().split('   ')))   #input
        for i in op:
            if (i[0]==a[0] and i[1]==a[1]):     # true if both id's matchs
                print("detailes:- ",i[2],",","Rs."+str(i[3]),",",i[4],",",str(i[5])+"g/Kg.",",",i[6],",",i[7])
                print("Predicted Sale Rs."+str(round(Repoly.predict(re.transform([[b.transform([i[2]])[0],i[3],c.transform([i[4]])[0]]]))[0])),"\n\n\n")  #predicted part
                break


#     datatest["Predicted_item_outlet_sale"]=Repoly.predict(re.transform(x2))   # prediction of test dataset goes to PredictedTest.csv file
#     datatest.to_csv("PredictedTest.csv",index=False)   

