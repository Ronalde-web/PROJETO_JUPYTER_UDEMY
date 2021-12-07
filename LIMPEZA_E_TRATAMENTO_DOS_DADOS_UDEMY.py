#!/usr/bin/env python
# coding: utf-8

# ciêntista de dados: RONALDE GONÇALVES
# limpeza e tratamento de dados.

# In[1]:


import pandas as pd
import seaborn as srn
import statistics as sts


# In[3]:


# IMPORTAR DADOS
dataset = pd.read_csv('C:/Users/Ronalde/DADOS-DO- CURSO-UDEMY/FormaçãoCD2/10.Prática em Python/dados/Churn.csv', sep=";")
# VISUALIZAR
dataset.head()


# In[33]:


dataset.shape


# In[5]:


# COLOCANDO NOMES NAS COLUNAS
dataset.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'temCartCredito',
                   'Ativo', 'Salario', 'Saiu']


# In[6]:


# VISUALIZAR A MUDANÇA
dataset.head()


# In[18]:


# FILTRO SÓ PARA O ESTADO SC.
filtro = dataset['Estado'] == 'SC'
paraiba = dataset[filtro]
paraiba


# In[14]:


# EXPLORAR DADOS CATEGORICOS
# AGRUPAR O ESTADO
agrupado = dataset.groupby(['Estado']).size()
agrupado


# In[19]:


agrupado.plot.bar(color = 'red') # GERANDO UM GRAFICO DE BARRAS DA COR "red"(VERMELHA)


# In[20]:


# AGRUPAR PELO GENERO
agrupado = dataset.groupby(['Genero']).size()
agrupado


# In[21]:


agrupado.plot.bar(color = 'blue') # GERANDO UM GRAFICO DE BARRAS DA COR "blue"(AZUL)


# In[22]:


# EXPLORAR COLUNAS NUMÉRICAS
# A COLUNA Score
dataset["Score"].describe()


# In[23]:


srn.boxplot(dataset['Score']).set_title('Score')


# In[25]:


srn.distplot(dataset['Score']).set_title('Score')


# In[26]:


# IDADE
dataset['Idade'].describe()


# In[29]:


srn.boxplot(dataset['Idade']).set_title('Idade')
# OS PONTOS FORA DO PADRÃO SÃO OS OUTLAES


# In[30]:


srn.distplot(dataset['Idade']).set_title('Idade')


# In[34]:


# SALDO
dataset['Saldo'].describe()


# In[32]:


srn.boxplot(dataset['Saldo']).set_title('saldo')


# In[35]:


srn.distplot(dataset['Saldo']).set_title('Saldo')


# In[36]:


# SALÁRIO
dataset['Salario'].describe()


# In[37]:


srn.boxplot(dataset['Salario']).set_title('Salario')


# In[38]:


srn.distplot(dataset['Salario']).set_title('Salario')


# In[39]:


# CONTAMOS VALORES NAN
# GENERO E SALÁRIO
dataset.isnull().sum()


# # FAZENDO AS CORREÇÕES NOS DADOS

# In[40]:


# SALARIOS
# REMOVER NANS E SUBSTITUIR PELA MEDIANA
dataset['Salario'].describe()


# In[41]:


mediana = sts.median(dataset['Salario'])
mediana


# In[42]:


# SUBSTITUIR NAN POR MEDIANA
dataset['Salario'].fillna(mediana, inplace=True)


# In[43]:


# VERIFICAR SE NAN NÃO EXISTEM MAIS
dataset['Salario'].isnull().sum()


# In[44]:


# GENERO, FALTA DE PADRONIZAÇÃO E NANS
agrupado = dataset.groupby(['Genero']).size()
agrupado


# In[45]:


# TOTAL DE NANS 
dataset['Genero'].isnull().sum()


# In[48]:


# PREENCHE NANS COM MASCULINO (moda)
dataset['Genero'].fillna('Masculino', inplace=True)


# In[49]:


# VERIFICAR NOVAMENTE OS NANS
dataset['Genero'].isnull().sum()


# In[50]:


# PADRONIZAR DE ACORDO COM O DOMINIO
dataset.loc[dataset['Genero']  ==  'M', 'Genero'] = 'Masculino'
dataset.loc[dataset['Genero'].isin( ['Fem','F']), 'Genero'] = 'Feminino'

# VISUALIZAR O RESULTADO
agrupado = dataset.groupby(['Genero']).size()
agrupado


# In[51]:


# IDADE FORA DO DOMINIO
dataset['Idade'].describe()


# In[52]:


# VISUALIZAR
dataset.loc[(dataset['Idade'] < 0) | ( dataset['Idade'] > 120)]


# In[54]:


# CALCULAR A MEDIANA
mediana = sts.median(dataset['Idade'])
mediana


# In[55]:


# SUBSTITUIR
dataset.loc[(dataset['Idade'] < 0 ) | (dataset['Idade'] > 120), 'Idade'] = mediana


# In[56]:


# VERIFICAMOS SE AINDA EXISTEM IDADE FORA DO DOMÍNIO
dataset.loc[(dataset['Idade'] < 0 ) | ( dataset['Idade'] > 120 )]


# In[58]:


# DADOS DUPLICADOS, BUSCANDO PELO ID
dataset[dataset.duplicated(['Id'],keep=False)]


# In[59]:


# EXCLUIMOS PELO ID
dataset.drop_duplicates(subset='Id', keep='first',inplace=True)#subset = nome da coluna | keep='first' = vai manter o primeiro Id
# BUSCAMOS DUPLICADOS
dataset[dataset.duplicated(['Id'],keep=False)] # MESMO CODIGO DA CELULA DE CIMA | VERIFICAR SE AINDA TEM DUPLICADOS


# In[60]:


# ESTADO FORA DO DOMINIO
agrupado = dataset.groupby(['Estado']).size()
agrupado


# In[61]:


# ATRIBUIMOS RS PELA MODA ->(moda = É O DE MAIOR VALOR, NO CASO "RS")
dataset.loc[dataset['Estado'].isin( ['RP','SP','TD']), 'Estado'] = 'RS'# isin = (ESTAR EM) PARA MEXER COM CONJUNTO
agrupado = dataset.groupby(['Estado']).size()


# In[62]:


# VERIFICANDO O RESULTADO
agrupado


# In[63]:


# OUTLIERS EM SALARIO, VAMOS CONSIDERAR 2 DESVIO PADRÃO
desv = sts.stdev(dataset['Salario'])
desv


# In[64]:


# DEFINIR PADRÃO COMO MAIOR QUE 2 DESVIO PADRÃO
# CHECAMOS SE ALGUM ATENTE CRITÉRIO
dataset.loc[dataset['Salario'] >= 2 * desv ]


# In[67]:


# VAMOS ATUALIZAR SALARIO PARA MEDIANA, CALCULAMOS
mediana = sts.median(dataset['Salario'])
mediana


# In[69]:


# ATRIBUIMOS
dataset.loc[dataset['Salario'] >= 2 * desv, 'Salario'] = mediana
#CHECAMOS SE ALGUM ATENDE CRITÉRIO
dataset.loc[dataset['Salario'] >= 2 * desv]


# In[70]:


dataset.head()


# In[71]:


dataset.shape


# In[ ]:





# In[ ]:





# In[ ]:




