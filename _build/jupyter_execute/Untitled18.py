#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assessing Regression models in Python.

The process of applying equations for $R^2$, standard errors, and the 95% confidence intervals around the slope are all done for us in Python. In fact, without asking, Python gives us these statistics in the regression output. To have a first look, we will come back to the immigration attitudes data from last week’s tutorial. 


### Set up Python libraries

As usual, run the code cell below to import the relevant Python libraries


# In[ ]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

