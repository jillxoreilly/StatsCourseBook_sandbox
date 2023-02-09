#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# In these exercises we will create bootstrapped sampling distributions for all sorts of stuff!
# 

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


wb = pandas.read_csv('data/wellbeingSample.csv')
wb


# ### Plot the distribution of wellbeing scores

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
# We are going to calculate the mean change in wellbeing score from pre- to post-vacation measuremments and then obtain a bbootstrapped confidence interval for this difference
# 
# If only a small percentage of simulated samples have a negative change in wellbeing over the vacation, we will conclude that we are confident mean wellbbeing increased over the vacation for psychology students
# 
# Let's start by creating a column in our dataframe for the difference in wellbeing score between pre- and post-vacation measurements

# In[4]:


wb['Score_diff'] = wb['Score_postVac']-wb['Score_preVac']


# Now let's 
# <ul>
#     <li>get the mean change in wellbeing for psychology students
# <li>find out how many psychology students there are
#     </ul>

# In[5]:


print('mean change = ' + str(wb[wb['Subject']=='Psychology']['Score_diff'].mean()))
print('n = ' + str(len(wb[wb['Subject']=='Psychology'])))


# The mean increase in wellbeing score across the vacation for the 25 Psychology students is 2.68
# 
# How confident can we be that wellbeing <i>really</i> increases across the vacation, though? If we surveyed a new sample of Psychology students, how close would the change in wellbeing be to 2.68? Would it still be greater than zero (ie would the vacation still increase wellbeing)?
# 
# We need the sampling distribution of the mean! (the mean change in wellbeing across the vac, that is)
# 
# Let's simulate it by bootstrapping!

# In[6]:


nReps = # your code here
m = # create an empty array to store the sample means
n = # your code here

for i in range(nReps):
    sample = # your code here to draw a sample of size n with replacement fromthe dataframe wb
    m[i] = # the mean change in wellbeing across the vacation for this sample

sns.histplot(m) # plot the sample means


# In[168]:


nReps = 10000
m = np.empty(nReps)
n = len(wb[wb['Subject']=='Psychology'])

for i in range(nReps):
    sample = wb.sample(n, replace=True)
    m[i] = sample['Score_diff'].mean()
    
sns.histplot(m) # plot the sample means


# We can also work out exactly what percentage of the samples have a negative change in wellbeing

# In[170]:


100 * sum(m<0)/len(m)


# I make it about 8.7% of random (re)samples in which the change in wellbeing is negative.
# 
# This is some evidence that the change in wellbeing over the vacation is positive but would not be considered staatstically significant in general - more on statistical significance next term

# #### 95% confidence interval
# 
# We can define a 95% confidence interval for the change in wellbeing over the vacation in psychology students as the range in which 95% of (re)sample means fall:

# In[176]:


# The boundaries of the 95% confidence interval 
# exclude the lowest and highest 2.5% of sample means 
# (ie exclude 5% of sample means overall)

print('lower bound = ' + str(np.quantile(m,0.025)))
print('upper bound = ' + str(np.quantile(m,0.975)))


# The confidence interval includes ero, meaning no change in wellbeing (or a negative change) is a plausible value for the population change in wellbbeing over the vac

# ## Is wellbeing higher in Lonsdale than in Beaufort engineering students?
# 
# Let's try bootstrapping something else!
# 
# Say we want to know if wellbeing (as measured before the vacation) is higher in engineering students at Lonsdale or Beaufort college.
# 
# Let's have a look at the relevant data:

# In[186]:


# Get the engineering students only from the dataframe

# count how many engineering students in each college using df.value_counts()
wb[wb['Subject']=='Biology']['College'].value_counts()


# PLot their wellbbeing scores (before the vac) in a violin plot

# In[187]:


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
    sample_Beaufort = 
    mDiff[i] = # mean wellbeing of Beaufort biologists minus mean wellbeing of Lonsdale biologists
    

sns.histplot(mDiff) # plot the sample means


# In[199]:


LonsdaleBiol = wb[(wb['College']=='Lonsdale') & (wb['Subject']=='Biology')]
BeaufortBiol = wb[(wb['College']=='Beaufort') & (wb['Subject']=='Biology')]

nReps = 10000
mDiff = np.empty(nReps)
nL = len(LonsdaleBiol)
nB = len(BeaufortBiol)

for i in range(nReps):
    sample_Lonsdale = LonsdaleBiol.sample(nL, replace=True)
    sample_Beaufort = BeaufortBiol.sample(nB, replace=True)
    mDiff[i] = sample_Beaufort['Score_preVac'].mean()-sample_Lonsdale['Score_preVac'].mean() # mean wellbeing of Beaufort biologists minus mean wellbeing of Lonsdale biologists
    

sns.histplot(mDiff) # plot the sample means


# In[200]:


sum(mDiff<0)/len(mDiff)


# ### Bootstrapped correlation between wellbeing scores before and after the vacation
# 
# Over the vacation, wellbeing went up overall - but are the students with higher wellbeing before the vacation generally also the ones with higher wellbeing after the vacation?
# 
# Let's get an overview by plotting the data

# In[212]:


sns.scatterplot(data=wb, x='Score_preVac', y='Score_postVac')


# It looks like there is a fairly strong correlation between wellbeing scores before and after the vacation for the same individual.
# 
# The correlation might be exaggerated by a few outliers with particularly low scores, so let's use Spearman's correlation coefficient:

# In[213]:


wb['Score_preVac'].corr(wb['Score_postVac'], method='spearman')


# I want to know how confident I can be that wellbeing before and after the vacation are correlated
# 
# I need a sampling distriubtion for the correlation coefficient $r$
# 
# I can obtain this using bootstrapping:

# In[216]:


nReps=10000
c=np.empty(nReps)
n=len(wb)

for i in range(nReps):
    sample = wb.sample(n, replace=True)
    c[i] = sample['Score_preVac'].corr(sample['Score_postVac'], method='spearman')

sns.histplot(c)
plt.xlabel('sample correlation, $r_s$')
plt.show()


# We can see that all the (re)samples have a strong positive correlation between wellbeing before and after the vacation
# 
# Can you obtain a 95% confidence interval for the correlation coefficient $r_s$?

# In[217]:


# your code here


# # Further exercises
# 
# #### Bootstrapped correlation in a smaller sample
# 
# The sample correlation between wellbeing before and after the vacation was very reliably positive, partly because the correlation coefficient was high (in other words, we ca see there *is* a strong correlation in the scatterplot) and partly because $n$ is large
# 
# Let's look at the same correlation- wellbeing before and after the vac- in a smaller sample- just the Psychology students:

# In[220]:


psy=wb[wb['Subject']=='Psychology']
sns.scatterplot(data=psy, x='Score_preVac', y='Score_postVac')


# Let's get the correlation coefficient:

# In[221]:


psy['Score_preVac'].corr(psy['Score_postVac'], method='spearman')


# There is a positive correlation,although it is weaker than the correlation in the whole dataset of 300 students.
# 
# Intuitively, just from looking at the scatterplot, it feels that if we drew random samples from just the psychology students, we would find some random samples with a zero or even negative correlation between wellbeing before and after the vacation - much more likely that when we were working with the full dataset of 300 students.
# 
# <ul>
#     <li> Obtain a bootstrapped sampling distriubtion for the correlation coefficient $r_s$
#     <li> What proportion of the (re)samples have $r_s<0$?
#     <li> Obtain at 95% confidence interval for $r_s$
# </ul>

# In[222]:


nReps=10000
c=np.empty(nReps)
n=len(psy)

for i in range(nReps):
    sample = psy.sample(n, replace=True)
    c[i] = sample['Score_preVac'].corr(sample['Score_postVac'], method='spearman')

sns.histplot(c)
plt.xlabel('sample correlation, $r_s$')
plt.show()


# In[278]:


sum(c<0)/len(c)

wb['Score_preVac'].quantile(0.06)


# ### Further exercises
# 
# Let's investigate some more questions using bootstrapping!
# 
# <ol>
#     <li> Do PPE students have higher wellbeing (before the vacation) than Psychology students? 
#         <ul><li>What percentage of random resamples is the mean wellbeing higher for PPE students?</ul>
#     <li> The 5th centile of the wellbeing distriubtion is the score below which the students with the lowest 5% of wellbeing scores fall. The 5th centile of wellbeing is exactly the same pre- and post vacation (49). 
#         <ul><li>Obtain a sampling distribution for the difference in the 5th centile pre- and post vacation</ul>
# </ol>

# In[282]:


# Exercise 1 solution

PPE=wb[wb['Subject']=='PPE']
psy=wb[wb['Subject']=='Psychology']

nReps = 10000
mDiff = np.empty(nReps)
nPPE = len(PPE)
nPsy = len(psy)

for i in range(nReps):
    sample_PPE = PPE.sample(nPPE, replace=True)
    sample_psy = psy.sample(nPsy, replace=True)
    mDiff[i] = sample_PPE['Score_preVac'].mean()-sample_psy['Score_preVac'].mean() # mean wellbeing of Beaufort biologists minus mean wellbeing of Lonsdale biologists
    

sns.histplot(mDiff) # plot the sample means
print('proportion of resamples in which PPE wellbeing is higher: ' + str(sum(mDiff>0)/len(mDiff)))


# In[288]:


# Exercise 2 solution

nReps = 10000
diff_q05 = np.empty(nReps)
n = len(wb)

for i in range(nReps):
    sample = wb.sample(n, replace=True)
    diff_q05[i] = sample['Score_postVac'].quantile(0.05)-sample['Score_preVac'].quantile(0.05)

sns.histplot(diff_q05) # plot the sample means

# CI - note the irritatingly different syntax to get quantile of an np array vs pandas df
print(str(np.quantile(diff_q05,0.025)) + ',' + str(np.quantile(diff_q05,0.975)))


# In[272]:


n=20
data= np.random.normal(10,2,n)
m=data.mean()

nReps=10000
t=np.empty(nReps)


for i in range(nReps):
    sample=np.random.choice(data,n,replace=True)
    t[i]=(sample.mean()-m)/(sample.std()/(n**0.5))

sns.histplot(t, bins=np.arange(-4,4,0.1))

binwidth=0.1
x=np.arange(-4.05,4.05,binwidth)
p=stats.t.pdf(x,n-1)
frq=p*nReps*binwidth
plt.plot(x,frq,'k')


# In[227]:





# In[ ]:




