#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

Location = "datasets/axisdata.csv"
df= pd.read_csv (Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[6]:


pd.pivot_table(df,values= ['Cars Sold'],index = ['Gender'])


# In[7]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


df['Years Experience'].mean()


# In[9]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[10]:


pd.pivot_table(df,values= ['Cars Sold'],index = ['SalesTraining'])


# In[21]:


import matplotlib.pyplot as plt
import pandas as pd

names = ['Jada','Nicole','Tanya','Ronelle','Brad']
gender = ['Female','Male']
hoursworked = [39,46,42,38,33]
WorkList = zip(names,hoursworked)
df = pd.DataFrame(data = WorkList, columns=['Names', 'HrsWorked'])

get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')


# In[22]:


df2 = df.set_index(df['Names'])
df2.plot(kind="bar")


# In[23]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[25]:


plt.scatter (df['Cars Sold'], df['Hours Worked'])


# In[26]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[34]:


df.hist(column= "Years Experience", by="SalesTraining")


# In[ ]:




