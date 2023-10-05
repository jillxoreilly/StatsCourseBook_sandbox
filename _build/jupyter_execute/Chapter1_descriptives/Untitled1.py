#!/usr/bin/env python
# coding: utf-8

# # Key Python functions: Missing data and NaNs
# 
# In this notebook we gather together and recap the <tt>Pandas</tt> functions we have learned this week:
# * Functions for **locating outliers**
# * Syntax for replacing missing data with **NaN**
# 
# ## Set up Python Libraries
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


# ## Import a dataset to work with
# 
# You will need to download the file OxfordWeather.csv from Canvas to your computer, then import it

# In[2]:


weather = pandas.read_csv("https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/OxfordWeather.csv")
display(weather)


# In[ ]:




