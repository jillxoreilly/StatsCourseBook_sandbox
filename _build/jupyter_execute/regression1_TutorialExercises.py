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
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ## Life satisfaction full dataset
# 
# Let's import the full dataset for life satisfaction vs GDP

# In[2]:


happy = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/All_countries_lifesat_2020.csv')
happy


# ### Data cleaning
# 
# We are working with real data here! We need to examine it and take any necessary steps to clean the data before we begin analysis. 
# 
# * What steps do you need to take to clean the data? 
# * Are there any data points that look wrong (e.g., too low or too high)? Change any suspicious values to ‘NaN’.
# * How many missing data points do you have on lifesat? 
# * How many missing data points do you have on GDP per capita?
# 

# In[3]:


# your code here to clean the data


# * How many valid data points do you have? 
# 
# 
# ### Describing the data
# 
# Let’s begin with some descriptive analysis before running our first regression model. 
# 
# Run a scatterplot. 
# 
# Be sure to plot $y$ on the $y$-axis and $x$ on the $x$-axis. 
# (If you are not sure which is which, discuss with your tutor).
# 

# In[4]:


# Your code here for the scatterplot


# * What are your initial conclusions about the relationship between GDP and life satisfaction? 
# 
# ### Regression model
# 
# It’s time to run the regression model. 
# 
# The basic code can be copied from the worked examples in the previous notebook, but you will need to modify it. 
# 
# Where do you tell Python which is the $y$ variable, and which is the $x$?

# In[5]:


# code for regression model


# Look at the Python regression output. 
# 
# * Find the intercept and the slope. 
# * Write out the regression equation (on your computer or by hand on paper). 
# * Make notes on how to interpret the intercept and the slope. E.g., “the intercept is the average life satisfaction in a country with…” And “the slope of x.xx means that for every additional $1000 in GDP…”
# 
# ### Regression plot
# 
# Let’s add the regression line to the scatterplot in Python. 
# 
# 
# `seaborn` has a special plotting function for plotting a scatterplot with regression line included, called `sns.regplot`. 
# 
# Give it a try, the syntax is the same as for `sns.scatterplot`
# 

# In[6]:


# your code here for a scatterplot with regression line using sns.regplot


# Eyeballing the scatterplot, how well do you think the regression line fits the data points? Do you think there are any outliers? We can see that several countries with very large GDPs are below the regression line. Also, that many countries with very low GDP are a long way from the regression line. We can examine potential outliers more systematically, by asking Python to calculate residuals (and predicted values) for us.

# In[7]:


# Your code here to generate predictions (y-hat) and residuals for each data point.
# add them as columns to your datafram
# view the resulting dataframe


# ### SSE
# 
# Can you find the sum of squared residuals using an equation?
# 
# Hint: The code for $x^2$ in Python is `x**2`

# In[8]:


# Your code here for squaring then adding up all the residuals.


# * How meaningful is the sum of squared residuals (or “sum of squared error” - SSE)? What does it tell us?
#     * We know this is the minimized residual. Because this line is fitted using the method of least squares, there is no other line that could fit the data with a lower SSE. 
# 
# The sum of squared residuals is provided by `statsomdels` as `reg_results.ssr` - 
# 
# * check that the sum of squared residuals you calculated matches the output of `reg_results.ssr`
# 
# 
# 

# In[9]:


# your code here


# ### Check datapoints that are not well fit by the model
# 
# Sort and display the data and find any very large residuals (remember outliers could have a positive or negative residual. Look for both!). Choose the 6 largest residuals (in absolute terms). Which countries are they? Are they in the same region, are they rich or poor? 
# 
# Now change the life satisfaction for these six countries to ‘NaN’ so that we can exclude them from the analysis. Store the data with the excluded outliers with a new name. Then re-run the regression, and the scatterplot with regression line.
# 

# In[10]:


# your code here!


# In the new analysis with the six outliers excluded, do your conclusions about the relationship between GDP and life satisfaction change, or stay the same?
# 
# We will learn more about the assumptions of regression in the next week or two, but looking back at the scatterplot, have you noticed any potential concerns about the model?
# 
# 

# In[ ]:





# In[ ]:




