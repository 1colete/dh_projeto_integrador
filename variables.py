# SECTION HOMEPAGE

import pandas as pd
df = pd.read_pickle('dados/cleaned/df_preped.pkl')


home_page_text = """
<div style="text-align: justify"> 

## Objetivo:
Este aplicativo tem o objetivo de ajudar na triagem de pacientes com COVID-19, baseado no histórico médico é capaz de reconhecer casos possívelmente graves e ajudar no processo de decisão de internação.

## Sintomas
A Covid-19 é uma doença infecciosa causada pelo coronavírus (Sars-CoV-2) e tem como principais sintomas:
- Febre
- Cansaço
- Tosse seca. 

Alguns pacientes podem apresentar 
- Dores
- Congestão nasal
- Dor de cabeça
- Conjuntivite
- Dor de garganta
- Diarreia
- Perda de paladar ou olfato
- Erupção cutânea na pele ou descoloração dos dedos das mãos ou dos pés. 
  
Esses sintomas geralmente são leves e começam gradualmente. Algumas pessoas são infectadas, mas apresentam apenas sintomas muito leves ou nao apresentam sintomas.

## Obs:
A maioria das pessoas (cerca de 80%) se recupera da doença sem precisar de tratamento hospitalar. Uma em cada seis pessoas infectadas por Covid-19 fica gravemente doente e desenvolve dificuldade de respirar. As pessoas idosas e as que têm outras condições de saúde como pressão alta, problemas cardíacos e do pulmão, diabetes ou câncer, têm maior risco de ficarem gravemente doentes. No entanto, qualquer pessoa pode pegar a Covid-19 e ficar gravemente doente.

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
<div style="text-align: justify">

## Projeto desenvolvido por:
- Alexandre Antunes
- Alexandre Colete Silva
- Emerson Araujo
- Eduardo Hagiwara
- Vinicio Lima Pedrosa Lins

## Proposta e Metodologia:
A proposta desse aplicativo é prever casos graves de COVID-19 usando como base informações de idade, sexo e comorbidades pré-existentes. Foi utilizado um modelo de arvore de decisão com seus hiper parâmetros otimizados.


## Fontes:
- https://www.saude.df.gov.br/coronavirus/
- https://cidades.ibge.gov.br/brasil/sp/panorama
- https://github.com/ipeaGIT/geobr
- https://ipeagit.github.io/geobr/articles/python-intro/py-intro-to-geobr.html
- https://basedosdados.org/dataset/br-ibge-populacao
- https://www.kaggle.com/rubensmau/covid-19-deaths-per-capita
- https://towardsdatascience.com/analysis-of-covid-19-using-per-capita-data-f8f9a31a2c4d



</div>
"""