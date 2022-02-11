#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("ocorrencia.csv", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head(5)


# In[5]:


df.loc[1,'ocorrencia_cidade']


# In[6]:


df.loc[1:3]


# In[7]:


df.codigo_ocorrencia.is_unique


# In[9]:


df.set_index('codigo_ocorrencia', inplace=True)


# In[10]:


df.head()


# In[12]:


df.loc[45407]


# In[13]:


df


# In[ ]:




