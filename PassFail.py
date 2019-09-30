#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]

# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']


# In[3]:


df['lettergrade'] = pd.cut(df['grade'], bins,labels=group_names)
df


# In[4]:


pd.value_counts(df['lettergrade'])


# In[6]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df['status'] = pd.cut(df['grade'], bins,labels=status_names)
pd.value_counts(df['status'])


# In[ ]:




