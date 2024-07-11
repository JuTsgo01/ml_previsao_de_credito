# Previsão de Crédito

Este projeto utiliza técnicas de aprendizado de máquina para prever o score de crédito de clientes com base em um conjunto de dados pré-existente. Ele foi desenvolvido usando a biblioteca scikit-learn e demonstra o processo completo de importação, treinamento e teste de modelos de machine learning.

Este projeto foi seguido com a escola de treinamento  "Hashtag Treinamento".

## Estrutura do Projeto
* previsao_credito.py: Script principal que contém todo o código para ler os dados, treinar os modelos e fazer previsões.

## Funcionalidades

### Importação e Preparação dos Dados:

* Leitura de um arquivo CSV contendo informações dos clientes.
* Tratamento de dados categóricos utilizando LabelEncoder.
* Separação dos dados em conjuntos de treino e teste.

### Treinamento de Modelos:

* Criação e treinamento de dois modelos de machine learning: K-Nearest Neighbors (KNN) e Random Forest.
* Avaliação da acurácia dos modelos.

### Previsão para Novos Clientes:

* Leitura de um arquivo CSV contendo informações de novos clientes.
* Aplicação do modelo treinado para prever o score de crédito dos novos clientes.
* Requisitos
  * Python 3.7+
  * Bibliotecas:
  * pandas
  * numpy
  * scikit-learn
  * matplotlib
    
