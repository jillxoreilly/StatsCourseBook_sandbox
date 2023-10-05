#!/usr/bin/env python
# coding: utf-8

# # Permutation test for paired data
# 
# We first look at the case of paired data - data in which we wish to compare two groups and each datapoint in one group has a counterpart in the other
# 
# Experimental designs using paired data include matched pairs (eg brothers and sisters) and repeated measures (measurements of the same individual before- and after- an intervention, or on- and off-drug).
# 

# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

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


# ## Colab users
# 
# You need to use a more recent version of scipy.stats than the default. To do this run the following code block and *after* it has run, go to the menus at the top of colab and click `runtime-->Restart Runtime`

# In[2]:


# Set-up Python libraries - you need to run this but you don't need to change it
get_ipython().system('pip install scipy==1.10.0')
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import seaborn as sns
sns.set_theme(style='white')
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ## Toy example
# 
# [A toy example is an example with a very small dataset, just to show how it works]
# 
# #### Question & design
# 
# We are interested in whether men or women own more pairs of socks. 
# 
# We decide on a **matched pairs design** in which husbands are compared to their wives, as it is hypothesised that lifestyle factors such as the size of the home in which people live and the duration of holidays taken will affect the number of pairs that can be reasonably justified, and these lifestyle factors are generally shared by both members of a married couple.
# 
# 
# #### Hypotheses
# 
# We can state our hypotheses as follows:
# 
# $\mathcal{H_o}:$ The mean sex difference quantity of socks owned is zero 
# * in our dataset, on average a wife and her husband have the same number of pairs of socks
# 
# $\mathcal{H_a}:$ The mean sex difference quantity of socks owned is non-zero
# * in our dataset, on average a wife has mome socks than her husband, or vice versa
# 
# #### Data
# 
# We obtain sock-counts for the following informal sample of 10 couples:

# In[3]:


socks = pd.DataFrame(data=[[10,12],[17,13],[48,20],[28,25],[23,18],[16,14],[18,13],[34,26],[27,22],[22,14]], columns=['Husband','Wife'])
socks


# Let's plot those data. 
# 
# For paired data a scatter plot is often a good choice, but actually for this tiny dataset, I prefer showing the pairs using a plot like that shown on the right. 
# * You won't be required t reproduce this type of plot for the course.
# 
# 
# * Why do I prefer the plot on the right? We are going to be interested in whether husbands have more socks than their wives or vice versa - I think this can be very clearly seen in the plot on the right (by inspecting whether the lines slope up or downwards) - however if there were 1000 couples in the sample rather than 10 this plot would be too crowded and hard to inspect
# 

# In[4]:


# Plotting code - don't get sidetracked by this, it's not that important
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
sns.scatterplot(data=socks, x='Husband', y='Wife')
plt.plot([0,50],[0,50],'r--') # add the line x=y for comparison


plt.subplot(1,2,2)
sns.barplot(data=socks, ci=None, color=[0.9,0.9,0.9])
sns.lineplot(data=socks.T, legend=False, marker='o') # ci=None switches off errorbars
plt.ylabel('pairs of socks owned')

plt.tight_layout()
plt.show()


# **Note-** 
# 
# * In most couples (9/10) the husband owns more socks that the wife
# * There is one couple in which the husband has an extreme number of socks.
# 
# #### Test statistic
# 
# We need to sumamrize the sex difference as a number. 
# 
# Here, we are interested in the within-pairs difference in sock ownership, so we need the mean difference in pairs of socks owned, for [husband - wife].
# 
# This mean difference, <tt>mean(Husband-Wife)</tt>, is calculated as follows:

# In[5]:


socks['difference'] = socks.Husband-socks.Wife # create a new column for the within-couple difference
socks.difference.mean()


# On average, the husbands own 6.6 more pairs of socks than their wives.
# 
# ### Is the result statistically significant? 
# 
# In our particular sample, husbands have (on average) more socks than their wives - our test statistic (<tt>mean(Husband-Wife)</tt>) is 6.6. 
# 
# However, even if there were no true sex differences in sock ownership, if we picked 10 random couples we wouldn't expect the average difference in number of socks owned to be *exactly zero* - just by chance the wives would sometimes have more socks than the husbands, or vice versa. 
# 
# Is it plausible that the sex difference we observed (husbands have 6.6 more pairs of socks than their wives) arose due to chance from a situation in which there is no true sex difference in sock ownership (ie, the *null hypothesis is true*?
# 
# In that case, it would be just chance whether the person with more socks in each couple was the man or the woman.
# 
# 
# ### Permutation
# 
# In previous weeks we have obtained simulated distributions of statistics such as the sample mean, by drawing many samples from a (known) parent population (as in the exercises on the Central Limit Theorem) or by bootstrapping. Here we will attempt to do something similar.
# 
# We don't have access to the parent population, only the sample of 10 couples. The sample tells us several interesting things about the parent distribution, regardless of sex effects:
# 
# * For most couples there is a small difference in the number of pairs of socks owned
# * For some couples there is a large difference, driven by one member having way more socks than ois reasonable
#     * ie the distriution of differences has positive skew
#     
# * husbands with lots of socks tend to have wives with lots of socks 
#     * ie there is a correlation in number of socks between husbands and wives) </ul>
# 
# It also tells us about some potential sex effects:
# 
# * in most couples the husband has more socks
# * the outlier individuals with loads of socks tend to be male
# 
# What we are going to do is shuffle the data around to create many new (re)samples **preserving the non-sex-related information** but **ignoring the sex of the sock owner**. 
# 
# We will do this by creating lots of new *resamples* of the data in which, for each couple, we randomly decide who gets which label, *husband* or *wife*. Within each resample, some couples will retain their true labels and some will be relabelled; which couples are which will differ between resamples.
# 
# For each resample, we then calculate the mean difference, <tt>mean(Husband-Wife)</tt>.
# 
# After repeating the process thousands of times, we can ask on what proportion of random resamples we get a values of <tt>mean(Husband-Wife)</tt> at least as large as our observed difference, 6.6.

# ### Run the simulation
# 
# To generate new simulated datasets, we will shuffle around the datapoints in our original dataset. 
# 
# Which ones can we shuffle?
# 
# * We assume there are no sex differences, so we can swap men for women
# * We assume that it *does* matters which couple you are in (high-sock men tend to have high-sock wives), therefore we cannot swap people between couples.
# 
# Therefore, the only shuffling that we are allowed is to swap the labels 'Husband' and 'Wife' within couples. 
# 
# Conceptually, to generate a new simulated dataset (one *resample*), we go through each couple in turn and 'flip a virtual coin' to decide whether the labels 'Husband' and 'Wife' are flipped.
# 
# If you are interested you can read more about how this would work in code at the bottom of this page.
# 
# **Here are the original data and four random permutations:**
# 
# <img src= "../images/HT_wk1_4Permutations.png" width="100%" />
# 
# Look closely. Each coloured line represents on couple. Note that some of the lines are left-right flipped, but the lines never move up or down overall (because we are only flipping people within couples).
# 
# The grey bars show the group means in each permutation. 
# * Sometimes the mean number of socks is higher for the husbands, sometimes for the wives. 
#     * These two situations should happen equally often in the permuted data as the 'high sock' partner in each couple is assigned equally often the labels 'husband' and wife'.
# * The group with the higher mean does tend to be the group with the extreme 48-sock individual in it.
# 
# #### Flipping - toy example
# 
# The code below randomly flips the labels 'husband and wife' in half the couples. Run it a few times and 
# 
# To make it easier to see what is going on, I have created a tiny dataframe in which there are only three couples and the husband always has 10 more pairs of socks than the wife. 
# 
# - **you don't need to be able to reproduce this code** because we will use a built-in function to apply permutation tests, but you should try to understand conceptually what is happening

# In[6]:


socks_shuffled = socks.copy()  # work on a copy of the original dataframe
for i in range(len(socks_shuffled)):
    if np.random.rand()>0.5: # generate a random number between 0 and 1 - if it is more than 0.5:
        socks_shuffled.loc[i,'Husband'] = socks.loc[i,'Wife'] # flip number of socks for husband and wife
        socks_shuffled.loc[i,'Wife'] = socks.loc[i,'Husband'] # flip number of socks for husband and wife
    #else:
        # don't shuffle the row!
socks_shuffled


# #### What?
# 
# The above might be clearer in an example where the flips are easier to see.
# 
# Try running the code block below a few times and keep an eye on how the dataframe changes - note that in the original dataframe the man always has an odd number of pairs of socks.

# In[7]:


df = pd.DataFrame(data=[[11,1],[12,2],[13,3]], columns=['Husband','Wife'])

df_shuffled = df.copy()  # work on a copy of the original dataframe
for i in range(len(df)):
    if np.random.rand()>0.5: # generate a random number between 0 and 1 - if it is more than 0.5:
        df_shuffled.loc[i,'Husband'] = df.loc[i,'Wife'] # flip number of socks for husband and wife
        df_shuffled.loc[i,'Wife'] = df.loc[i,'Husband'] # flip number of socks for husband and wife
    #else:
        # don't shuffle the row!
df_shuffled


# ### Visualizing randoms shuffles in the sock data
# 
# Back to our 'real' sock data
# 
# Let's see how the distribution of differences changes over a few random shuffles.
# 
# Below I generate 4 random shuffles of our sock data (in which some husbands and wives are randomly flipped), and plot the outcomes:

# In[8]:


plt.figure(figsize=(10,4))
plt.subplot(1,5,1)
sns.barplot(data=socks, ci=None, color=[0.9,0.9,0.9]) # ci=None switches off errorbars
for i in range(len(socks)):
    plt.plot([0,1], [socks.Husband[i], socks.Wife[i]], '.-')
    plt.xticks([0,1], labels=['Husband','Wife'])

for n in range(4):
    socks_shuffled = socks.copy()  # work on a copy of the original dataframe
    for i in range(len(socks)):
        if np.random.rand()>0.5: # generate a random number between 0 and 1 - if it is more than 0.5:
            socks_shuffled.loc[i,'Husband'] = socks.loc[i,'Wife'] # flip number of socks for husband and wife
            socks_shuffled.loc[i,'Wife'] = socks.loc[i,'Husband'] # flip number of socks for husband and wife
        #else:
        # don't shuffle the row!
    socks_shuffled
    

    plt.subplot(1,5,n+2)
    sns.barplot(data=socks_shuffled, ci=None, color=[0.9,0.9,0.9]) # ci=None switches off errorbars
    for i in range(len(socks)):
        plt.plot([0,1], [socks_shuffled.Husband[i], socks_shuffled.Wife[i]], '.-')
        plt.xticks([0,1], labels=['Husband','Wife'])
plt.tight_layout()
plt.show()


# We note that:
#     
# <ul>
#     <li> Different couples are randomly flipped in different simulated datasets (shuffles - look which colour=ed lines have reversed their slope)
#     <li> It matters a lot whether the couples with a big disparity were flipped - you can get a sense of this by looking at the grey bars which show the mean number of socks for men and women
# </ul>
# 
# ### Obtain the summary statistic of interest
# 
# We are interested in the mean difference in pairs of socks owned [husband-wife]. For each shuffle this is obtained as follows:

# In[9]:


mDiff = np.mean(socks_shuffled.Husband - socks_shuffled.Wife)
print('mean difference for the last shuffle = ' + str(mDiff))


# ### Plot the null distribution for a large number of shuffles
# 
# Now we can repeat the process for a large number of shuffles and get the mean difference in pairs of socks owned [husband-wife] for each shuffle. The distribution of these difference is the null distribution to which our observed difference (husbands own 6.6 more pairs) is to be compared.

# In[10]:


nReps = 10000 # (number of shuffles)
mDiff = np.empty(nReps) # array to store mean difference for each shuffle

for j in range(nReps):
    socks_shuffled = socks.copy()  # work on a copy of the original dataframe
    for i in range(len(socks)):
        if np.random.rand()>0.5: # generate a random number between 0 and 1 - if it is more than 0.5:
            socks_shuffled.loc[i,'Husband'] = socks.loc[i,'Wife'] # flip number of socks for husband and wife
            socks_shuffled.loc[i,'Wife'] = socks.loc[i,'Husband'] # flip number of socks for husband and wife
        #else:
        # don't shuffle the row!
    mDiff[j] = np.mean(socks_shuffled.Husband - socks_shuffled.Wife)
    
sns.histplot(mDiff)
plt.show()

print('proportion >6.6 = ' + str(100*np.mean(mDiff>6.6)) + '%')


# We can see that the null distribution for the mean difference in socks owned between husbands and wives is a bit bimodal. This is probably due to the large influence of outliers (points to the right of the plot above are probably those where the two high-sock individuals were assigned to be husbands; points to the left are probably cases where the two high-sock individuals were assiged to be wives)
# 
# ### The $p$ value
# 
# We can also calculate the proportion of cases in which the mean difference in socks owned for [Husband-Wife] exceeds the value we observed in our original sample, 6.6. This proportion is about 0.06% (it will actually vary on each run of the permutation test as the permutations are random - but hopefully not much). It tells us that if we simulate a situation in which sex does not determine the number of socks owned (but preserving some other important features of the dataset like the high skew, and the correlation between husabnds and their wives), there is only a 0.06% chance that we would get an apparent sex difference as large as the one we observed in our 'real' data.
# 
# The probability that the test statistic (in this case, the mean difference in pairs of socks owned) would be observed if the null hypothesis were true, is sometimes called the <b><i>$p$-value</i></b>. 
# 
# Our permutation test shows that the $p$-value associated with the observed difference of means is 0.0006.
# 
# The result is considered statistically significant if $p$ is smaller than some predetermined level, known as $\alpha$. Usually $\alpha = 0.05$ or $\alpha = 0.01$ is used, so the result is significant if $p<0.05$ or $p<0.01$. Our result is therefore statistically significant.

# ## Use a built in function
# 
# Now you have seen how the permutation test works, we can learn how to run it more easily using the built in function <tt>scipy.stats.permutation_test</tt>
# 
# <b>Note-</b> For those NOT using colab - You need scipy stats version > 1.8.0 to run this. You may need to check your version by running the following code block.

# In[11]:


import scipy as scipy
scipy.version.version


# If this is less than 1.8.0 you need to update it - see the technical note in the first page of this chapter
# 
# For those who are using Colab - check you followed the instructions at the top of this page

# ### Syntax of <tt>stats.permutation_test</tt>
# 
# Here is how we run the permutation test (same as the one we did with our own code above, although note how much more quickly this one runs!)

# In[12]:


def mDiff(x, y):
    return np.mean(x-y)

stats.permutation_test((socks.Husband, socks.Wife), mDiff, permutation_type='samples', alternative='two-sided', n_resamples=10000)


# Firstly, to reassure you this is doing a very similar job to our home-made code, check the p-value (should be about 0.06). 
# 
# We can also plot the null distribution, which hopefully looks similar to what we got from the home-made code:

# In[13]:


res = stats.permutation_test((socks.Husband, socks.Wife), mDiff, permutation_type='samples', alternative='two-sided', n_resamples=10000)
sns.histplot(res.null_distribution)
plt.show()


# However, the syntax may be a bit unfamiliar.
# 
# Firstly, we had to give the function <tt>stats.permutation_test</tt> our two samples <tt>(socks.Husband, socks.Wife)</tt> as a pair of <b>series</b> (individual columns from the dataframe), rather than giving it the whole pandas dataframe as we do for many other stats functions.
# 
# Secondly, to tell <tt>stats.permutation_test</tt> the test statistic we want to get the null distribution of, we had to pass it a <i>function</i> called <tt>mDiff</tt>, and this function had to have the property that it takes in two series <tt>(socks.Husband, socks.Wife)</tt> and returns a single number <tt>mean(socks.Husband, socks.Wife)</tt>

# ### Defining a function
# 
# You will have come across this in datacamp but we haven't used it since. Don't be scared! It's unfamiliar but quite handy. On the other hand for a pairwise permutation test, the function I have given you for mDiff is always going to work, so if in doubt you can just copy it :-)
# 
# A function is a little computer programme that takes in some information (in this case, it takes in two series, <tt>(socks.Husband, socks.Wife)</tt> and returns some value (in this case the mean difference <tt>mean(socks.Husband, socks.Wife)</tt>

# In[14]:


# define a function
def mDiff(x, y):
    return np.mean(x-y)

# run the function for some inputs
mDiff(socks.Husband, socks.Wife)


# Here's another example:

# In[15]:


# definte a new function that divides one element of each pair by the other, and then adds up the result across pairs
def bananas(x,y):
    return sum(x/y)

cats = np.array([1,2,3]) # one input array - have given it an arbitrary name
dogs = np.array([10,20,30]) # another input array - have given it an arbitrary name

bananas(cats,dogs)


# Now we can see how we could run <tt>stats.permutation_test</tt> on our function <tt>bananas</tt> and our data <tt>cats</tt> and <tt>dogs</tt>

# In[16]:


stats.permutation_test((cats, dogs), bananas, permutation_type='samples', alternative='two-sided', n_resamples=10000)


# ## Recap
# 
# To run a permutation test on paired data, we randomly flipped some of the pairs so that the husband's sock count was assigned to the wife and vice versa. We did NOT move people between couples, as we want to retain the characteristic of the original dataset that high-sock husbands tend to have high-sock wives
# 
# For each shuffle we calculated the mean (pairwise) difference in the number of socks - husband-wife. 
# 
# Permutation testing in this way gives us a null distribution for the mean difference. Values of mean difference that occur rarely in the null distribution are considered statistically significant.
#     
# To run the permutation test with <tt>scipy.stats</tt> we need the option `permutation_type='samples'`

# In[ ]:




