# -*- coding: utf-8 -*-
"""previsao_credito.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JEpt86_E11wdxeqOPVsCB83-Y9fhK3U9
"""

!pip install scikit-learn

"""## Sempre 3 etapas para criar uma IA
### 1 - Importar a IA
### 2 - Criar a IA
### 3 - Treinar

### 1 - Importando as blib (Importando a IA)
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder #Serve para tranfromarmos feature
from sklearn.model_selection import train_test_split #Usado para separar o x e y de treino do x e y de teste
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

"""### Lendo com pandas a base de dados dos clientes que será usado para treino e teste"""

clientes = pd.read_csv('/content/drive/MyDrive/python IA/clientes.csv') #lendo a tabela CSV
clientes.isnull().sum() #Não há números nulos

clientes.info()

"""### Fazendo o encoding na base de clientes que usaremos para treino e teste nas colunas 'profissao', 'mix_credito', 'comportamento_pagamento'"""

feature_categorica = ['profissao', 'mix_credito', 'comportamento_pagamento']
codificador = LabelEncoder()

for feature in feature_categorica:
  clientes[feature] = codificador.fit_transform(clientes[feature])

features = clientes.drop(columns=['id_cliente', 'score_credito']) #fetures usada para prever
target = clientes['score_credito'] #alvo que queremos como resposta/prever

x = features
y = target

#Criando nossas variaveis de treino e teste, além de setar 30% para teste e 70% para treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

"""### 2 e 3 - Criando e Treinando as IA's com as variaveis de treino (70%)"""

#Treinando nosso modelo com KNN
modelo_KNN = KNeighborsClassifier()
modelo_KNN.fit(x_treino, y_treino)

#Treinando nosso modelo com Arvore de descisão
modelo_arvore_de_descisao = RandomForestClassifier()
modelo_arvore_de_descisao.fit(x_treino, y_treino)

"""### Fazendo a previsão nas variaveis de teste"""

previsao_knn = modelo_KNN.predict(x_teste)
previsao_arvore_de_descisao = modelo_arvore_de_descisao.predict(x_teste)

display(accuracy_score(y_teste, previsao_knn)) # Acuracia de 73%
display(accuracy_score(y_teste, previsao_arvore_de_descisao)) # Acuracia de 82%

"""### Lendo com pandas a base de dados dos novos clientes que será usado para fazer a previsão, aplicando nosso modelo que foi treinado e testado (82% de acuracia - Árvore de descisçoes)"""

novos_clientes = pd.read_csv('/content/drive/MyDrive/python IA/novos_clientes.csv')
display(novos_clientes)

"""### Aplicando encoding (feture categorica em numérica) nas colunas 'profissao', 'mix_credito', 'comportamento_pagamento'"""

feature_categorica_novos_clientes = ['profissao', 'mix_credito', 'comportamento_pagamento']
codificador = LabelEncoder()

for feature in feature_categorica:
  novos_clientes[feature] = codificador.fit_transform(novos_clientes[feature])

"""### Fazendo as previsões nos novos clientes cadastrados"""

previsao_arvore_de_descisao = modelo_arvore_de_descisao.predict(novos_clientes)
display(previsao_arvore_de_descisao)