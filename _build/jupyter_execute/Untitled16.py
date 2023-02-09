#!/usr/bin/env python
# coding: utf-8

# # Regression models in Python
# 
# We will be using the statsmodels package in Python, so we will need to import this along with the other Python packages we have been using.
# 
# 
# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries
# 

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsomdel.api as sm
import statsmodels.formula.api as smf


# ## Life satisfaction full dataset
# 
# Let's import the full dataset for life satisfaction vs GDP

# In[ ]:


#


# ### Data cleaning
# 
# We are working with real data here! We need to examine it and take any necessary steps to clean the data before we begin analysis. 
# 
# * What steps do you need to take to clean the data? 
# * Are there any data points that look wrong (e.g., too low or too high)? Change any suspicious values to ‘NaN’.
# * How many missing data points do you have on lifesat? 
# * How many missing data points do you have on GDP per capita?
# 

# In[1]:


# your code here to clean the data


# * How many valid data points do you have? 
# 
# 
# ### Describing the data
# 
# Let’s begin with some descriptive analysis before running our first regression model. 
# 
# Run a scatterplot. Be sure to plot $y$ on the $y$-axis and $x$ on the $x$-axis. 
# (If you are not sure which is which, discuss with your tutor).
# 

# In[ ]:


# your code here for a scatterplot


# * What are your initial conclusions about the relationship between GDP and life satisfaction? 
# 
# ### Regression model
# 
# It’s time to run the regression model. 
# 
# The basic code is added for you, but you need to complete it. 
# 
# Where do you tell Python which is the $y$ variable, and which is the $x$?

# In[ ]:


# code for regression model


# Look at the Python regression output. 
# 
# * Find the intercept and the slope. 
# * Write out the regression equation (on your computer or by hand on paper). 
# * Make notes on how to interpret the intercept and the slope. E.g., “the intercept is the average life satisfaction in a country with…” And “the slope of x.xx means that for every additional $1000 in GDP…”
# 
# ### Regression plot
# 
# Let’s add the regression line to the scatterplot in Python. Here’s the code:
# 

# In[2]:


# Code for scatterplot with regression line.


# Eyeballing the scatterplot, how well do you think the regression line fits the data points? Do you think there are any outliers? We can see that several countries with very large GDPs are below the regression line. Also, that many countries with very low GDP are a long way from the regression line. We can examine potential outliers more systematically, by asking Python to calculate residuals (and predicted values) for us.

# In[ ]:


# Code for generating and storing y-hat and residuals for each data point.


# Can you find the sum of squared residuals? 

# In[ ]:


# Code for squaring then adding up all the residuals.


# 1. How meaningful is the sum of squared residuals (or “sum of squared error” - SSE)? What does it tell us?
#     * We know this is the minimized residual. Because this line is fitted using the method of least squares, there is no other line that could fit the data with a lower SSE. 
#     
# Sort and display the data and find any very large residuals (remember outliers could have a positive or negative residual. Look for both!). Choose the 6 largest residuals (in absolute terms). Which countries are they? Are they in the same region, are they rich or poor? 
# 
# Now change the life satisfaction for these six countries to ‘NaN’ so that we can exclude them from the analysis. Store the data with the excluded outliers with a new name. Then re-run the regression, and the scatterplot with regression line.
# 

# In[ ]:


# your code here!


# In[ ]:





# In[ ]:





# In[ ]:




