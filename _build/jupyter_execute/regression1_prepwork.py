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
import statsmodels.api as sm
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
# 
# ### Import and view data

# In[3]:


# import and view data
happiness=pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/happiness10.csv')
happiness


# ### Run the regression using `statsmodels`

# In[4]:


# run the regression model

# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = happiness, formula = 'LifeSat ~ GDPpc')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 

# note you get a warning message because the dataset is quite small - disregard this
                                             


# 
# ### Interpreting the output
# 
# The summary output is three tables
# 
# The **top table** tells us about the regression we ran, including 
# * what was the dependent variable
# * how many observations there were
# * type of regression model used (in this case Ordinary Least Squares, OLS - don't worry about this for now)
# * various measures of model fit such as $R^2$, AIC, BIC, Log-Likelihood - some (but not all) of these will be covered in later weeks
# 
# The **middle table** gives the output of the regression
# * coefficients (beta values) - in this simple regression these are the intercept and the slope
# * statistical significance of the effects (t and p values)
# 
# The **bottom table** contains some information about whether the assummptions of linear regression were satisfied
# 
# ### Predicted values, residuals
# 
# For now let's focus on the middle table
# 
# * find the values for the intercept and the slope. Can you write out the regression equation in the form
# 
# $$ \hat{y} = \beta_0 + \beta_1 x $$
# 
# ... replacing the $\beta$ values with numbers?
# 
# 
# You could work out the predicted value of $y$, namely $\hat{y}$, for each value of $x4 from the equation. 
# However `statsmodels` can give us the predicted values and residuals. 
# 
# * Run the following code which will give us the predicted values $\hat{y}$ for each row of the data. Display the result. 
# 

# In[5]:


# return predicted values
reg_results.fittedvalues


# ... and the residuals

# In[6]:


# return residuals
reg_results.resid


# These would be easier to view if we added them in as new columns in our dataframe:

# In[7]:


happiness['yhat']=reg_results.fittedvalues
happiness['residuals']=reg_results.resid
happiness


# This should look familiar! We had the same table back in concepts section. (There may be small differences due to rounding). 
# 
# Hopefully you can see that:
# 
# * The $\hat{y}$ values are fairly similar to the corresponding values of $y$, LifeSat
# * The residuals are positive when $y>\hat{y}$ and negative $y<\hat{y}$  
# * The size of the residual is larger when the difference between $y$ and $\hat{y}$ is larger
# 
# Do you think there are any outliers in the data? As we noted earlier, there was one very high and one very low value among the residuals. 
# 
# Let’s try re-running the regression model without these two potential outliers: Finland and Ukraine. Let’s change the happiness measure to ‘NaN’ for these two countries and re-run the regression command.
# 

# In[8]:


# Code for changing Finland and Ukraine to NaN
happiness_clean = happiness.copy()
happiness_clean[happiness_clean['Country']=='Ukraine']=np.nan
happiness_clean[happiness_clean['Country']=='Finland']=np.nan
happiness_clean


# In[9]:


# re-run the regression model

# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = happiness_clean, formula = 'LifeSat ~ GDPpc')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 


# ### What changed when we excluded outliers? 
# 
# * Has the slope value become bigger or smaller? 
# 
# * Has the conclusion changed?

# # The calculation for the slope and intercept 
# 
# Back in Week 4 when you were learning about correlation and covariance, you saw the formula for calculating $b$, the slope coefficient. 
# 
# Remember the Height/ Finger length example?
# 
# The equation for finding $b$ is
# 
# $$ b = \frac{s_{xy}}{s^2_x} $$

# In[10]:


# load and view the data
heightFinger = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/HeightFingerInches.csv')
display(heightFinger)


# The equation for finding $b$ is
# 
# $$ b = \frac{s_{xy}}{s^2_x} $$
# 
# Let's apply that in Python

# In[11]:


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

# In[12]:


x_bar = heightFinger.Height.mean()
y_bar = heightFinger.FingerLength.mean()


# Can you calculate $a$? 

# In[13]:


a = y_bar - b*x_bar
a


# Let’s run a regression model in Python for the finger length data, to check our results. 

# In[14]:


# run the regression model on height/finger data

# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = heightFinger, formula = 'FingerLength ~ Height')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 


# Find $a$ and $b$ in the regression output tablbe (they are not called $a$ and $b$ in the table - what are they called?). Do they match the values we calculated ourselves using the equation?
# 
# Great! Our calculations based on the equations are confirmed by Python’s regression table. 

# ### Quick extra questions
# 
# Here are some extra questions on the Regression output table, to see if you can begin to pick out all the important information. 
# 
# 1. In the top left, it gives the method as ‘Least Squares’. Above, it gives the model type as ‘OLS’. Do you know what OLS stand for?
#     * Ordinary Least Squares
# 1. How many observations are in the Height vs Finger model according to the regression output table?
#     * 3000
# 1. What do you think ‘std err’ might stand for, in the column after ‘coef’?
#     * Standard Error. You learned about this important concept in Week 6, and we’ll come back to it again in a couple of weeks. 
# 

# In[ ]:





# In[ ]:




