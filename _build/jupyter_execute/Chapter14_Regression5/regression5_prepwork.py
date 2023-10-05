#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression in Python
# 
# <img src="https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/images/regression5_darwin.jpg" width=30% >
# 
# **Example:** The General Social Survey is a regular survey of the population of the United States that gathers information on people’s opinions since 1972. 
# 
# Here we use data from 2018, when the following question was put the respondents: “Human beings, as we know them today, developed from earlier species of animals. True or false?” 
# 
# In this analysis, $y$ = opinion about evolution (1 = true, 0 = false). 
# 
# We have three $x$ variables for the analysis: 
# 
# * age (measured in years), 
# * political ideology (measured from 1 = extremely conservative to 7 = extremely liberal, which we treat as continuous here), and 
# * whether the participant studied science at college (yes, no). 
# 
# Before we start, have a think about these $x$ variables: which direction do you expect the relationship to go? E.g., will older or younger people be more likely to answer “true”?
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


evolution = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/evolution.csv')
evolution


# Which column is which variable, from the list above?
# 
# ## Logistic regression
# 
# We ask Python to run a logistic regression, predicting people's view on evolutions (True or False) based on their age, political views and whether they studied science at college;

# In[3]:


# create the logistic regression model and fit it
logistic_model = smf.logit('evolved ~ age + polviews + colsci', data=evolution).fit()

# print out the summary table
logistic_model.summary()


# The standard model output looks rather like the output table from linear regression. 
# 
# The coefficients in the column “coef” are in log odds. 
# 
# We can interpret these coefficients in the following way: 
# 
# * as people get older they are less likely to agree that humans evolved from earlier species (hence the negative coef)
# * as people’s political views get more liberal they are more likely to agree (hence the positive coef)
# * the log odds for studying science at college is also positive; however, it is not statistically significant
# 
# Because logs odds are rather hard to interpret intuitively (for most of us anyway), we can convert them into odds ratios by exponentiating them, to help with interpretation. 
# 

# In[4]:


# logistic_model.params contains the beta coefficients for each explanatory variable

# use numpy's exp function to exponentiate them:
np.exp(logistic_model.params)


# ### Interpreting the odds ratios
# 
# Remember the practice session with logs above? The same principles apply here. 
# 
# Odds of 1 relate to a 50/50 probability, which we can interpret in a logistic regression model as no effect (i.e., the $x$ variable is not associated with a higher or lower probability of the outcome occurring). 
# 
# Positive log odds become odds ratios with a value greater than 1, and negative log odds become odds ratios with a value below 1. 
# 
# Here, we can interpret the model output as follows: 
# 
# * The odds ratio of 1.47 for political views suggests that for each additional point along the scale from conservative to liberal is associated with a 1.47 times greater likelihood of agreeing that humans evolved from earlier species. 
# 
# The output from python provides confidence intervals too. The 95% confidence intervals for the odds ratio are 1.29 – 1.68. 
# 
# * For age, the odds ratio tells us that for each additional year the odds of answering ‘true’ are 0.02 (or 2%) lower (using 1-0.98 for the effect size). Here I will not interpret ‘colsci’ as it is not statistically significant. 
# 
# We know this from the p-value but also because the confidence intervals include 1. Note the contrast with the original model with log odds in this regard).
# 
# ### Making a prediction
# 
# Python will compute a predicted probability for us. 
# 
# Let’s find out the predicted probability of believing in evolution for a 50-year-old with a score of 5 on the conservative scale, who did not study science at college.
# 
# The syntax for this is a bit faffy, as we need to use a dictionary (dictionaries in Python are actually really useful, but we haven't used them on this course so don't worry too much about it)
# 

# In[5]:


vals = dict(age=50, polviews=5, colsci='no')

# Code for calculating predicted probability
logistic_model.predict(vals)


# The probability this person believes in evolution is 0.62 or 62%
# 
# * Try plugging in some different values - what about yourself or your family members?

# ## Assessing the model
# 
# Just as we did in linear regression, we can obtain predicted values for the model for the people in the original dataset - that is for each person in the original dataframe, we get the model's predicted probability they believe in evolution (we also know the ground truth, whether they replied that they do believe in evolution, or not)
# 
# The predicted values can help us to understand how well our model did. They take a value between 0 and 1 and can be treated as a predicted probability of each individual answering ‘true’ to the survey question, given the $x$ variables that we have modelled
# 

# In[6]:


# Get predicted values for each row of the dataframe
logistic_model.predict(evolution[['age','polviews','colsci']])


# We can compare how well the model prediction matches the observed data byb classifying (using Pr(y=1)>0.5 as cut-off) which cases would be predicted as true or false, and comparing to whether the observed value was true or false. 
# 

# In[7]:


# Get predicted values for each row of the dataframe
yhat = logistic_model.predict(evolution[['age','polviews','colsci']])

# add column to the dataframe with the probability, and another with the binary prediction
evolution['yhat']=yhat
evolution['prediction']=(yhat>0.5)

# work out proportion correctly classified
# a participant (row) is correctly classified if columns 'evolved' and 'prediction' match
correct = evolution[(evolution['evolved']==evolution['prediction'])]

len(correct)/len(evolution)


# In[ ]:





# Overall, 65% of the cases were correctly classified by this model
# 
# While a linear regression uses the method of Ordinary Least Squares (OLS) to fit the model, logistic regression uses the *Maximum Likelihood Estimation* method. This method uses the values of the model parameters that are most consistent with the observed data, so that with the intercept and slope values estimated in the model, the observed data have a greater chance of occurring than with any other estimated values (See Agresti, Chapter 5). 
# 
# The log-likelihood is based on summing the probabilities of the observed and actual outcomes and tells us how much unexplained information there is after the model has been fitted (thus analogous to residual sum of squares in linear regression). The model log likelihood can be found in the model summary table.
# 
# Like in linear regression $R^2$, we use a ‘baseline’ model with no $x$ variables (predicting the outcome that occurs most often), and compare the log-likelihood after adding the $x$ variables. The likelihood-ratio test, (in python the LLR $p$-value) produces a $p$-value so that we can tell if our model is statistically significant. Low p-values (below 0.05) tell us that the model with the $x$s is significantly better at predicting the outcome than the baseline model. 

# In[ ]:




