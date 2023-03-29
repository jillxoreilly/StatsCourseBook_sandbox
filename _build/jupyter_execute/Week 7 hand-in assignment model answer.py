#!/usr/bin/env python
# coding: utf-8

# # Week 7 Assignment model answer

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


# In[2]:


## Part 1: loading data and introduction


# In[3]:


happy = pandas.read_csv('data/happy.csv')
happy


# 1) INTRODUCTION: In this research report I will investigate whether people's perception of their position in society is associated with their happiness. My hypothesis is that people who perceive themselves as higher in society are happier. To investigate this, I will use survey data and regression analysis.

# In[4]:


## Part 2: Checking for sample size and missing values
# Change 99s to NaN.


# In[5]:


happy[happy==99]=np.nan
happy.info()


# 2) DATA AND METHODS: The data were collected with an online survey conducted by YouGov in 2019. The data are intended to be representative of the UK population. The survey included questions about the respondents' happiness, their perception of social standing, and demographic and socioeconomic details about the respondent. The outcome variable in this analysis is 'happy' which is measured on a scale of 0-10. The explanatory variable is 'ladder' which is measured on a scale of 1-11. As marital status, age, income, and working status have known associations with happiness, I will treat these as potential confounders and include them as control variables in the regression analysis. The aim is to understand the relationship between perceived social standing and happiness, after controlling for these potential confounders. There were 1000 partipants in the study, but I changed values of 99 to "not a number" for ladder (n = 50). In addition, there are two missing values for marital status and 253 missing values for income.

# In[6]:


## Part 3 results
# First give mean and standard deviation of happy
print('mean happiness = ' + str(happy['happy'].mean()))
print('sd of happiness = ' + str(happy['happy'].std()))
# And the mean and standard deviation of ladder
print('mean of "ladder" = ' + str(happy['ladder'].mean()))
print('sd of "ladder" = ' + str(happy['ladder'].std()))


# In[7]:


# First regression model
reg_formula = sm.regression.linear_model.OLS.from_formula(data = happy, formula = 'happy ~ ladder')
reg_results = reg_formula.fit()

# Get RMSE
RMSE = reg_results.mse_resid**0.5
print('RMSE for first model = ' + str(RMSE))

# View regression results
reg_results.summary() 


# In[8]:


# Second regression model
reg_formula = sm.regression.linear_model.OLS.from_formula(data = happy, formula = 'happy ~ ladder + marital + age + income + work')
reg_results = reg_formula.fit()

#Get RMSE
RMSE = reg_results.mse_resid**0.5
print('RMSE = ' + str(RMSE))

# View regression results
reg_results.summary() 


# 3) RESULTS: The mean level of happiness in the sample is 6.173 with a standard deviation of 2.369. The mean level of perceived social standing is 6.296 and the standard deviation is 1.634. The first regression model shows an intercept of 2.9733 which can be interpreted as the average level of happiness when social ladder is at zero. The slope for ladder is 0.5035 suggesting that for every unit increase in social standing, happiness increases by a little over half a point. The standard error for the slope is 0.044 and the slope is thus statistically significantly different to zero. The R-squared for this regression model is 0.121 suggesting that ladder can explain 12.1% of the variation in happiness. The RMSE of 2.220 suggests that there is a considerable spread of values around the regression line. 
# 
# Model two includes the control variables which show that are no statistically significant differences in happiness by martial status, or by income group, or by age, as the p-values are all above 0.05 for these variables. There are, on the other hand, statistically significant effects by working status. People with the working status "other" have happiness 0.9374 points higher than people who are employed (the reference category which is omitted from the regression table), and people who are unemployed have happiness 0.6511 points lower than the employed. Once controlling for these variables, the effect of perceived social standing continues to have a statistically significant effect on happiness. The slope coefficient for ladder is 0.4200 in model 2, so somewhat reduced compared to model 1. Model 2 has an R-squared of 0.177 suggesting that we are now explaining 17.7% of the variation in happiness. The RMSE has correspondingly decreased to 2.134. Although this second model is better fitting than the first, there is still considerable variation around the regression line.

# In[9]:


# Part 4 Plot
# Fitted scatter
reg_formula = sm.regression.linear_model.OLS.from_formula(data = happy, formula = 'happy ~ ladder + marital + age + income + work')
reg_results = reg_formula.fit()
# View regression results
reg_results.summary() 
sns.regplot(data=happy, x='ladder', y='happy', scatter=False)


# 4) PLOT: The regression plot shows the fitted values of ladder on happy. There is a strong positive relationship between ladder and happy. [Other options would be to show an interaction plot here].

# 5: LIMITATIONS: There are several limitations to this study. First, as the R-squares are on the low side, there is still a lot of unexplained variation in happy. There is a lot of spread of values around the regression line. A major limitation relates to causality. We have no way of knowing from the data if high perceived social standing causes happiness or if happiness changes perceptions of social standing. Another study could collect overtime data, or run an experiment for understanding causality.

# 6) CONCLUSIONS: This research has shown, using regression analysis, that there is an association between perceptions of social standing with happiness. People who feel higher up in the social hierarchy also feel happier. This association holds even after controlling for age, marital status, working status and income. 

# In[ ]:




