#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.xlsx"
df = pd.read_excel(Location)


# In[3]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr']
df.head()


# In[4]:





# In[ ]:




