#!/usr/bin/env python
# coding: utf-8

# # ANOVA and Kruskal-Wallis in Python
# 
# We’ll use the data from the chimps examples to demonstrate the python code. First, as usual, we’ll import the relevant packages and import the data as a `.csv` file. 
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


chimps=pandas.read_csv('data/chimps.csv')
chimps


# Have a look at the data
# 
# Each row is a 'participant' (a chimp). 
# 
# We have the following information on each chimp;
# * ID number
# * Experimental group (who did the chimp see yawning?)
# * yawns (number of yawns produced)
# * age3 (age of the chimp, in three categories)
# 
# 
# What is the dependent variable? What is the independent variabble? What are the control variables?
# 
# ## Running the ANOVA
# 
# We want to run an ANOVA to test whether the species of the yawner affects the number of yawns produced by the chimp.
# 
# Here is some code to do so:

# In[3]:


# First we create the ANOVA model:
chimps_lm = smf.ols('yawns ~ group', data=chimps).fit()

# Then output the ANOVA table
table = sm.stats.anova_lm(chimps_lm, typ=2) 
print(table)


# The python output confirms our longhand example above. The p-value is 0.0003. There is a statistically significant difference in yawn rates between the groups.
# 
# ### Control variable
# 
# We can add a control variable in a “two-way ANOVA”. Here we want to control for age which is a categorical variable of the chimp’s age: young, middle-aged, and old

# In[4]:


# First we create the ANOVA model:
chimps_lm = smf.ols('yawns ~ group + age3', data=chimps).fit()

# Then output the ANOVA table
table = sm.stats.anova_lm(chimps_lm, typ=2) 
print(table)


# The results show that the experimental treatment group is statistically significant (p=0.0002) but age is (just) not statistically significant (p=0.0533). 

# ### Interaction terms
# 
# ANOVA can also handle interaction terms (as we explored with Regression Analysis last term).
# 
# Let's look at whether there is an interaction between `group` and `age3` (this would mean that the yawning behaviour of young and old chimpanzees was differently affected by the species of the yawner)

# In[5]:


# First we create the ANOVA model:
chimps_lm = smf.ols('yawns ~ group + age3 + group:age3', data=chimps).fit()

# Then output the ANOVA table
table = sm.stats.anova_lm(chimps_lm, typ=2) 
print(table)


# The interaction is not statistically significant (p=0.4961), which we can interpret to mean that the effect of the treatment group was the same for chimps of different ages. 
# 
# ## Kruskal-Wallis Test

# We can also run a Kruskal-Wallis Test in python, using a function from `scipy.stats` called `kruskal`
# 
# Here is the syntax - remember the Kruskall-Wallis test is similar to a one-way ANOVA, in that it tests for the effect of only one (categorical) varialbe, no control variables or interactions:

# In[6]:


# annoyingly, we have to give stats.kruskall each group's data as a separate series

stats.kruskal(chimps[chimps.group == 'Baboons']['yawns'], 
              chimps[chimps.group == 'Control (human, no yawn)']['yawns'],
              chimps[chimps.group == 'Familiar humans']['yawns'],
              chimps[chimps.group == 'Unfamiliar humans']['yawns'],)


# The Kruskal-Wallis test produces an H-statistic of 12.894 and a p-value of 0.0049. It therefore gives the same result as the one-way ANOVA, suggesting a statistically significant difference between treatment groups in the chimp experiment.

# In[ ]:




