#!/usr/bin/env python
# coding: utf-8

# # Permutation test for paired data
# 
# Say we are interested in whether men earn more money than women. 
# 
# We suspect that familial factors (family background and eduactional opportunities) play a major roll in determining adult income, so we decide to use a paired design, comparing brothers to their sisters.
# 
# We survey 25 brother-sister pairs in which both siblings are working full time. All surveyed individuals are between 50 and 55 years of age. 
# 
# We find that in XX cases the brother earns more than the sister, and the average difference in income is XX cm (note these are made up data for the exercise, but reflect the true distribution of incomes for this age bracket as reported by the UK Office for National Statistics).
# 
# How do we determine whether the difference is statistically significant (unlikely to have occurred due to chance)?
# 
# ## Hypotheses
# 
# $\mathcal{H_0}$: Our <b>null hypothesis</b> is that the mean income difference between brothers and their sisters is £0; E($x_M - x_F) = £0$
# 
# $\mathcal{H_a}$: Our <b>alternative hypothesis</b> is that the mean income difference favours brothers; E($x_M - x_F) > £0$
# 
# 
# ## Establishing the null distribution
# 
# Even if the null hypothesis were true, we wouldn't expect the mean income difference in our sample to be exactly zero; depending on which sibling pairs happen to be in our random sample, the average income difference would be randomly slightly in favour of men or women.
# 
# The task of working out whether we can reject the null hypothesis boils down to working out how likely it is that the mean difference we observed (on average the brother earns £XX more) could have happened due to chance, if the null hypothesis was true.
# 
# To answer this we need to know the <b>null distribution</b> - the probability distribution of brother-sister income differences that would arise if there was no true underlying difference in mens' and womens' incomes.
# 
# The shape and spread of the null distribution will depend on the distribution of data in the sample. In this particular case there are a couple of very large income differences and many smaller differences, which reflects something about the skewed nature of the income distribution overall. 
# 
# Whether we would obtain a mean income difference as large as the observed one (on average the brother earns £XX more) in a new sample would depend the proportion of sibling pairs in which the brother earns more than the sister, and how many large differences favour the brother rather than the sister, in the new sample.
# 
# In our sample, there are more pairs where the brother earns more than the sister than vice versa, and for the sibling pairs with the largest income difference, in most cases the brother is the higher earner. Of course this could happen due to chance even if men and women had the same income distribution, and the null hypothesis is that this is the case. 
# 
# Under the null hypothesis, the sex of the sibling would be irrelevant to predicting their income. If that were the case, it would just be random whether the higher earner in each pair was the brother or the sister, and we could simulate many more samples of sibling pairs by randomly relabelling some of our actual samples (randomly flipping or switching the labels 'brother' and 'sister' in some of our sibling pairs). 
# 
# In fact, that is how permutation testing works. By using the computer to simulate many 'new' samples in which the brother/sister labels are flipped in a random subset of sibling pairs from our original dataset, we can establish the null distribution <i>empirically</i> (this is not dissimilar to what we did previously with the bootstrap)
# 
# Let's go!
# 

# ### Coding up the permutation test
# 
# 

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# In[2]:


data = pandas.read_csv('data/BrotherSisterData.csv')
data


# In[3]:


data['brother'],['sister']]


# ### Why can't we break the pairing?
# 
# You will have noticed that the random shuffling we applied to the data was only done <i>within</i> pairs. Why?
# 
# As can be seen from the scatter plot, a major feature in the data is that high earning brothers tend to have high-earning sisters. The paired design allows us to look at the difference between men and women over and above the shared familial effects.
# 
# If we were to shuffle the data in such a way that we match brothers with the wrong sisters, our simulated datasets would not resemble the original dataset very much.
# 
# This can be seen in the figure below:
# 
# 
# 
# This reflects a general rule of permutation testing:
# 
# #### (Only) permute datapoints that are equivalent under the null hypothesis
# 
# If the null hypothesis were true, it should be just as likely that a sister has a higher income than her brother than vice versa. The null hypothesis <i>does not</i> say that income is unaffected by family, which is what would be implied if we were to repair brothers and sisters in our permuted samples.

# In[ ]:




