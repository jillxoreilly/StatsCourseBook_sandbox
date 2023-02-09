#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# In these exercises we will create bootstrapped sampling distributions for all sorts of stuff!
# 
# We will work with a (made up) dataset containing scores on a wellbeing survey before and after the Christmas vaacation for some Oxford University students

# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ### Import and view the data

# In[2]:


wb = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/WellbeingSample.csv')
wb


# ### Plot the distribution of wellbeing scores
# 
# It's always a good idea to plot the data to familiarize yourself with them and spot any outliers!
# 
# Below is a basic plot of the wellbeing scores before and after the vacation

# In[3]:


sns.histplot(wb['Score_preVac'], bins=range(1,100,5), color='b', alpha=0.5)
sns.histplot(wb['Score_postVac'], bins=range(1,100,5), color='r', alpha=0.5)
plt.legend(['before vacation', 'after vacation'])
plt.xlabel('wellbeing score')
plt.show()


# ### Did wellbeing increase over the vacation?
# 
# Say I am interested in the change in wellbeing score across the vacation for psychology students. 
# 
# We are going to calculate the mean change in wellbeing score from pre- to post-vacation measurements and then obtain a bootstrapped confidence interval for this difference
# 
# If only a small percentage of simulated samples have a negative change in wellbeing over the vacation, we will conclude that we are confident mean wellbbeing increased over the vacation for psychology students
# 
# Let's start by creating a column in our dataframe for the difference in wellbeing score between pre- and post-vacation measurements

# In[4]:


# Your code here!


# Now let's 
# <ul>
#     <li>get the mean change in wellbeing for psychology students
# <li>find out how many psychology students there are
#     </ul>

# In[5]:


print('mean change = ' + str(##### your code here #####)
print('n = ' + str(##### your code here #####))


# The mean increase in wellbeing score across the vacation for the 25 Psychology students is 2.68
# 
# How confident can we be that wellbeing <i>really</i> increases across the vacation, though? If we surveyed a new sample of Psychology students, how close would the change in wellbeing be to 2.68? Would it still be greater than zero (ie would the vacation still increase wellbeing)?
# 
# We need the sampling distribution of the mean! (the mean change in wellbeing across the vac, that is)
# 
# Let's simulate it by bootstrapping!

# In[ ]:


nReps = # your code here
m = # create an empty array to store the sample means
n = # your code here

for i in range(nReps):
    sample = # your code here to draw a sample of size n with replacement fromthe dataframe wb
    m[i] = # the mean change in wellbeing across the vacation for this sample

sns.histplot(m) # plot the sample means


# We can also work out exactly what percentage of the samples have a negative change in wellbeing

# In[ ]:


100 * sum(m<0)/len(m)


# I make it about 11% of random (re)samples in which the change in wellbeing is negative.
# 
# This is some evidence that the change in wellbeing over the vacation is positive but would not be considered staatstically significant in general - more on statistical significance next term

# #### 95% confidence interval
# 
# We can define a 95% confidence interval for the change in wellbeing over the vacation in psychology students as the range in which 95% of (re)sample means fall:

# In[ ]:


# The boundaries of the 95% confidence interval 
# exclude the lowest and highest 2.5% of sample means 
# (ie exclude 5% of sample means overall)

print('lower bound = ' + str(np.quantile(m,0.025)))
print('upper bound = ' + str(np.quantile(m,0.975)))


# The confidence interval includes zero, meaning no change in wellbeing (or a negative change) is a plausible value for the population change in wellbeing over the vac

# ## Is wellbeing higher in Lonsdale than in Beaufort biology students?
# 
# Let's try bootstrapping something else!
# 
# Say we want to know if wellbeing (as measured before the vacation) is higher in biology students at Lonsdale or Beaufort college.
# 
# Let's have a look at the relevant data:

# In[ ]:





# In[ ]:


# Get the biology students only from the dataframe
wb[wb['Subject']=='Biology']


# In[ ]:


# count how many biology students in each college using df.value_counts()
# your code here!


# Plot their wellbeing scores (before the vac) in a violin plot

# In[ ]:


sns.violinplot(data=wb[wb['Subject']=='Biology'], y='Score_preVac', x='College')


# It looks like Beaufort biologists had slightly higher wellbeing scores but how confident can we be in that difference?
# 
# We need the sampling distribution for the difference of means for wellbeing score between colleges
# 
# We can adapt our bootstrap code to do this!

# In[ ]:


nReps = # your code here
mDiff = # create an empty array to store the sample means
nL = # number of biologists in Lonsdale college
nB = # number of biologists in Beaufort college

for i in range(nReps):
    sample_Lonsdale = # 
    sample_Beaufort = #
    mDiff[i] = # mean wellbeing of Beaufort biologists minus mean wellbeing of Lonsdale biologists
    

sns.histplot(mDiff) # plot the sample means


# In what proportion of (re)samples do Lonsdale biologists actually have higher mean wellbeing?

# In[ ]:


# your code here!


# ### Bootstrapped correlation between wellbeing scores before and after the vacation
# 
# Over the vacation, wellbeing went up overall - but are the students with higher wellbeing before the vacation generally also the ones with higher wellbeing after the vacation?
# 
# Let's get an overview by plotting the data

# In[ ]:


sns.scatterplot(data=wb, x='Score_preVac', y='Score_postVac')


# It looks like there is a fairly strong correlation between wellbeing scores before and after the vacation for the same individual.
# 
# The correlation might be exaggerated by a few outliers with particularly low scores, so let's use Spearman's correlation coefficient:

# In[ ]:


wb['Score_preVac'].corr(wb['Score_postVac'], method='spearman')


# I want to know how confident I can be that wellbeing before and after the vacation are correlated
# 
# I need a sampling distribution for the correlation coefficient $r$
# 
# I can obtain this using bootstrapping:

# In[ ]:


nReps=# your code here
r=# your code here
n=# your code here

for i in range(nReps):
    sample = # your code here
    r[i] = # your code here

sns.histplot(r)
plt.xlabel('sample correlation, $r_s$')
plt.show()


# We can see that all the (re)samples have a strong positive correlation between wellbeing before and after the vacation
# 
# Can you obtain a 95% confidence interval for the correlation coefficient $r_s$?

# In[ ]:


# your code here
print(str(np.quantile(r,0.025)) + ',' + str(np.quantile(r,0.975)))


# ## Further exercises
# 
# #### Bootstrapped correlation in a smaller sample
# 
# The sample correlation between wellbeing before and after the vacation was very reliably positive, partly because the correlation coefficient was high (in other words, we ca see there *is* a strong correlation in the scatterplot) and partly because $n$ is large
# 
# Let's look at the same correlation- wellbeing before and after the vac- in a smaller sample- just the Psychology students:

# In[ ]:


psy=wb[wb['Subject']=='Psychology']
sns.scatterplot(data=psy, x='Score_preVac', y='Score_postVac')


# Let's get the correlation coefficient:

# In[ ]:


psy['Score_preVac'].corr(psy['Score_postVac'], method='spearman')


# There is a positive correlation,although it is weaker than the correlation in the whole dataset of 300 students.
# 
# Intuitively, just from looking at the scatterplot, it feels that if we drew random samples from just the psychology students, we would find some random samples with a zero or even negative correlation between wellbeing before and after the vacation - much more likely that when we were working with the full dataset of 300 students.
# 
# <ul>
#     <li> Obtain a bootstrapped sampling distriubtion for the correlation coefficient r
#     <li> What proportion of the (re)samples have r less than 0?
#     <li> Obtain at 95% confidence interval for r
# </ul>

# In[ ]:


# Your code here!


# In[ ]:


sum(r<0)/len(r)

wb['Score_preVac'].quantile(0.06)

