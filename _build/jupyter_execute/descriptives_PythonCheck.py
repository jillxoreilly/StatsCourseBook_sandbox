#!/usr/bin/env python
# coding: utf-8

# # Python skills check
# 
# Here we will review all the Python skills you should know by the end of this week

# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ### Load the data
# 
# <img src="https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/images/titanic.jpg" width=50% alt="Picture of the Titanic" />
# 
# <br>
# <br>
# 
# Let's load some data about the passengers of the Titanic from the file "data/titanic.csv"

# In[2]:


titanic = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/titanic.csv')
display(titanic)


# You can find some information abbout this dataset on <a href="https://www.kaggle.com/competitions/titanic/data">Kaggle</a> including explanations of the less obvious column headers
# 
# ### Get descriptives
# 
# Let's get some descriptive statistics, just for practice:

# In[3]:


# How many people were in each class? Hint - use df.value_counts() which we saw on the page on data cleaning


# In[4]:


# What was the mean fare in each class? Hint- use .mean() and .groupby()


# In[5]:


# What was the standard deviation of fare in each class? Hint- use .std() and .groupby()


# In[6]:


# What was the 10th and 90th centile of age overall?


# In[7]:


# display rows 400-420 of the dataframe


# In[8]:


# display only passengers under 12 years old


# In[9]:


# display only passengers whose age is unknown (NaN)


# In[10]:


# count how many passengers' age was unknown


# In[11]:


# display only passengers over 70 years old


# Wait a minute!
# 
# There was something strange in that last dataframe. Maybe someone's age was mis-recorded?

# In[12]:


# replace the misrecorded age with NaN - hint - check the page on data cleaning

# and display the relevant part of the dataframe to check
titanic[420:425]


# In[ ]:




