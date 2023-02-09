#!/usr/bin/env python
# coding: utf-8

# # Regression models in Python
# 
# We will be using the `statsmodels` package in Python, so we will need to import this along with the other Python packages we have been using. 
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
import statsmodels.formula.api as smf


# If that threw an error, you may need to install `statsmodels` before you can import it.
# 
# Try this code block:

# In[2]:


get_ipython().system('pip3 install statsmodels')


# ... and then rerun the importing block above

# ## Happiness toy example
# 
# The python code, once you get the hang of it, is pretty straightforward. The output that Python gives is a whole table of statistics, some of which are important to us in this class, and some will be important later, and some we won’t need in the course at all. 
# 
# So, when looking at the Python output, the key objective for the moment is to know where to find the key things, e.g., the intercept and slope coefficients.
# 
# Let’s run a regression model in Python for the ‘toy’ country happiness data. 

# In[3]:


# import and view data
happiness=pandas.read_csv('data/happiness10.csv')
happiness


# In[4]:


# run the regression model


# * Find the intercept and the slope. How does Python label these?
# 
# Python will also help us out with the predicted values and residuals. 
# 
# * Run the following code which will store $\hat{y}$ and the residual for each row of the data. Display the result. 
# 

# In[5]:


# code for storing y-hat and residuals


# This should look familiar! We had the same table back in concepts section. (There may be small differences due to rounding). Do you think there are any outliers in the data? As we noted earlier, there was one very high and one very low value among the residuals. 
# 
# Let’s try re-running the regression model without these two potential outliers: Finland and Ukraine. Let’s change the happiness measure to ‘NaN’ for these two countries and re-run the regression command.
# 

# In[6]:


# Code for changing Sweden to NaN, and new regression model


# What’s changed in the model? 
# 
# * Has the slope value become bigger and smaller? 
# 
# * Has the conclusion changed?

# # The calculation for the slope and intercept 
# 
# Back in Week 4 when you were learning about correlation and covariance, you saw the formula for calculating b, the slope coefficient. 
# 
# Remember the Height/ Finger length example?
# 
# The equation for finding $b$ is
# 
# $$ b = \frac{s_{xy}}{s^2_x} $$

# In[7]:


# load and view the data
heightFinger = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/HeightFingerInches.csv')
display(heightFinger)


# The equation for finding $b$ is
# 
# $$ b = \frac{s_{xy}}{s^2_x} $$
# 
# Let's apply that in Python

# In[8]:


s_x = heightFinger['Height'].std()
s_y = heightFinger['FingerLength'].std()
s_xy = heightFinger['Height'].cov(heightFinger['FingerLength'])

b = s_xy/(s_x**2)
print('b = ' + str(b))


# What is the value of the intercept? The equation for finding the intercept is as follows:
# 
# $$ a = \bar{y} - b\bar{x} $$
# 
# $\bar{x}$ and $\bar{y}$ are the means of $x$ and $y$ for the 10 data points. 
# 
# Use Python to find the mean of $y$ and $x$. 

# In[9]:


x_bar = heightFinger.Height.mean()
y_bar = heightFinger.FingerLength.mean()


# Can you calculate $a$? 

# In[10]:


a = 6.7 + (49.4*0.055) 
a


# In[11]:


a = y_bar - b*x_bar
a


# Let’s run a regression model in Python for the finger length data, to check our results. 

# In[12]:


# Code for importing finger length data, and regression model. 


# Great! Our calculations based on the equations are confirmed by Python’s regression table. 

# ### Quick extra questions
# 
# Here are some extra questions on the Regression output table, to see if you can begin to pick out all the important information. 
# 
# 1. In the top left, it gives the method as ‘Least Squares’. Above, it gives the model type as ‘OLS’. Do you know what OLS stand for?
#     * Ordinary Least Squares
# 1. How many observations are in this model according to the regression output table?
#     * 71,341
# 1. What do you think ‘std err’ might stand for, in the column after ‘coef’?
#     * Standard Error. You learned about this important concept in Week 6, and we’ll come back to it again in a couple of weeks. 
# 

# In[ ]:




