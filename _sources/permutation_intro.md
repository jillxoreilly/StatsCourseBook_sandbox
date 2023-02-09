# Permutation Testing

This week we introduce the idea of null and alternative hypotheses.

Many statistical tests work by assuming the null hypothesis (usually that there is no difference between groups, or that there is no relationship/correlation between variables) is true, and asking how likely the observed result would be to occur due to chance. Most classic tests (such as the t-test and Wilcoxon test, which you may have met at school) work this way.

This week we will introduce null hypothesis testing using a class of computer based tests which make it very explicit what we mean by assuming the null is true - permutation tests. Permutation tests involve shuffling datapoints between- or within groups to produce 'new' (resampled) datasets. We then observe how much the test statistic (such as the difference of means) varies randomly across the shuffled datasets and ask how often a test statistic as extreme aas the one observed in our real data occurs.

Which datapoints are allowed to be shuffled depends on the null hypothesis we are simulating.

We will cover three examples:
<ul>
<li> difference of means for independent samples (eg are men in Oxford taller than men in Cambridge)
<li> mean difference between paired datapoints (eg are brothers taller than their sisters)
<li> correlation (eg do tall brothers have tall sisters)
</ul>

We will see how permutation tests are constructed using 'home made' code, and also learn to run them using a built in function in <tt>scipy.stats</tt>

```{warning}
You need <tt>scipy.stats</tt> version 1.8.0 or higher to run the permutation tests.

For those running Python on their own computer, there are instructions on how to check this and update if necessary,
in the first page of the worked examples

For those using Colab, there is a block you need to run within each
page of worked examples

Please attempt to implement this before the tutorial
```


## Tasks for this week

<b>Conceptual material</b> is covered in the lecture. In addition to the
live lecture, you can find lecture videos on Canvas.

Please work through the guided exercises in this section (everything
<i>except</i> the page labelled "Tutorial Exercises") in advance of
the computer-based tutorial session.

To complete the guided exercises you will need to either:
<ul>
<li>open the pages in Google Colab (simply click the Colab button on each page), or
<li>download them as Jupyter Notbooks to your own computer and work
with them locally (eg in Spyder)
</ul>

If you find something difficult or have questions, you can discuss
with your tutor in the computer-based tutoral session.

This week is particularly heavy on conceptual material, so please do
discuss the guided exercises and tutorial exercises with your tutor to
make sure you understand
