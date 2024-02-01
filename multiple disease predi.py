# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:11:58 2023

@author: Suruchi
"""

import pickle

import streamlit as st
from streamlit_option_menu import option_menu
import account


class MultiApp:
    
    def _init_(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
            })
     
   


#loading the saved models
diabetes_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/diabetes_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/heart_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Suruchi/Desktop/Multiple disease prediction system/saved models/parkinsons_model.sav','rb'))



#sidebar with navigate
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Account','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                                 
                           icons=['person-fill','clipboard2-pulse','heart-pulse-fill','person-circle'],
                           menu_icon='hospital-fill',
                                 
                           default_index = 0,
                           styles={
                               "container": {"padding": "5!important", "background-color":"lightyellow"},
                               "icon": {"color": "black", "font-size": "23px"},
                               "nav-link": {"color": "blue", "font-size": "20px", "text-align": "left","margin": "0px"},
                               "nav-link-selected": {"background-color": "#02ab21"},
                               } )
     
    
             
#Account
if (selected == 'Account'):
    account.app()
   
      
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
        
    #page title
    st.title(':blue[Diabetes Prediction using ML]')
        
    #getting the input data from the user
    #clumns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin value')
        
    with col3:
        BMI = st.text_input('BMI value')  
         
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
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
    
        
    #getting the input data from the user
    #clumns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Cerebral Palsy')
        
    with col1:
        trestbps = st.text_input('Trestbps value')
        
    with col2:
        chol = st.text_input('Cholestrol value')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar value')  
         
    with col1:
        restecg = st.text_input(' Resting electrocardiographic measurement')
        
    with col2:
        thalach = st.text_input('The maximum heart rate achieved by a person')
        
    with col3:
        exang = st.text_input('Exercise induced angina value')  
         
    with col1:
        oldpeak = st.text_input('Oldpeak value')  
     
    with col2:
        slope = st.text_input(' ST/heart rate slope value')  
         
    with col3:
        ca = st.text_input('Coronary artery value')  
            
    with col1:
        thal = st.text_input('Thalassemia value')
           
        
        
    
    
    #code for prediction
    heart_diagnosis = ''

    #creating a button for prediction
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The Person is having a heart disease'
        else:
            heart_diagnosis = 'The Person is not having a heart disease'
    st.success(heart_diagnosis)        
    
            
            
if (selected == 'Parkinsons Disease Prediction'):
                
    #page title
    st.title('Parkinsons Disease Prediction using ML')
    
        
        
      
            
        
        
           
        