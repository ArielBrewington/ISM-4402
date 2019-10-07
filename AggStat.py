#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]

GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,columns=['Names','Grades'])
df


# In[3]:


print 'count:', df['Grades'].count()  
print 'mean:', df['Grades'].mean()   

print 'standard deviation:', df['Grades'].std() 

print 'min:', df['Grades'].min()     
print 'max:', df['Grades'].max()    

print '1st quartile:', df['Grades'].quantile(.25)  
print '2nd quartile:', df['Grades'].quantile(.5)   
print '3rd quartile:', df['Grades'].quantile(.75)  


# In[4]:


print 'mean:', df['Grades'].mean()

print 'median:', df['Grades'].median()

print 'mode:', df['Grades'].mode()


# In[5]:


print 'variance:', df['Grades'].var()


# In[6]:


df.mean()


# In[7]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[8]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df= pd.DataFrame(data = GradeList, columns=['Names', 'Grades', 'BS', 'MS', 'PhD'])
df


# In[9]:


df.count()


# In[10]:


df.mean()


# In[11]:


df.std()


# In[12]:


df.min()


# In[13]:


df.max()


# In[14]:


df.quantile(.25)


# In[15]:


df.quantile(.5)


# In[16]:


df.quantile(.75)


# In[ ]:




