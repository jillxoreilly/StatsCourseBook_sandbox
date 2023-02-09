#!/usr/bin/env python
# coding: utf-8

# # Climate example

# ## Example
# 
# We will look at a dataset containing carbon emissions, GDP and population for 164 countries (data from 2018).
# 
# These data are adapted from a dataset downloaded from <a href="https://ourworldindata.org/">Our World in Data</a>, a fabulous Oxford-based organization that provides datasets and visualizations addressing global issues.
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
# Load the data from the file CO2vGDP.csv

# In[2]:


CO2vGDP = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/CO2vGDP.csv')
display(CO2vGDP)


# <b>Aside</b> - 
# I notice that the GDP values contain loads of decimal places which makes them hard to read. 
# Let's just round those:

# In[3]:


CO2vGDP['GDP']=CO2vGDP['GDP'].round()
display(CO2vGDP)


# It is easier to comapre the values now as the larger GDPs actually take up more space!

# ### Plot the data
# 
# Let's plot the data. A scatterplot is a good choice for bivariate data such as these.

# In[4]:


sns.scatterplot(data=CO2vGDP, x='GDP', y='CO2')
plt.xlabel('GDP: $/person/year')
plt.ylabel('CO2 emissions: tonnes/person/year')


# Let's find the UK on that graph:

# In[5]:


sns.scatterplot(data=CO2vGDP, x='GDP', y='CO2')
sns.scatterplot(data=CO2vGDP[CO2vGDP['Country']=='United Kingdom'], x='GDP', y='CO2',color='r') # see what I did there to plot the UK in red?
plt.xlabel('GDP: $/person/year')
plt.ylabel('CO2 emissions: tonnes/person/year')


# ### Calculate the correlation
# 
# We can calculate the correlation using the built in function <tt>pandas.df.corr()</tt>

# In[6]:


CO2vGDP.corr()


# Humph, population was included in my correlation matrix, which I didn't really want. 
# 
# The function <tt>pandas.df.corr()</tt> returns the matrix of correlations between all pairs of variables in your dataframe. 
# 
# This isn't a big problem in the current case, but if you had a big dataframe with many irrelevant columns, it would be an issue, because we don't want the reader to have to search through a huge correlation matrix to find the correlation we are interested in.
# 
# We have two options to avoid this - one is to create a new dataframe with only the columns you want to correlate, like this:

# In[7]:


CO2vGDP_reduced = CO2vGDP[['CO2','GDP']] # new dataframe has only columns 'CO2' and 'GDP'
CO2vGDP_reduced.corr()


# The other is to correlate just the two columns we want, rather than getting the whole correlation matrix:

# In[8]:


CO2vGDP['CO2'].corr(CO2vGDP['GDP'])


# ### Outliers
# 
# The correlation between GDP and C02 looks quite high, 0.79.
# 
# However, looking at our scatterplot, I can see a problem - there is one bad outlier with very high GDP and high CO2 emissions.
# 
# Any guesses what this country is? 
# 
# We can find out by sorting the dataframe by GDP:

# In[9]:


CO2vGDP.sort_values(by='GDP', ascending=False) # sort in descending order to put the richest country at the top


# It's Qatar - maybe not what you expected?

# ### Remove outlier
# 
# Let's exclude Qatar from our dataset and re-calculate the correlation.
# 
# We erase the values for Qatar data values for CO2 and GDP for Qatar to <tt>Nan</tt> but in this case, since they are not misrecorded but just unusual values, let's not do that, as we don't want to hide the data point.
# 
# Instead we conduct the correlation on the dataframe excluding Qatar:

# In[10]:


CO2vGDP[CO2vGDP['Country']!='Qatar'].corr()


# Hm, the correlation went down from $r$=0.79 to $r$=0.073 - lower but still strong
# 
# Here's a plot of the data with Qatar excluded

# In[11]:


sns.scatterplot(data=CO2vGDP[CO2vGDP['Country']!='Qatar'], x='GDP', y='CO2')
plt.xlabel('GDP: $/person/year')
plt.ylabel('CO2 emissions: tonnes/person/year')


# We no longer have an obvious outlier, but we do have a problem, called heteroscedasticity
# 
# Heteroscedasticty is when the variance of the data in $y$ depends on the value in $x$. In this case, CO2 emissions are more variable for high income countries (which can be high- or low poluting) compared to low income countries
# 
# This property violates the assumptions of Pearson's correlation coefficient, so for these dataset we would be better off using Spearman's rank correlation coefficient, as explored in the next section.

# In[ ]:




