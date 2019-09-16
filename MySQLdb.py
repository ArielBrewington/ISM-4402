#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)

df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])



# In[24]:


import os
import sqlite3 as lite

db_filename = r'datasets/mydb.db'
con = lite.connect(db_filename)

df.to_sql('mytable',con,flavor='sqlite',
          schema=None,if_exists='replace',index=True,
          index_label=None,chunksize=None,dtype=None)

con.close()


# In[ ]:




