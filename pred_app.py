# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:58:09 2022

@author: user
"""

import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

loaded_model=pickle.load(open('fuel.sav', 'rb'))
def fuel_predict(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return prediction
   
def main():
    st.title('fuel predection on web app')
   					
    shaftSpeed=st.text_input('enter shaft speed')
        
    
    
    TWS  =st.text_input('enter  TWS')
            
   
            
    temp=st.text_input('entertemp')
            
    meanDraft=st.text_input('enter meanDraft')
    
    
    if st.button("fuel predection"):
        pred =fuel_predict([shaftSpeed,	TWS	,	temp,	meanDraft])
        st.write(pred)
        
if __name__=='__main__':
    main()
