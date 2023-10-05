#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# This week's tutorial exercises focus on indexing and obtaining descriptive statistics
# 
# ### Set up Python Libraries
# 
# As usual you will need to run this code block to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### Import a dataset to work with
# 
# You will need to download the file OxfordWeather.csv from Canvas to your computer, then import it

# In[2]:


weather = pandas.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# ## Exercises
# 
# In the following questions, we descriptive statistics and indexing to answer some questions about the weather and climate in Oxford.
# 
# Where you are asked to calculate a value (such as the mean) rather than output a table, you should **report your answer in words** in the text box below the code block.
# 
# Where the question asks you to "comment", you are simmply being asked to engage with the data/ explain what  you notice in plain English. Please discuss with your fellow students and your tutor as this is a really important skill for data analysis.
# 
# ### Part 1: Heat

# #### a. What was the hottest temperature on record?
# 
# Note that the dataset ends in April 2022 and therefore does not include the record heatwave of summer 2022.

# In[3]:


# Your code here


# *Your text here*

# #### b. On what date did the hottest temperature occur?
# 
# Hint: you could use `df.query()` to help you here

# In[4]:


# Your code here


# *Your text here*

# #### c. Display the 10 hottest days on record and comment
# 
# Hint: you can use `df.values_sort()` and `df.head()` or `df.tail()` to help you here

# In[5]:


# Your code here


# *Your comment here*

# #### d. Find the mean of maximum daily temperature (Tmax) for each month and comment
# 
# Hint: you can use `df.groupby()` to help you here

# In[6]:


# Your code here


# *Your comment here*

# #### e. Make a table displaying the mean and standard deviation of Tmax in each month
# 
# Hint: A combination of `df.agg()` and `df.groupby()` will help you here

# In[7]:


# Your code here


# #### e. Make a table displaying the mean of Tmax and Tmin in each month
# 
# Hint: A combination of `df.agg()` and `df.groupby()` will help you here

# In[8]:


# Your code here


# ### Part 2: Rain

# #### a. Run this code block to add a column called <tt>wet</tt> containing a <tt>True</tt> for days on which it rained and <tt>False</tt> otherwise
# 
# We will practice adding columns in a later session

# In[9]:


# Your code here
weather['wet']=weather.Rainfall_mm>0
weather


# #### b. What is the proportion of wet days overall?
# 
# Hint: The values <tt>True</tt> and <tt>False</tt> can be treated as <tt>1</tt> and <tt>0</tt> respectively.
#     
# To get the proportion of days on which <tt>wet==True</tt>, we can use a programmming trick which is to simply take the mean of the column <tt>wet</tt>:
#     
# * say there are 100 days in my sample
#     * say 66 of them, <tt>wet==True==1</tt>
#     * for the other 44, <tt>wet==False==0</tt>
# * If we take the mean, this gives us the proportion of wet days because we:
#     * add up all the values (answer=66) 
#     * divide by the number of cases (100)
#     * result is 66/100 = 0.66 or 66%, the proportion of wet days

# In[10]:


# your code here


# *Your text here*

# #### c. What is the proportion of wet days in each month? Comment on your findings
# 
# Hint: use `df.groupby()`

# In[11]:


# your code here


# *Your comments here*

# #### d. What is the mean quantity of rainfall (in mm) in each month? Comment on your findings

# In[12]:


# your code here


# *Your comment here*

# #### e. Display the 10 wettest days on record and comment

# In[13]:


# Your code here


# *Your comment here*

# #### f. Compare and contrast the different findings in part 2 c,d, and e
# 
# Different descriptive statistics tell us different things about the same data!

# *Your comments here!*

# ### Snow
# 
# #### a. Create a dataframe <tt>WhiteChristmas</tt> containing the weather on Christmas day, for all the years in which there was a White Christmas 
# 
# Hint: we don't have a column telling us when is has snowed, but it is reasonable to assume this happens when the minimum temperature dips below zero, and Rainfall_mm is above zero.

# In[14]:


# Your code here
# WhiteChristmas = 


# #### b. Sort the dataframe <tt>WhiteChristmas</tt> by year and comment

# In[15]:


# Your code here


# *Your comments here*

# #### c. Any issues with our definition of 'snow'?
# 
# We defined snow as when the <tt>Tmin</tt> falls below zero and Rainfall is non-zero. 
# 
# * Do you think this over- or under- estiamtes the number of snowy days?
# * Why?

# *Your comments here*

# #### d. How common is 'proper' snowfall in Oxford?
# 
# Let's focus on days with enough snowfall to make at least a tiny snowman! Assume that this happens when TMin is below zero and there is more than 4mm of rainfall 
# 
# * 4mm of rain makes about 5cm of soggy snow in Oxford conditions, although it would make a uch greater depth of powder in a cold dry atmosphere like Utah or Colorado
# 
# Create a dataframe called <tt>SnowDays</tt> containing only days with enough snow to make a snowman.
# 
# You can check how often this happened in recent years using `df.tail()`

# In[16]:


# Your code here


# *Your comments here*
# 
# 

# In[ ]:




