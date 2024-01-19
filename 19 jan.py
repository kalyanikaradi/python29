#!/usr/bin/env python
# coding: utf-8

# In[1]:


#data manipulation
import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv('train.csv')


# In[3]:


type(data)


# In[4]:


data


# In[5]:


#head function (The head() function in pandas displays the top rows of a DataFrame)
data.head()


# In[6]:


# tail() function shows the bottom rows. 
data.tail()


# In[7]:


data['Pclass']


# In[9]:


#iloc[] is an indexer used for integer-location-based indexing of data in a DataFrame. It allows users to select specific rows and columns. 
data.iloc


# In[10]:


data.iloc[:,2]


# In[12]:


#shows the unique values
data['Pclass'].unique()


# In[14]:


data.shape


# In[15]:


data.info()


# In[16]:


data['Age']


# In[17]:


data.describe()#returns numerical data by calculting mean,medain etc


# In[19]:


#(include = ['O']) it pulls out the objects dtypes attributes and shows their count/frequency/max/quartiles
data.describe(include='O')


# In[20]:


data.columns


# In[21]:


data.Embarked.value_counts()


# In[22]:


data.Survived.value_counts()


# In[24]:


data.PassengerId.value_counts()


# In[25]:


data.Pclass.value_counts()


# In[26]:


data.Age.value_counts()


# In[ ]:




