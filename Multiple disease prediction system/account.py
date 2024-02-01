# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:23:52 2024

@author: Suruchi
"""

import streamlit as st

def app():
    st.title('Welcome to :red[AI healthcare]👩‍⚕️')
    
    choice = st.selectbox('Login/Signup', ['Login','Sign Up'])
    if choice=='Login':
        
        email=st.text_input('Email Address')
        password=st.text_input('Password', type='password')
        
        st.button('Login')
    
    else:
        email=st.text_input('Email Address')
        password=st.text_input('Password', type='password')
        username=st.text_input('Enter your uique username')
        
        st.button('Create my account')