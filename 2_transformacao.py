#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandera as pa


# In[6]:


valores_ausentes = ['**','###!','####','****','*****','NULL'] 
df = pd.read_csv("ocorrencia.csv", sep=',', parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
df.head(10)


# In[10]:


schema = pa.DataFrameSchema(
    columns = {
        "codigo_ocorrencia":pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String, nullable=True),
        "ocorrencia_uf": pa.Column(pa.String, nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime, nullable=True),
        "ocorrencia_hora": pa.Column(pa.String, nullable=True),
        "total_recomendacoes": pa.Column(float, nullable=True)        
        
    })


# In[11]:


schema.validate(df)


# In[12]:


df.dtypes


# In[14]:


df.loc[1]


# In[15]:


df.iloc[-1]


# In[16]:


df.tail()


# In[17]:


df.iloc[10:15]


# In[18]:


df.loc[:,'ocorrencia_uf']


# In[19]:


df.isna().sum()


# In[20]:


filtro = df.ocorrencia_uf.isnull()
df.loc[filtro]


# In[21]:


df.count()


# In[25]:


#ocorrencias com mais de 10 recomendações

filtro = df.total_recomendacoes > 10
df.loc[filtro, ['ocorrencia_cidade','total_recomendacoes']]


# In[27]:


#ocorrencias cuja classificação é igual a INCIDENTE GRAVE

filtro = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'
df.loc[filtro]


# In[30]:


#ocorrencias cuja classificação é igual a INCIDENTE GRAVE e estado SP

filtro = df.ocorrencia_classificacao == 'INCIDENTE GRAVE'
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro | filtro2]


# In[32]:


#ocorrencias cuja classificação é igual a INCIDENTE GRAVE e estado SP

filtro = df.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE'])
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro | filtro2]


# In[ ]:




