# SECTION HOMEPAGE

import pandas as pd
df = pd.read_pickle('dados/cleaned/df_preped.pkl')

home_page_text = """
<div style="text-align: justify"> Diabetes is due to either the pancreas not producing enough insulin, or the cells of the body not responding properly to the insulin produced. There are three main types of diabetes mellitus.
Type 1 diabetes results from failure of the pancreas to produce enough insulin due to loss of beta cells. This form was previously referred to as "insulin-dependent diabetes mellitus" or "juvenile diabetes". The loss of beta cells is caused by an autoimmune response. The cause of this autoimmune response is unknown.
Type 2 diabetes begins with insulin resistance, a condition in which cells fail to respond to insulin properly. As the disease progresses, a lack of insulin may also develop. This form was previously referred to as "non insulin-dependent diabetes mellitus" or "adult-onset diabetes". The most common cause is a combination of excessive body weight and insufficient exercise.
Gestational diabetes is the third main form, and occurs when pregnant women without a previous history of diabetes develop high blood sugar levels (text FROM WIKIPEDIA).
The aim of this Data App is to predict whether or not the patient has diabetes.</div>

"""
#  SECTION DATA

data_description = """
<div style = "text-align: justify">O conjunto de dados consiste em algumas condições de saúde preexistentes para determiar o risco de óbito por COVID-19. As variáveis analisadas incluem idade, sexo, cardiopatia, diabetes, doencas neurologicas, obesidade, e outros fatores de risco .</div>
<br>
"""


age_min_value = int(df['idade'].min())
age_max_value = int(df['idade'].max())

# SECTION ABOUT
about_text = """
<div style="text-align: justify">Diabetes mellitus, commonly known as diabetes, is a group of metabolic disorders characterized by a high blood sugar level over a prolonged period of time.Symptoms often include frequent   urination, increased thirst and increased appetite. If left untreated, diabetes can cause many health complications. Acute complications can include diabetic ketoacidosis, hyperosmolar hyperglycemic state, or death. Serious long-term complications include cardiovascular disease, stroke, chronic kidney disease, foot ulcers, damage to the nerves, damage to the eyes and cognitive impairment (from Wikipedia).    


Thus, the purpose of this application is to predict whether or not the patient has diabetes. For didactic purposes we use only the SVM model.</div>
"""