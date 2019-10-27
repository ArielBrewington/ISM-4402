#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df.hist()


# In[6]:


df.hist(column="age")


# In[7]:


df.hist(column="age", by="gender")


# In[ ]:




