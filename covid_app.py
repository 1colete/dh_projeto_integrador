from soupsieve import select
import streamlit as st
# import joblib
import pickle
import pandas as pd
import numpy as np
#import sqlite3
#from monitor_for_app import *
# from variables import *
#from datetime import datetime
st.set_page_config(page_title = 'Previsor de COVID-19')

@st.cache
def load_data():
    df = pd.read_pickle('dados/cleaned/df_preped.pkl')
    return df

def load_model(model):
	# load_model = joblib.load(open(os.path.join(model),"rb"))
    load_model = pickle.load(open(f'models/clf_tuned.pkl', 'rb'))
    return load_model

# load data
# df = load_data()

def main():
    options = ['Início', 'Dados' ,'Predição','Sobre']
    page_option = st.sidebar.selectbox('Páginas', options)
    
    if page_option == 'Início':
        st.title('Previsor COVID-19 ')
        # st.markdown(home_page_text, unsafe_allow_html = True)
        
    elif page_option == 'Dados':
        st.title('Mais informações sobre o conjunto de dados')
        # st.markdown(data_description, unsafe_allow_html = True)

        # with st.expander('Estatisticas', expanded = False):
        #     st.write('Podemos ver estatisticas para as colunas numéricas.')
        #     st.write(df.describe())

        # with st.expander('Valores Targets'):
        #     st.write(f'Temos {round(df.obito.value_counts(normalize = True)*100, 2)[1]} % de obtidos na base.')
        #     st.write(round(df.obito.value_counts(normalize = True)*100, 2))

    elif page_option == 'Predição':
        st.title('Predição')
        
        cardiopatia = st.checkbox('cardiopatia')
        diabetes = st.checkbox('diabetes')
        doenca_neurologica = st.checkbox('Doenças neurológicas')
        obesidade = st.checkbox('obesidade')
        outros_fatores_de_risco = st.checkbox('outros_fatores_de_risco')
        idade = st.slider('Idade: ', 0, 110, 29)
        cs_sexo = st.selectbox( 'Sexo', 
                ('Masculino', 'Feminino'))
        if cs_sexo == 'Masculino':
            cs_sexo = True
        else:
            cs_sexo = False

        selected_options = [cardiopatia, diabetes, doenca_neurologica, obesidade, outros_fatores_de_risco , idade , cs_sexo]

        sample_input = np.array(selected_options).reshape(1,-1)
        model = load_model('models/clf_tuned.pkl')

        if st.button('Submit'):
            # class prediction
            prediction_class = model.predict(sample_input)
            if prediction_class == 1:
                prediction_class = 'ALTO RISCO'
            else:
                prediction_class = 'BAIXO RISCO'

            st.success(f"Paciente com {prediction_class} de obito")
               
    else:
        st.title('Sobre')
        # st.markdown(about_text, unsafe_allow_html = True)
        
    
main()

