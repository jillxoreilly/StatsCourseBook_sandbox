#!/usr/bin/env python
# coding: utf-8

# # Assessing Regression models in Python.
# 
# The process of applying equations for $R^2$, standard errors, and the 95% confidence intervals around the slope are all done for us in Python. In fact, without asking, Python gives us these statistics in the regression output. To have a first look, we will come back to the immigration attitudes data from last week’s tutorial. 
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


# # ESS data
# 
# Let's work again with the European Social Survey data (attitudes to immigration)
# 
# ### Import and view data

# In[2]:


# load and view the data
ess = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/immigrationData.csv')
ess


# We’ll fit a regression model just like we did last week. 

# In[3]:


# Fit a regression model: Y = better, x1 = age, x2, = sex, x3 = education, x4 = bornuk.

# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = ess, formula = 'better ~ age + sex + educ + bornuk')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 


# ### Interpretation
# 
# Have a good look at the contents of the output table above 
# 
# * Find the standard error. 
# * Find the lower and upper confidence interval. 
# 
# Answer the quick questions:
# 
# 1. What is the slope for age, and what are the confidence intervals around the slope? How would you interpret these confidence intervals in words?
# 
#     * $b$ = -.0117951, the 95% confidence intervals are -.0174981 and -.0060921 meaning that we can be 95% confident that the true population value lies between these two points. The lower and upper confidence bounds are below zero, so we can be sure the slope is statistically significant.
#     
#     
# 2. What other information in the table can tell us the slope is statistically significant?
# 
#     * The standard error of .002908 can be used to give the $t$-statistic. -.0117951/.002908 = -4.06. As this $t$ value is larger than 1.96, we know the slope is statistically significant. The regression table also provides the $p$-value associated with this $t$-statistic. So, there are several ways to know if the slope is statistically significantly different to zero. 
#     
#     
# 3. For all the $x$-variables in this model, find the one(s) that are not statistically significant. 
#     * In this model, the variable for sex is not significant. There is no difference in immigration attitudes between men and women. 
#     
#     
# 4. What is the $R^2$ for this model, and how do we interpret it? 
#     * $R^2$ = 0.1358 meaning that 13.6% of the variability in $y$ is explained by these $x$s. 
#     
#     
# 5. Remember the model with political party? Do you think the $R^2$ in this model will be higher or lower? Let’s take a look. 

# In[4]:


# Code to run a regression. Y = better, x1 = age, x2, = sex, x3=vote x4 = age*vote.

# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = ess, formula = 'better ~ age + sex + vote + age:vote')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 


# R-squared for this model is 0.076 meaning that we have now explained around 7.6% of the variation in y, i.e., less than in our first model.

# ### RMSE
# 
# We don't have RMSE (root mean squared error) in our summary table, but we can call the MSE from the larger results structure, and get its square root as follows:

# In[5]:


reg_results.mse_resid**0.5


# We could compare the RMSE for this regression model to the RMSE we calculated when we only had a single explanatory variable, age (which we did by hand in the section on conditional distributions)
# 
# With only age used as an explanatory variable, RMSE was a bit higher, 2.50
# 
# * What does this suggest about spread of values around the regression line?

# ## Checking regression assumptions
# 
# In Python, we can also examine the regression assumptions. We can explore:
# 
# * whether the data are suitably linear
# * whether there is heteroskedasticity in the residuals
# * whether the residuals are normally distributed
# 
# For now, let's just take a look at the last of these three assumptions and plot a histogram of the residuals:

# In[6]:


sns.histplot(reg_results.resid)


# The residuals look roughly normally distributed. It looks like the normality assumption has been met

# In[ ]:




