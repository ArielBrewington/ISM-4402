#!/usr/bin/env python
# coding: utf-8

# In[1]:


path_to_zip_file = "datasets.zip"directory_to_extract_to = ""import zipfilezip_ref = zipfile.ZipFile(path_to_zip_file, 'r')zip_ref.extractall(directory_to_extract_to)zip_ref.close()


# In[2]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[3]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[4]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[5]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


df.columns = ['Names','Grades']
df.head()


# In[7]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])

df.to_csv('studentgrades.csv',index=False,header=False)


# In[8]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.head()


# In[9]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.head()


# In[11]:


df.to_csv('studentgrades.csv',index=False,header=True)


# In[ ]:




