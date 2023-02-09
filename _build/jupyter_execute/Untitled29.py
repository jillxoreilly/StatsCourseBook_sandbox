#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bootstrapping the $t$ distribution


# We learned last week that for large samples, the sampling distribution of the mean as normalized by the standard error:
# 
# $$ Z = \frac{\bar{x}-\mu}{\frac{\sigma}{\sqrt{n}}} $$
# 
# ...  is the standard normal distribution $Z \sim \mathcal{N}(0,1)$
# 
# We also learned that if the data themselves are drawn from a normal distribution (such as height data), the above sampling distribution is a $t$ distribution (this is true for all sample sizes, including small samples - for large $n$ the $t$ distribution is very similar to the normal distribution)
# 
# $$ t = \frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}} $$

# In[2]:


Now we know how to obtain bbootstrapped sampling distributions, we shall see if the sampling distribution of the 


# In[ ]:





# In[ ]:





# In[ ]:


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




