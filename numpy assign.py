#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Create a null vector of size 10

# In[6]:


x = np.zeros(10)
x[4]=1
x


# # values ranging from 10 to 49

# In[13]:


x = np.arange(10,50)
x


# # 3*3 matrix with range from 0 to 8

# In[15]:


x = np.arange(0,9).reshape(3,3)
x


# # indices of non-zero elements 

# In[18]:


x = np.nonzero([1,2,0,0,4,0])
x


# # 10 * 10 array find the min and max

# In[22]:


x = np.random.random((10,10))
print(x.min())
print(x.max())


# # random vector of size 30, find mean

# In[24]:


x = np.random.random(30)
print(x.mean())


# In[ ]:




