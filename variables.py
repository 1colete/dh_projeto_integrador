# SECTION HOMEPAGE

import pandas as pd
df = pd.read_pickle('dados/cleaned/df_preped.pkl')


home_page_text = """
<div style="text-align: justify"> 

A Covid-19 é uma doença infecciosa causada pelo coronavírus (Sars-CoV-2) e tem como principais sintomas febre, cansaço e tosse seca. Alguns pacientes podem apresentar dores, congestão nasal, dor de cabeça, conjuntivite, dor de garganta, diarreia, perda de paladar ou olfato, erupção cutânea na pele ou descoloração dos dedos das mãos ou dos pés. Esses sintomas geralmente são leves e começam gradualmente. Algumas pessoas são infectadas, mas apresentam apenas sintomas muito leves.

A maioria das pessoas (cerca de 80%) se recupera da doença sem precisar de tratamento hospitalar. Uma em cada seis pessoas infectadas por Covid-19 fica gravemente doente e desenvolve dificuldade de respirar. As pessoas idosas e as que têm outras condições de saúde como pressão alta, problemas cardíacos e do pulmão, diabetes ou câncer, têm maior risco de ficarem gravemente doentes. No entanto, qualquer pessoa pode pegar a Covid-19 e ficar gravemente doente.

O SARS-CoV-2 é um betacoronavírus descoberto em amostras de lavado broncoalveolar obtidas de pacientes com pneumonia de causa desconhecida na cidade de Wuhan, província de Hubei, China, em dezembro de 2019. Pertence ao subgênero Sarbecovírus da família Coronaviridae e é o sétimo coronavírus conhecido a infectar seres humanos.

Os coronavírus são uma grande família de vírus comuns em muitas espécies diferentes de animais, incluindo o homem, camelos, gado, gatos e morcegos. Raramente os coronavírus de animais podem infectar pessoas e depois se espalhar entre seres humanos como já ocorreu com o MERS-CoV e o SARS-CoV-2. Até o momento, não foi definido o reservatório silvestre do SARS-CoV-2.

Fonte: https://www.saude.df.gov.br/coronavirus/
</div>

"""


#  SECTION DATA

data_description = """
<div style = "text-align: justify">O conjunto de dados consiste em algumas condições de saúde preexistentes para determiar o risco de óbito por COVID-19. As variáveis analisadas incluem idade, sexo, cardiopatia, diabetes, doencas neurologicas, obesidade, e outros fatores de risco.

Fonte dos dados de contaminação por COVID-19 https://www.seade.gov.br/coronavirus/
</div>
<br>
"""

age_min_value = int(df['idade'].min())
age_max_value = int(df['idade'].max())

# SECTION ABOUT
about_text = """
<div style="text-align: justify">Diabetes mellitus, commonly known as diabetes, is a group of metabolic disorders characterized by a high blood sugar level over a prolonged period of time.Symptoms often include frequent   urination, increased thirst and increased appetite. If left untreated, diabetes can cause many health complications. Acute complications can include diabetic ketoacidosis, hyperosmolar hyperglycemic state, or death. Serious long-term complications include cardiovascular disease, stroke, chronic kidney disease, foot ulcers, damage to the nerves, damage to the eyes and cognitive impairment (from Wikipedia).    


Thus, the purpose of this application is to predict whether or not the patient has diabetes. For didactic purposes we use only the SVM model.</div>
"""