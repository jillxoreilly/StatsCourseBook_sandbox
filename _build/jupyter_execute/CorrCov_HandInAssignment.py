#!/usr/bin/env python
# coding: utf-8

# # Hand-in Assignment
# 
# You task is to produce a report for the Chair of Medicare (the organization that paid for the hospital stays of the patients in this dataset).
# 
# The Chair of Medicare wants to know what factors affect the cost of a hospital admission for heart attack.
# 
# Your report will summarise the distribution of costs and the factors that affect the cost of a hospital stay, using appropriate plots and descriptive statistics. 
# 
# This report should build on the Tutorial Exercises for session 3, BUT an important part of the task is to prepare a report (as if for presentation to a client, the Chair of Medicare), NOT just paste the tutorial exercises.
# 
# ## Instructions for completing this report
# 
# You will produce your report in the form of a a Jupyter notebook (you could modify this one or create a new one).
# 
# The notebook will contain text (to be read by the Chair of Medicare who is not familiar with Python code) and code blocks (showing transparently how you processed the data, in case someone in the Medicare Data Science Team wants to check or elaborate on the analysis).
# 
# You can add as many new blocks as you need to a notebook by clicking the + button in the toolbar at the top of the notebook viewer, then selecting the type (code or markdown, which is text) from the dropdown menu.
# 
# ### What your report should cover
# 
# Some suggested sections for the report are included in the <b>stub</b> notebook below.
# 
# ### What makes a good report
# 
# It should contain information useful to the Chair, and this should not be swamped by irrelevant information (ie, do not report every possible correlation and produce every possible graph, but focus on those you think are important)
# 
# The text blocks should be readable by a non statistically trained person, although they should contain key descriptive statistics
# 
# The text blocks should be supported by code blocks illustraing how you obtained the descriptive statsistics
# 
# You should include plots to support key points. The plots should be of an appropriate type and be labelled (eg axis labels and legends) in such a way that the reader can understand them directly, without needing to refer to your code or to the data table.
# 
# It should include subheadings. Where possible, subheadings summarize the key findings (eg 'older patients have longer hospital stays') rather than describing the analysis (ef 'association between age and length of stay')

# ## Your report [replace with a proper title!]

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
sns.set_theme()


# ## Data Source
# 
# The report examines a sample of 12,843 patients admitted to hospital in New York City with a heart attack.
# 
# The data were collected via the Medicare system and are modified from a dataset at <a href="https://dasl.datadescription.com/">DASL</a>.
# 
# The variables recorded were .........
# 

# In[2]:


### Import and inspect data
heartAttack=pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/heartAttack.csv')
display(heartAttack)


# ### Data Cleaning
# 
# Explain how many outlier/bad/missing values you removed and what your criteria for removal were

# ### Sample Overview
# 
# Report key demographics of the sample (proportion male/female; proportion that survived in each case)

# ### Distribution of charges
# 
# You should summarize the distribution of costs, disaggregated (broken down) by any categorical variables that, in your opinion, play an important role in determining cost

# ### Factors affecting charges
# 
# Explain, with supporting graphs and descriptive statistics, what are the key factor(s) affecting the cost of the hospital stay

# ### Factors affecting length of stay
# 
# You have probably established that length of stay is a key factor determining cost.
# 
# In this section, present the distribution of length of stay, disaggregated by any catcgorical variables that, in your opinion, play an important role in determining lenth of stay 
# 
# Also present any important correlations between length of stay and other numerical variables

# ### Your conclusions
# 
# Summarize the key points from your report, perhaps using a few bullet points.

# In[ ]:




