import streamlit as st
import pickle 
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
model = pickle.load(open("mobileprice.pkl","rb"))
dt= pickle.load(open("labeldictionary.pkl","rb"))
st.title("Smart Phone Prediction")
brandname=st.selectbox("Choose your brand",dt["Brand"])
brandindex=dt['Brand'].tolist().index(brandname)
modelname=st.selectbox("Choose your Model",dt["Model"])
modelindex=dt['Model'].tolist().index(modelname)
year= st.number_input("Select year",min_value=2015,max_value=2025,step =1)
original_price=st.number_input("Enter original price",min_value=10000,max_value=200000,step=1000)
month =st.number_input("Enter Original Price",min_value=10000,max_value=200000,step =1000)
storage = st.selectbox("Select Storage",[64,128,256,512])
ram=st.selectbox("Select RAM Size", [4,6,8,12,16,18])
ram =int(ram)
battery = st.number_input("Enter Battery health", min_value=0.0,max_value=100.0,step =0.1)
condition =st.selectbox("Select Condition",dt["Condition"]) 

conditionnumber = dt["Condition"].tolist().index(condition)
Warranty = st.selectbox("Phone is still in Warranty",dt["Warranty"])
Warrantynumber= dt['Warranty'].tolist().index(Warranty)
Color = st.selectbox("Select Condition",dt["Color"])
colornumber =dt["Color"].tolist().index(Color)
if st.button("predict"):
    data=[[brandindex,modelindex,year,original_price,month,storage,ram,battery,conditionnumber,
    Warrantynumber,colornumber]]
    print(data)
    res=model.predict(data)[0]
    st.write("Resale value of a phone=",round(res,2))
    

 