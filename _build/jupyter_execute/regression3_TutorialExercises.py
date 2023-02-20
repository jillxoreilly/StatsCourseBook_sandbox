#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# The tutorial exercises this week will form the basis of your next hand-in assignment. You will be using real data that were collected in 2019 about people’s perception of their social standing and their happiness. These data were collected online by the well-respected polling company YouGov. The data are intended to be representative of the UK population. 
# 
# Note: as well as completing these exercises, it’s a good idea to review the instructions for the assignment ahead of the tutorial, so that you can check you understanding with your tutor. 
# 
# The variables are as follows:
# 
# *	`happy` (a continuous measure ranging from 0-10, where higher scores are greater happiness)
# *	`ladder` (a continuous measure of 1-11 where participants rate themselves in their standing in society, where the lowest rung on the ladder was labelled “bottom of society” and the top rung as “top of society”)
# *	`age` (a continuous measure in years)
# *	`marital` (a categorical measure of marital status with three categories) 
# *	`work` (a categorical measure of working status with four categories)
# *	`educ` ( a categorical measure of educational qualifications summarised into 3 categories)
# *	`sex` (male, female)
# *	`leftout` (a categorical variable in which people state whether they agree or disagree that they feel left out of society)
# *	`income` (a categorical variable with four categories)
# *	`region` (a categorical variable with twelve categories)
# 
# 
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
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### Import and view the data

# In[2]:


# Your code here to import the data from the file Happy.csv


# ### Data cleaning
# 
# First, get to know your data and do any necessary data cleaning. 
# 
# YouGov uses codes of 99 to indicate missing data. Change these to NaN.

# In[3]:


# Your code here to remove missing values!


# ### Control Variables
# 
# * The outcome variable here is `happy` 
# * The main explanatory variable is `ladder`  
# * There are a set of 8 possible control variables. 
# 
# Which do you think might be important controls here? 
# 
# There is no right or wrong answer here but think about your reasons for selecting your control variables (don’t just throw all of them in!).
# 
# Specify two regression models - Model 1 includes just the main explanatory variable. Model 2 adds the control variables of your choice (and keeps the main explanatory variable). Calculate the RMSE for both. 
# 

# In[4]:


# Your code here!


# ### Compare your two models:
# 
# * Which is better fitting in terms of the $R^2$? 
# * And which has a smaller spread of values around the regression line? 

# In[5]:


# Your answer here!
# You may need to add extra cells


# ### Interpret your regression models. 
# 
# Make some notes:
# * Which coefficients are significant? 
# * What are the confidence intervals around the slope for ‘ladder’? 
# * Does the coefficient for ‘ladder’ change much between model 1 and model 2? 
# * What can we conclude about the relationship between perceptions of social standing and happiness? 
# * Looking at the association between the control variables and happiness, are these as you might have expected, or are there any surprises here?

# In[6]:


# Your answer here!
# You may need to add extra cells


# ### Check the regression assumptions. 
# 
# Refer back to section 15.7 for the code for three plots.

# In[7]:


# Your code here


# What conclusions can you draw about the following assumptions?
# 
# 1.	Linearity
# 2.	Constant variance (homoscedasticity)
# 3.	Normally distributed residuals
# 

# In[ ]:




