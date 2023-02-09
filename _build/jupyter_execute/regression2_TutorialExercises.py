#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# This week, you will be investigating attitudes to immigration using data from the <a href='https://www.europeansocialsurvey.org'>European Social Survey (ESS)</a>. 
# 
# The ESS is a highly respected survey and uses random sampling to achieve a sample that is representative of the population. The survey includes lots of questions about the social and economic circumstances of the household as well as asking a set of questions on political preferences and attitudes. 
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


# ## ESS data
# 
# Today’s data file is restricted to respondents in the UK. The outcome measure of interest is ‘better’ and is a score from 0-10 in answer to the following question: “Is the UK made a worse or a better place to live by people coming to live here from other countries?” 0 is labelled as “Worse place to live” and 10 as “better place to live”, or respondents could choose an answer in between. Thus, high scores indicate more open attitudes, i.e., those who feel more positive about the consequences of immigration, and low scores the opposite. 
# 
# This file contains several explanatory/ controls variables: 
# 
# * age (a continuous measure in years)
# * sex (a binary measure where 0 = male and 1 = female)
# * educ (a categorical measure of education where 1 = lower secondary qualifications or below, 2 = upper secondary (e.g., A Levels) and vocational qualifications, and 3 = Tertiary (university degree))
# * vote (a categorical measure of the party the respondent last voted for where 1 = Conservatives, 2 = Labour, 3 = any other party)
# * bornuk (a binary measure of whether the respondent was born in the UK where 0 = No, and 1 = Yes).

# In[2]:


# load and view the data
ess = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/immigrationData.csv')
ess


# ### Data cleaning
# 
# Get to know your data. 
# 
# * How survey respondants are there? 
# * For each variable, check whether there are many missing values.
# 

# In[3]:


# your code here to check for missing data


# ### Simple regression model
# 
# Some of the common ideas about attitudes to immigration include that younger people tend to be more positive about immigration. Let’s test this idea using regression analysis.
# 

# In[4]:


# Your code here to run a regression model Y = better, x = age
# You can refer back to last week's work for how to do this!


# * What does the result tell us? 
# 
# * Is the age coefficient positive or negative and how do we interpret the size of the slope?
# 
# ### Multiple regression model
# 
# We are going to add a further explanatory variable to the model: sex. 
#     
# This is a binary variable where male takes the value 0, and female takes the value 1.
# 
# Add sex to your model, keeping age in the model too. ou will need to change the formula from `better ~ age` to `better ~ age + sex`
# 

# In[5]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex


# * What does the coefficient for sex tell us? 
# 
# * Do men or women have more positive attitudes towards immigration? 
# 
# * In the new model that includes sex, does the age coefficient change from model 1?
# 
# NB: The eagle-eyed among you might spot that the coefficient for sex is not statistically significant. Well spotted! We will spend more time looking at statistical significance next week.
# 
# ### Add a categorical variable
# 
# Next, we are going to add education as a further explanatory variable. 
# 
# * This is a categorical variable - what are its possible values?
# 
# 

# In[6]:


ess['educ'].unique()


# Think:
#     
# * How many categories does the education variable have? 
# * How many dummy variables are needed in the regression model? 
# 
# Before you run the model, think about what you expect to see. Do you think the coefficients will be positive or negative? 

# In[7]:


# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = ess, formula = 'better ~ age + sex + educ')

# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 
 


# #### Choosing the reference category
# 
# Which category was used as the reference category?
# 
# You should be able to tell from the summary table, as there will be no $\beta$ value for the reference category - If we have categories A,B,C and B is the reference, then $\beta_A$ and $\beta_C$ tell us how much the expected value of $y$ increases or decreases in catgories A and C compared to category B.
# 
# By default, `statsmodels` chooses the least frequent category as the reference, which in this case is 'lower secondary'. So the $\beta$ values for 'Upper secondary' and 'Tertiary' tells us how much higher the value of 'better' is expected to be for survey respondants with 'Upper secondary' or 'Tertiary' education respectively.
# 
# You may wish to choose the reference category. You can do this by using slightly different syntax - for example to choose 'Upper secondary' as teh reference category, in the formula we replace the simple variable name `educ` with the code `C(educ, Treatment(reference="Upper secondary")`
# 
# I chose the middle category (Upper secondary) as the reference, so I am expecting opposite signed beta values for those with a level of education below (Lower secondary) or abobve (Tertiary) my reference category.
# 
# * Run the model, and check the output.

# In[8]:


# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = ess, formula = 'better ~ age + sex + C(educ, Treatment(reference="Upper secondary"))')
                                                          
                                                        
# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 
 


# ### Interpretation
# 
# * How should you interpret the education coefficients in the model? 
# * Which is the “omitted category” or “reference group” (these two terms are used interchangeably here). 
# * Can you explain in words the relationship between education and immigration attitudes? 
# 
# ### Further categorical variable
# 
# What do you think the attitudes will be like of people who are immigrants themselves, versus people who were born in the UK? 
# 
# Let’s test your hypothesis, by adding ‘bornuk’ to the model. This is another binary variable where 0 = born in the UK, and 1 = born outside the UK. 
# 
# Run the code. What does it show?
# 

# In[9]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex, x3 = education, x4 = bornuk


# What about you? Plug your own values into the regression equation and find out what the model predicts YOUR answer to the immigration question to be. (NB: I know you are all still doing your degree! Assume you have finished it for the purpose of this exercise). 
# 
# You could use pencil and paper or Excel, or type the equation in a code block as I have done below

# In[10]:


# edit this equation - 
# you will need to replace the B values with coefficients from the regression summary table, 
# and the variable names with actual values (so if your age is 20, replace 'age' with 20)
# for categorical variables you need to work out which B value to use - 

# better = B0 + B1*age + B2*sex + B3*education + B4*bornuk

# In the following examples I used 'upper secondary' as the reference category for the categorical variable 'educ'

# For example, for a person who is 41, female and tertiary educated, and was born in the UK, the value should be calculated as follows:
# better = intercept + coef(age)*41 + coef(sex[T.male])*0 + coef(educ[T.tertiary])*1 + coef(bornuk)*1
print(5.9264 + -0.0118*41 + 0.0390*0 + 1.1765*1 + 1.1811*1)

# For example, for a person who is 43, male and lower secondary educated, and was born outside the UK, the value should be calculated as follows:
# better = intercept + coef(age)*43 + coef(sex[T.male])*1 + coef(educ[T.Lower Secondary])*1 + coef(bornuk)*0
print(5.9264 + -0.0118*44 + 0.0390*1 + -0.6699*1 + 1.1811*0)


# ### Interaction terms
# 
# Finally, we are going to explore the effect of age, according to different political preferences using the ‘vote’ variable. We will do this by adding an interaction term of age*vote to the model.
# 
# When we want to include an interaction between, say, age and vote, we use age*vote in the model. This actually adds three explanatory variables to the regression - age, vote, and the interaction ageXvote - age was already in our old model so we need to remove it or it will be included twice

# In[11]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex, x3 = education, x4 = bornuk, x5=age*vote
# first we run this line to tell statsmodels where to find the data and the explanatory variables
reg_formula = sm.regression.linear_model.OLS.from_formula(data = ess, formula = 'better ~ sex + C(educ, Treatment(reference="Upper secondary")) + bornuk + age*vote')
                                                          
                                                        
# then we run this line to fit the regression (work out the values of intercept and slope)
# the output is a structure which we will call reg_results
reg_results = reg_formula.fit()

# let's view a summary of the regression results
reg_results.summary() 
 


# Interpret the results in your own words. 
# 
# Check your understanding with your classmates or your tutor. 
# 
# (Hint: where is the gap between the political parties is smaller, and where it is wider?). Does this make sense to you, in terms of people you know? (Do you know many young Conservatives?) 

# ## Further Exercises
# 
# 1. Can you run 3 separate regression models for Conservative voters, Labour voters, and Other? 
# * I'd recommend creating three separate data frames for each political preference

# In[12]:


# your code here!


# 2. Just by eyeballing the coefficients, do you think there might be any other significant interactions?
# 
# 3. A conceptual question: What other variables would you like to include in the model for explaining attitudes to immigration? (Things that are not included in this data set, but you think are likely to be important. Just assume the measures would be available!)
# 

# In[ ]:




