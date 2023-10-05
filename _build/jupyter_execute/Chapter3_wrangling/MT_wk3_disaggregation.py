#!/usr/bin/env python
# coding: utf-8

# # Data Disaggregation
# 
# **Disaggregation** means describing or plotting data separately for different categories of individuals.
# 
# As we saw in the first lecture of the series, data in a single dataset can arise from different causal processes, for example:
# * The distribution of age at death in 1840 includes a set of deaths caused by infant/child mortality, and a set caused by old age
# * The distribution of reaction times in a psychological experiment may include a mixture of 'true' responses, false starts, and missed trials
# 
# *Disaggregating* data so that we are reporting statistics separately for these different groups is an important part of describing and analyzing data. For example:
# * We would like to report the mean reaction time for each condition of our psychological experiment based on 'true' responses, not including missed trials, which contribute a lot of noise to our estimate of the mean.
# 
# 
# Disaggregation becomes even more important when we think about making predictions based on data. For example:
# * If a patient presents with chest pain, is it more likely to be indigestion or a heart attack? The answer to this question partly depends on the age of the patient (heart attacks are much less likely in young patients), BUT that is different again for men and women.
# 
# 
# #### Equality
# 
# If a dataset includes a majority and minority group (for example, if the dataset consistes of more men than women, or more white people than black people), then failure to disaggregate data results in findings being biased towards the majority group
# 
# * For example, shockingly, <a href="https://www.theguardian.com/society/2021/nov/11/black-women-uk-maternal-mortality-rates">black women are four times more likely to die in childbirth<a> than white women in the UK, a statistic that was long un-remarked because data on maternal outcoems were not routinely disaggregated by race
# 
#     
# #### Disaggregation skills
#     
# Working out  which categories of data should be presented in disaggretgated form is a skill that you will learn through practice. Too little disaggregation obbscured important group differences or retains noise that could be removed; but too much disaggregation can result in an ocean of graphs and statistics that makes it hard to see the big picture.
# 
# In this section we will look at disaggregation in the context of the heart attack dataset.    
#     
# ### Set up Python Libraries
# 
# As usual you will need to run this code block to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import seaborn as sns
sns.set_theme(style='white')
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ### Import a dataset to work with
# 
# Let's look at a fictional dataset containing scores on English and Maths tests for 150 children.

# In[2]:


hospital=pd.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(hospital)


# #### Clean the data
# 
# We have reloaded the dataframe from the .csv file, so we need to re-implement the data cleaning steps we already decided were necessary:

# In[3]:


hospital.replace(9999, np.nan, inplace=True)
hospital.AGE.replace(774, np.nan, inplace=True )
hospital.describe() # check it worked


# ## Age vs Sex
# 
# Is the age distribution of heart attack patients the same regardless of sex?
# 
# Let's find out by plotting the age distribution separately for men and women:

# In[4]:


sns.kdeplot(data=hospital, x='AGE', hue='SEX', fill=True) 
plt.show()


# **Note-**
# * More men had heart attacks than women
# * The female patients tend to be older.
# 
# **Think**
# 
# A 40 year old patient presents with chest pain. It could be a heart attack or it could be indigestion. The doctor needs to decide the likely cause. Does it matter whether the patient is a mman or a woman?

# ### Length of stay
# 
# Let's plot the distribution of Length of Stay in hospital:

# In[5]:


sns.histplot(data=hospital, x='LOS', bins=range(0,40))
plt.show()


# **Note-**
# 
# There is something unusual here - the dataset is bimodal, with a large number of people staying just one day in hospital.
# 
# Often a bimodal distribution is a hint that data the data distribution is a imxture of data arising from two causes. In other words, we suspect the length of stay data could be meaningfully disaggregated.
# 
# If we disaggregate these by the categorical variable <tt>DIED</tt>, we can get a clearer picture what happened:
# 

# In[6]:


sns.histplot(data=hospital, x='LOS', hue='DIED', bins=range(0,40))
plt.show()


# **Note-**
# 
# People who sadly died from their heart attack tended to have short stays in hosiptal, with many dying on the same day they were brought to hospital.
# 
# For those who eventually survived, it was more typical to stay in hospital for 7-10 days.

# ## Mortality by sex
# 
# At first glance, female patients are much more likely to die than males:

# In[7]:


sns.barplot(data=hospital, y='DIED', x='SEX')
plt.ylabel('proportion who died')
plt.show()


# Is this due to difference in severity of heart attacks by sex, or perhaps differences int he effectiveness of treatment?
# 
# Probably not. We noticed earlier that the female patients were older than the males, and it is reasonable to wonder whether younger patients are more likely to survive.
# 
# It turns out this is true, younger patients are more likely to survive. We can see this clearly by plotting the proportion who died at each age
# 
# * This is a plot of mortality **conditional** upon age
# * If you are interested you can have a look at the syntax to produce this graph, but you won't be required to reproduce it

# In[8]:


plt.figure(figsize=(10,2))
plt.ylabel('Proportion Died')
sns.kdeplot(data=hospital, x='AGE', hue='DIED', multiple='fill', legend=False)

plt.tight_layout()
plt.show()


# If we plot mortality conditional upon age disaggregated by men and women, we can see that across all ages men are actually omre likely to die than women; the higher overall omrtality for women is explained by the presence of more older women in the sample (which in turn probably reflects the fact that women have longer life expectany than men).

# In[9]:


plt.figure(figsize=(10,4))

plt.subplot(2,1,1)
plt.title('Men')
plt.ylabel('Proportion Died')
sns.kdeplot(data=hospital.query('SEX == "M"'), x='AGE', hue='DIED', multiple='fill', legend=False)

plt.subplot(2,1,2)
plt.title('Women')
plt.ylabel('Proportion Died')
sns.kdeplot(data=hospital.query('SEX == "F"'), x='AGE', hue='DIED', multiple='fill', legend=False)

plt.tight_layout()
plt.show()


# ### Conclusion
# 
# You can learn a lot by disaggregating data!
# 
# The process of breaking data down to find evidence of different undelying distributions and relationships between variables is at the core of what a good data scientist, or indeed a research scientist, does.
# 

# In[10]:


hospital.AGE.corr(hospital.LOS, method='pearson')


# In[ ]:




