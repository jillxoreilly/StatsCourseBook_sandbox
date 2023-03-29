#!/usr/bin/env python
# coding: utf-8

# # Tutorial exercises
# 
# In the tutorial you will be analysing data (real but edited) from the 2021 General Social Survey from the USA.  The General Social Survey is a regular survey of the population of the United States that gathers information on people’s opinions. The sample is intended to be representative of the adult population. The outcome variable of interest (‘afraid’) is whether people feel afraid to walk in their neighbourhoods at night. The question wording was as follows: "Is there any area around your home--that is, within a mile--where you would be afraid to walk alone at night?" The answer options are yes (1) or no (0). (Some people also answered “don’t know” but these are set to missing).
# 
# The $x$ variables are as follows
# 
# * Sex (male, female)
# * Age (in years)
# * Race of respondent (white, black, other)
# * Born (whether respondent was born in the USA, yes or no)
# * Raclive (a binary variable indicating whether the neighbourhood is racially mixed).
# * Educ (education measured in years of education, where more years assumes higher educational qualifications)
# * Income (an ordinal variable of household income, where higher values mean higher incomes. Treat as continuous for this analysis)
# 
# 
# ### Set up Python libraries
# 
# Copy an appropriate code cell below, and run it, to import the relevant Python libraries
# 

# In[1]:


# your code here


# ### Import and view the data
# 
# The data are in file fear.csv - download them and import them as a dataframe called `fear`

# In[2]:


# your code here


# ### Designing the model
# 
# Before running your first logistic regression model, think about your expectations here. 
# 
# * Would you expect men or women to be more afraid of walking in their neighbourhoods at night? 
# * And would you expect older or younger people to feel more afraid? 
# 
# Let’s test these associations between age and sex with fear of walking in neighbourhoods. Run a logistic regression model with $y$ = afraid, $x$ = sex + age.
# 

# In[3]:


# your code here to run the logistic regression


# ### Interpret the output. 
# 
# * Which coefficients are statistically significant? 
# * Is the direction of effect as expected? 
# * Find the p-value for the log-likelihood ratio. 
# * Is this model statistically significant compared to the baseline model?
# 
# 

# < your comments here >

# 
# ### Make predictions
# 
# Compute the predicted probability that a 65-year-old woman reports feeling afraid. 

# In[4]:


# your code here


# ### Control variables
# 
# Run a second logistic regression model. Keep age and sex in the model, and add race, born, raclive. and educ. (We are treating educ as a continuous variable). Print the coefficients as odds ratios.

# In[5]:


# your code here


# ### Interpretation
# 
# Find the odds ratio for each preditor variable

# In[6]:


# your code here


# Make a few notes on the findings using the odds ratios. How would you report the size of the effect using the odds ratios?

# Make a few notes on the findings using the odds ratios. How would you report the size of the effect using the odds ratios

# < your comments here >

# How good is this second model? Check the classification table based on predicted probabilities. 

# In[7]:


# your code here for the classification table


# ### Control for income
# 
# Run a third logistic regression model adding a control variable for income. Request the output in odds ratios again

# In[8]:


# Your code here


# Interpret the results carefully. Do any of your conclusions change now that we are controlling for income? (Compare the coefficients in model 2 and model 3). Why do you think this might be?

# < your comments here >

# ### Extra exercise: effective sample size
#     
# Look back at the sample size in each of the three logistic regression models. 
# 
# Why do you think the sample size is changing each time? 
# 
# * `statsmodels` omits rows of the dataframe which have NaN for any predictor variable. Each time we change the set of predictor variables used, the number of rows excluded changes
# 
# If you want to keep the same sample throughout all of the analysis, we can save the “effective sample” from model 3 with the following code:
# 

# In[9]:


# code to save effective sample size


# Now re-run model 1 and check the sample size. Are there any changes in coefficient estimates once you have restricted the analysis to the effective sample?

# In[10]:


# your code here to run model 1 on the effective sample


# In[ ]:




