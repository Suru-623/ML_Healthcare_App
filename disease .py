# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:11:58 2023

@author: Suruchi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

def app():


#loading the saved models
diabetes_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/heart_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/parkinsons_model.sav','rb'))


#sidebar with navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinsons Disease Prediction'],
                            
                            icons=['clipboard2-pulse','heart-pulse-fill','person-circle'],
                            
                            default_index = 0)
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
    #page title
    st.title('Diabetes Prediction using ML')
        
        
        
    Pregnancies = st.text_input('Number of Pregnancies')
        
    Glucose = st.text_input('Glucose Level')
        
    BloodPressure = st.text_input('Blood Pressure value')
        
    SkinThickness = st.text_input('Skin Thickness value')
        
    Insulin = st.text_input('Insulin value')
        
    BMI = st.text_input('BMI value')
        
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    Age = st.text_input('Age of the Person')
    

    #code for prediction
    diab_diagnosis = ''

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'
    st.success(diab_diagnosis)        
    
    
if (selected == 'Heart Disease Prediction'):
            
    #page title
    st.title('Heart Disease Prediction using ML')
            
            
if (selected == 'Parkinsons Disease Prediction'):
                
    #page title
    st.title('Parkinsons Disease Prediction using ML')
        