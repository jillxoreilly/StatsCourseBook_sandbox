#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises - regression 6

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### a. Load and inspect data

# In[2]:


digital = pandas.read_csv('data/digital.csv')
digital


# ### b. Replace 999 with NaN

# In[3]:


# locate the offending items
np.sum(digital==999)


# In[4]:


# replace them
digital.loc[digital.skills==999,'skills']=np.nan
digital.loc[digital.daily==999,'daily']=np.nan

# check they've gone
np.sum(digital==999)


# In[5]:


# check Nans are there instead
digital.isna().sum()


# ### c. Find outlier in `eduyrs`

# In[6]:


# sort the values to find the outlier
digital.eduyrs.sort_values()


# In[7]:


sns.histplot(data=digital, x='eduyrs')


# In[8]:


# replace it with NaN
digital.loc[digital.eduyrs>100,'eduyrs']=np.nan

# check it's gone
digital.eduyrs.sort_values()


# **Note** we were informed that there was *one* unrealistic value to replace, hence sorting (to find the min and max values) is a good approach
# 
# If we didn't know how many outliers there might be, I would have checked for them by plotting the data instead

# ### d. Create a bar plot to show differences in mean digital skill level, by income. Comment on the results.

# In[9]:


# use sns barplot; put bars in sensible order so pattern can be perceived
sns.barplot(data=digital, x='inc4', y='skills', order=['Lowest','Mid-low','Mid-high','Highest'])


# **Comments** Digital skills increase as income increases

# ### e. Multiple linear regression analysis
# 
# Examine the association between digital skills $y$ and the following $x$ variables: age, eduyrs, daily and inc4.

# In[10]:


# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = digital, formula = 'skills ~ age + eduyrs + daily + C(inc4) ')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 


# ### Interpretation
# 
# **Mention the size, sign, and statistical significance of the slope coefficients.**
# 
# There is a negative effect of **age** such that for each additional year of age, skills decreased by 0.073 points (beta = -0.073). This was statistically significant (p<0.0005)
# 
# There is a positive effect of **eduyrs** such that for each additional year of education, skills increased by 0.25 points (beta = 0.25). This was statistically significant (p<0.0005)
# 
# There is a positive effect of **daily** internet use, such that fthose who used the internet daily had skills on average 2.9 points higher than those who did not (beta = 2.9). This was statistically significant (p<0.0005)
# 
# There is a positive effect of **income** on skills; all income catcgories had significantly higher mean skills that the **Lowest** income group, with skills increasing as income increased. People in the Mid-Low, Mid-High and Highesy income groups had on average skills 0.42, 1.0 and 1.4 points higher than those in the lowest groups (betas are 0.42, 1.0 and 1.4 respectively).  All differences from the reference category (Lowest) were statistically significant (p<0.0005)
# 
# **Report the R-squared and interpret.**
# 
# The adjusted R^2 is 0.505, meaning the model explains 50.5% of the varianbce in idigital skills; this is a pretty good model although some sources of variation remain uncaptured

# ### f. Causality
# 
# How good is the evidence, from this model, that the relationship between the daily internet use
# and digital skills is a causal relationship?
# 
# Although there is a strong relationship between daily internet use and high digital skills, we cannot determine the direction of causality - maybe those with poor digital skills avoid internet use, maybe those who don't have access to the internet have poor digital skills as a consequence, or maybe there is a feedback loop
# 
# The data are froma  cross sectional survey. To determine causality we should use an experiment in which people with low skills are randomly assigned to use the internet daily (or not). Or we could use a natural experiment in which some people don't have access to the internet for reasons outside their control. 

# ### g. Logistic regression
# 
# Using the variable ‘daily’ as the outcome variable, run a logistic regression model. Include the
# following 𝑥 variables: age, eduyrs, inc4, and home

# In[11]:


# create the logistic regression model and fit it
logistic_model = smf.logit('daily ~ age + eduyrs + inc4 + home', data=digital).fit()

# print out the summary table
logistic_model.summary()


# **i) Which of the explanatory variables are statistically significant?**
# 
# The effects of all the explanatory variables are significant (p<0.0005)
# 
# **ii) Report the odds ratios for each of the explanatory variables. Explain in words how to
# interpret the odds ratio for home**

# In[12]:


# obtain odd ratios by exponentiating log odds
np.exp(logistic_model.params)


# The odds ratios for each explanatory variable are given in the table above
# 
# For `home` the odds ratio is 15.6, meaning that those who have an internet connection at home are 15.6 times more likely to use the internet daily than those who do not

# **iii) What is the predicted probability of daily internet use for a person who is aged 75,
# has 12 years of education, a low income, and no internet access at home?**

# In[13]:


vals = dict(age=75, eduyrs=12, inc4='Lowest', home='No')

# Code for calculating predicted probability
logistic_model.predict(vals)


# The predicted probability of daily internet use for this person is 4.3%

# ### h) Model log likelihood
# 
# Looking back at the model in g), say whether the log-likelihood of the fitted model is a significant
# improvement compared to the null model.
# 
# Yes - as the LLL p-value is <0.0005

# In[ ]:




