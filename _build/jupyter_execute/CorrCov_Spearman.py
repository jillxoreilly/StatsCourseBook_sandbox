#!/usr/bin/env python
# coding: utf-8

# # Spearman's Rank Correlation

# ## Climate Example
# 
# We will again use the a dataset containing carbon emissions, GDP and population for 164 countries (data from 2018).
# 
# These data came from <a href="https://ourworldindata.org/">Our World in Data</a>, a fabulous Oxford-based organization that provides datasets and visualizations addressing global issues.
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
sns.set_theme() # use pretty defaults


# ### Load and inspect the data
# 
# Load the data from the file CO2vGDP.csv.

# In[2]:


CO2vGDP = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/CO2vGDP.csv')
display(CO2vGDP)


# 
# 
# We noted previously that our climate dataset is not suitable for a 'normal' Pearson's correlation because it has one of the three freatures that violate the assumptions of Pearson's correlation:
# 
# <ul>
#     <li> Non-Straight-Line relationship between x and y
#     <li> Heteroscedasticity
#     <li> Outliers
# </ul>
# 
# In this case the problem was heteroscedasticity
# 
# 
# ### Spearman's Rank Correlation
# 
# We therefore use a rank-based form of correlation called Spearman's rank correlation coefficient $r_s$, which does not rely on the same assumptions as Pearson's correlation.
# 
# $r_s$ can be calculated using the same built-in function <tt>pandas.df.corr()</tt>:

# In[3]:


CO2vGDP.corr(method='spearman')


# The 'methods' available are:
# 
# <ul>
#     <li>Pearson ('normal' correlation), 
#     <li>Spearman (rank based) and 
#     <li>Kendal (categorical; rarely used).     
# </ul>
#     
# The default (the method used if no method is specified) is Pearson - we can see this by comparing the results with method specified as Pearson and no method specified:

# In[4]:


CO2vGDP.corr(method='pearson')


# In[5]:


CO2vGDP.corr()


# ### The equation
# 
# Let's check our understanding by calculating Spearman's correlation coefficient oursleves.
# 
# The equation is:
#     
# $$ r_s = 1 - 6 \sum{\frac{d^2}{n(n^2 - 1)}} $$
# 
# ... where d is the difference in ranks between paired datapoints.
# 
# Let's walk that through.
# 
# First, we create new columns containing the rank of each datapoint - 
# <ul>
#     <li>the lowest GDP will have rank 1 and the highest will have rank 165
#     <li>the lowest CO2 emissions will have rank 1 and the highest will have rank 165
#     <li>the GDP aand CO2 ranks for each country need not match, but if GDP and CO2 are correlated, 
#     <li>high-ranked countries for GDP should also be high-ranked for CO2
# </ul>

# In[6]:


CO2vGDP['CO2_rank'] = CO2vGDP['CO2'].rank()
CO2vGDP['GDP_rank'] = CO2vGDP['GDP'].rank()

# We can see these most clearly if we sort the dataframe before displaying
display(CO2vGDP.sort_values(by='CO2'))


# You can see that countries with low ranks for CO2 do tend to have low ranks for GDP.
# 
# Let's plot the data, and the ranked data, on scatterplots. You can see that the ranked data do not have the same heteroscedasticity issue as the data themselves.

# In[7]:


plt.subplot(1,2,1)
sns.scatterplot(data=CO2vGDP, x='CO2', y='GDP')

plt.subplot(1,2,2)
sns.scatterplot(data=CO2vGDP, x='CO2_rank', y='GDP_rank')

plt.subplots_adjust(wspace = 0.5) # shift the plots sideways so they don't overlap


# To continue the process of applying the equation, we make a new column containing the difference of ranks:

# In[8]:


CO2vGDP['d'] = CO2vGDP['CO2_rank']-CO2vGDP['GDP_rank']


# ... and apply the formula:

# In[9]:


n = len(CO2vGDP)

r_s = 1 - 6*sum(CO2vGDP['d']**2)/(n*(n**2 - 1))
print('r = ' + str(r_s))


# Ta-daa! This should match the value from the built in function.
# 
# ### Spearman = Pearson on Ranks
# 
# The equation for Spearman's $r_s$ looks pretty weird, doesn't it? What is that 6 doing there?!
# 
# I can't tell you the derivation (although I believe I did once know it), but I can tell you a fun thing.
# 
# Spearman's $r_s$ is exactly the same value as Pearson's $r$ claculated on the ranks.
# 
# Let's try it!

# In[10]:


# make a new dataframe with only ranks
CO2vGDP_ranks = CO2vGDP[['CO2_rank','GDP_rank']]
display(CO2vGDP_ranks)


# In[11]:


# Calculate **Pearson's** correlation on the ranks
CO2vGDP_ranks.corr(method='pearson')


# Yep, the correlation is 0.9138 - the exact same value as $r_s$

# In[ ]:




