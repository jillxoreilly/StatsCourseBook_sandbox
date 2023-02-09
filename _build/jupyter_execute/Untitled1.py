#!/usr/bin/env python
# coding: utf-8

# # Permutation test for unpaired data
# 
# Say we are interested in whether students from Oxford of Cambridge earn more money five years after graduation.
# 
# We survey a small-ish number of students from each university and find that the income for Oxford students is sligtly higher. How can we determine whether this difference is real, or occurred due to chance?

# ### Establishing the null distribution
# 
# Even if the distribution of salaries for Oxford and Cambridge graduates was identical, we would not expect the mean salaries of Oxford and Cambridge graduates in our sample to be exactly the same. Just due to the random nature of sampling, there would be slightly more people with higher salaries, or more very high salaries, in one group or other. 
# 
# The question we need to answer whether the difference we observed is likely to have arisen due to chance in this way, or reflects a real difference in the underlying distribution of earnings for Oxford and Cambridge graduates.
# 
# In other words we need to know how what range of values the difference of mean salaries would take, if we were to draw more random samples of the same size as our actual sample.
# 
# To simulate this process of drawing many more samples, we use the data we do have (the salaries of the 40 graduates sureveyed) and randomly shuffle the labels of which graduate attended which university. In some of these random shuffles, more of the high salaries will be labelled 'Oxford' and in some, more of the high salaries will be labelled 'Cambridge'. How often will we get a difference of means as large as the one observed in our 'real' dataset?
# 
# #### Hang on, why are we relabelling the data?
# 
# According to the null hypothesis, all the graduates salaries are drawn from the same income distribution anyway. If that were true, a new sample would probably
# 
# 
