#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandera as pa


# In[2]:


df = pd.read_csv("ocorrencia.csv", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head()


# In[10]:





# In[7]:


df.dtypes


# In[8]:


df.ocorrencia_dia.dt.month


# In[9]:


df.head()


# In[10]:


df.dtypes


# pip install pandera

# In[45]:


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


# In[46]:


schema.validate(df)


# In[ ]:




