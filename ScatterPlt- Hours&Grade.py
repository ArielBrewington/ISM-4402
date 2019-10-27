#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

dataframe = pd.DataFrame({'Col': np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location = "datasets/gradedata.csv"
df= pd.read_csv(Location)
df.head()


# In[3]:


plt.scatter (df['hours'],df['grade'])


# In[ ]:




