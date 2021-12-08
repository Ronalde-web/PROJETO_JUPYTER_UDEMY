#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import seaborn as srn
import statistics as sts


# In[55]:


path = pd.read_csv('C:/Users/Ronalde/DADOS-DO- CURSO-UDEMY/FormaçãoCD2/10.Prática em Python/dados/tempo.csv', sep=';')


# In[56]:


tempo = path
tempo.head()


# In[57]:


tempo.shape


# In[58]:


agrupado = tempo.groupby(['Aparencia']).size()
agrupado


# In[59]:


tempo['Umidade'].describe()


# In[60]:


agrupado.plot.bar(color = 'red')


# In[61]:


agrupado = tempo.groupby(['Jogar']).size()
agrupado


# In[62]:


agrupado.plot.bar(color = 'red')


# In[63]:


tempo.isnull().sum()


# In[64]:


tempo['Umidade'].describe()


# In[65]:


mediana = sts.median(tempo['Umidade'])
mediana


# In[66]:


tempo['Umidade'].fillna(mediana, inplace=True)


# In[67]:


tempo['Umidade'].isnull().sum()


# In[68]:


tempo.drop('Vento', axis = 1, inplace=True)


# In[69]:


tempo.head()


# In[70]:


tempo.loc[tempo['Aparencia']  ==  'menos', 'Aparencia'] = 'sol'


# In[71]:


agrupado = tempo.groupby(['Aparencia']).size()
agrupado


# In[72]:


tempo.loc[(tempo['Umidade'] < 0) | ( tempo['Umidade'] > 100)]


# In[73]:


# CALCULAR Á MÉDIA 
mediana = sts.median(tempo['Umidade'])
mediana


# In[74]:


# CORRIGIR O DADO QUE ESTAR ERRADO
tempo.loc[(tempo['Umidade'] < 0 ) | (tempo['Umidade'] > 100), 'Umidade'] = mediana


# In[75]:


tempo.loc[(tempo['Umidade'] < 0) | ( tempo['Umidade'] > 200)]


# In[76]:


tempo.shape


# In[77]:


tempo.head(14)


# In[78]:


tempo.loc[(tempo['Temperatura'] < -130) | ( tempo['Temperatura'] > 130)]


# In[79]:


# CALCULAR Á MÉDIA DA TEMPERATURA
mediana = sts.median(tempo['Temperatura'])
mediana


# In[80]:


tempo.loc[(tempo['Temperatura'] < -130 ) | ( tempo['Temperatura'] > 130), 'Temperatura'] = mediana


# In[81]:


tempo.loc[(tempo['Temperatura'] < -130 ) | ( tempo['Temperatura'] > 130)]


# In[82]:


tempo.head(14)


# In[ ]:





# In[ ]:




