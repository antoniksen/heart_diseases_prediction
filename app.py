import streamlit as st
import pickle

def load():
    with open('model.pcl', 'rb') as fid:
        return pickle.load(fid)
    

age = st.slider('Age days', 8000, 24000, key='age')
hight = st.slider('Hight in cm', 140, 220, key='hight')
weight = st.slider('Weight in kg', 10, 183, key='weight')
ap_hi = st.slider('Hi pressure', 120, 240, key='ap_hi')
ap_lo = st.slider('Low pressure', 40, 208, key='ap_lo')
gender = st.radio('Choose your gender', options=('1', '2'), key='gender')
gluc = st.radio('Glucose level', options=('1', '2', '3'), key='gluc')
cholesterol = st.radio('Cholisterol level', options=('1', '2', '3'), key='cholesterol')
smoke = st.radio('Do you smoke?', options=(0, 1), key='smoke')
alco = st.radio('Are you alchohol dependant?', options=(0, 1), key='alco')
active = st.radio('Are you physically active?', options=(0, 1), key='active')

model = load()

y_pr = model.predict_proba([[age, hight, weight, ap_hi, ap_lo, gender, gluc, cholesterol, smoke, alco, active]])[:,1]

st.write(y_pr)

