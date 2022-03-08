from soupsieve import select
import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np
#import sqlite3
#from monitor_for_app import *
from variables import *
#from datetime import datetime
st.set_page_config(page_title = 'COVID-19 Prediction')

@st.cache
def load_data():
    df = pd.read_pickle('dados/cleaned/df_preped.pkl')
    return df

def load_model(model):
	load_model = joblib.load(open(os.path.join(model),"rb"))
	return load_model

# load data
df = load_data()

def main():
    options = ['Homepage', 'Data' ,'Make Prediction','About']
    page_option = st.sidebar.selectbox('Options', options)
    
    if page_option == 'Homepage':
        st.title('COVID-19 predictor')
        st.markdown(home_page_text, unsafe_allow_html = True)
        
    elif page_option == 'Data':
        st.title('More informations about dataset')
        st.markdown(data_description, unsafe_allow_html = True)

        with st.expander('Descriptive statistics', expanded = False):
            st.write('Here you can get some statistics for all numeric columns.')
            st.write(df.describe())

        with st.expander('Target values'):
            st.write('We have 35% class 1 observations.')
            # st.write(round(df.Outcome.value_counts(normalize = True)*100, 2))
        
    elif page_option == 'Make Prediction':
        st.title('Prediction')
        
        cardiopatia = st.checkbox('cardiopatia')
        diabetes = st.checkbox('diabetes')
        doenca_neurologica = st.checkbox('Doenças neurológicas')
        obesidade = st.checkbox('obesidade')
        outros_fatores_de_risco = st.checkbox('outros_fatores_de_risco')
        idade = st.slider('Idade: ', 0, 110, 29)
        cs_sexo = st.selectbox( 'Sexo', 
                ('Masculino', 'Feminino'))
        if cs_sexo == 'Masculino':
            cs_sexo = 1
        else:
            cs_sexo = 0 

        selected_options = [cardiopatia,diabetes, doenca_neurologica, obesidade, outros_fatores_de_risco , idade , cs_sexo]
        
        selected_options2 = []
        for option in selected_options2:
            if option == True:
                selected_options2.append(1)
            if option == False:
                selected_options2.append(0)
            else:
                selected_options2.append(option)

        sample_input = np.array(selected_options).reshape(1,-1)
        model = load_model('models/DecisionTreeClassifier.pkl')

        # class prediction
        prediction_class = model.predict(sample_input)
        if prediction_class == 1:
            prediction_class = 'Obito'
        else:
            prediction_class = 'Sobrevive'

        # proba prediction
        prediction_proba = model.predict_proba(sample_input)
        if st.button('Submit'):
            st.success(f'Cardiopatia: {cardiopatia}')
            st.success(f'Diabetes: {diabetes}')
            st.success(f'Doenças neurológicas: {doenca_neurologica}')
            st.success(f'Obesidade: {obesidade}')
            st.success(f'Outros fatores de Risco: {outros_fatores_de_risco}')
            st.success(f'Idade: {idade}')
            st.success(f'Sexo: {cs_sexo}')
            st.text(' ')
            st.success(f"Classe da previsão é: {prediction_class}")
            st.success(f"Probabilidade de óbito é de {round(prediction_proba[0,1]*100, 2)}%.")
               
    else:
        st.title('About')
        
        st.text('Projeto desenvolvido por:')
    
        st.text('''
        Alexandre Antunes
        Alexandre Colete
        Antonio Davi Ramos
        Emerson Araujo
        Eduardo Hagiwara
        Vinicio Lima Pedrosa Lins''')
        
    
main()

