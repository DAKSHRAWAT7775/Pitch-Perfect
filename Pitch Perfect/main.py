#import the libraries

import math
import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
from joblib import load

#SET PAGE WIDE
st.set_page_config(page_title='ODI Win Predictor',layout="centered")




column_transformer = load('column_transformer.joblib')
label_encoder=load('label_encoder.joblib')
#Get the ML model 
model = pickle.load(open(r"ml_model.pkl",'rb'))

#Title of the page with CSS

st.markdown("<h1 style='text-align: center; color: white;'> ODI Win Predictor </h1>", unsafe_allow_html=True)

#Add background image

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://4.bp.blogspot.com/-F6aZF5PMwBQ/Wrj5h204qxI/AAAAAAAABao/4QLn48RP3x0P8Ry0CcktxilJqRfv1IfcACLcBGAs/s1600/GURU%2BEDITZ%2Bbackground.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

#Add description

with st.expander("Description"):
    st.info("""A Simple ML Model to predict win percetage for the team batting first after the first innings is done.
    
 """)

# SELECT THE BATTING TEAM


bat_team= st.selectbox('Select the Batting Team ',('India', 'Afghanistan', 'Australia','Pakistan','Bangladesh','England'))

  # Batting Team





#SELECT BOWLING TEAM

bowl_team = st.selectbox('Select the Bowling Team ',('India', 'Afghanistan', 'Australia','Pakistan','Bangladesh','England'))
if bowl_team==bat_team:
    st.error('Bowling and Batting teams should be different')


col1, col2 = st.columns(2)

#Enter the Current Ongoing Over
with col1:
    overs = st.number_input('Enter total Overs played',min_value=0.1,max_value=50.0,value=50.0,step=0.1)
    if overs-math.floor(overs)>0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')
with col2:
#Enter Current Run
    runs = st.number_input('Enter Total Runs scored',min_value=0,max_value=1800,step=1,format='%i')


#Wickets Taken till now
wickets =st.slider('Enter Wickets fallen till now',0,10)
wickets=int(wickets)

col3, col4 = st.columns(2)

def predict_win_probability_svc(runs, wickets, overs, bat_team, bowl_team):
    # Encode categorical features
    bat_team_encoded = label_encoder.transform([bat_team])[0]
    bowl_team_encoded = label_encoder.transform([bowl_team])[0]

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Runs': [runs],
        'Wickets': [wickets],
        'Overs': [overs],
        'bat_team': [bat_team_encoded],
        'bowl_team': [bowl_team_encoded]
    })

    # Use one-hot encoding for categorical features
    input_data_encoded = column_transformer.transform(input_data)

    # Make predictions
    win_probability = model.predict_proba(input_data_encoded)[:, 1][0]

    return win_probability
    
if st.button('Predict Score'):
    #Call the ML Model
    win_percentage_svc = predict_win_probability_svc(runs, wickets, overs, bat_team, bowl_team)
    
    #Display the predicted Score Range
    x=f'PREDICTED WIN% FOR {bat_team} : {win_percentage_svc*100:.2f}%' 
    st.success(x)

