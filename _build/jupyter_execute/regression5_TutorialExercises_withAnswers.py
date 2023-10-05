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


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### Import and view the data
# 
# The data are in file fear.csv - download them and import them as a dataframe called `fear`

# In[2]:


# your code here
fear=pandas.read_csv('data/fear.csv')
fear


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


# create the logistic regression model and fit it
logistic_model = smf.logit('afraid ~ sex + age', data=fear).fit()

# print out the summary table
logistic_model.summary()


# ### Interpret the output. 
# 
# * Which coefficients are statistically significant? 
# * Is the direction of effect as expected? 
# * Find the p-value for the log-likelihood ratio. 
# * Is this model statistically significant compared to the baseline model?
# 
# 

# The effect of sex and age are significant:
# 
# * Males are less likely to be afraid than females (p<0.0005)
# * older people are less likely to be afraid (negative log odds) - (p<0.0005)
# 
# 
# The model is statistically significaant (model LLR p-Value is $1.8 * 10^{-42}$)

# 
# ### Make predictions
# 
# Compute the predicted probability that a 65-year-old woman reports feeling afraid. 

# In[4]:


vals = dict(sex='female', age=65)

# Code for calculating predicted probability
logistic_model.predict(vals)


# probability she feels afraid is 39%

# ### Control variables
# 
# Run a second logistic regression model. Keep age and sex in the model, and add race, born, raclive. and educ. (We are treating educ as a continuous variable). Print the coefficients as odds ratios.

# In[5]:


# create the logistic regression model and fit it
logistic_model = smf.logit('afraid ~ sex + age + race + born + raclive + educ', data=fear).fit()

# print out the summary table
logistic_model.summary()


# ### Interpretation
# 
# Find the odds ratio for each preditor variable

# In[6]:


# convert log odds to odds ratios
np.exp(logistic_model.params)


# Make a few notes on the findings using the odds ratios. How would you report the size of the effect using the odds ratios?

# * males are 59% less likely to be afraid than females (odds ratio = 0.41)
# * people whose race is not bblack are less likely to be afraid - for other, 8% less likely; for white, 21%
# * people who were born in the USA are 28% less likely to be afraid
# * people in racially mixed neighbourhoods are 127% more likely to be afraid
# * for each year of age, people are 1% less likely to be afraid
# * for each year of eductaion, people are 3% less likely to be afraid

# How good is this second model? Check the proportion of cases correctly classified.

# In[7]:


# Get predicted values for each row of the dataframe
yhat = logistic_model.predict(fear[['sex','age','race','born','raclive','educ']])

# add column to the dataframe with the probability, and another with the binary prediction
fear['yhat']=yhat
fear['prediction']=(yhat>0.5)

# work out proportion correctly classified
# a participant (row) is correctly classified if columns 'evolved' and 'prediction' match
correct = fear[(fear['afraid']==fear['prediction'])]

len(correct)/len(fear)


# 65% are correctly classified

# ### Control for income
# 
# Run a third logistic regression model adding a control variable for income. Request the output in odds ratios again

# In[8]:


# create the logistic regression model and fit it
logistic_model = smf.logit('afraid ~ sex + age + race + born + raclive + educ + income', data=fear).fit()

# print out the summary table
logistic_model.summary()

# convert log odds to odds ratios
np.exp(logistic_model.params)


# In[9]:


sns.kdeplot(data=fear, x='income', hue='race')
plt.show()


# Interpret the results carefully. Do any of your conclusions change now that we are controlling for income? (Compare the coefficients in model 2 and model 3). Why do you think this might be?

# HIgher incomes mean you are less likely to be afraid
# 
# When income is included as a control variable, the effects of education and race are reduced, suggesting these effect is partly 'explained away' (mediated) by income (ie people who are educated and non-black have higher incomes and this partly explains why they are less likely to be afraid)
# 
# The effects of being Male, born in the USA and 'raclive' are increased when income is included as a control variable.  
# 
# We can understand this better with the help of plots. 
# 
# Males are less afraid than females at all income levels, but males are more likely to have high incomes (which also makes you less afraid). Therefore when income was not taken into account, the benefit of being male was 

# In[10]:


sns.lmplot(data=fear, x='income', y='afraid', hue='sex', logistic=True)
plt.show()


# In[11]:


sns.kdeplot(data=fear, x='income', hue='sex')
plt.show()


# In[12]:


sns.lmplot(data=fear, x='income', y='afraid', hue='raclive', logistic=True)
plt.show()


# In[13]:


sns.kdeplot(data=fear, x='income', hue='raclive')
plt.show()


# In[ ]:




