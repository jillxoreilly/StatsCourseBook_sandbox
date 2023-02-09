#  Concepts: Statistical Significance in Regression

* What is statistical inference?

```{admonition} Click to reveal answer
:class: dropdown
Inference is drawing conclusions about the population from sample data. 
```

To be able to draw conclusions about the population from the results of a regression model, we need to check two things. First, whether the slope is statistically significantly different to zero, and second, whether the regression assumptions have been met. We’ll start by thinking about testing the slope for significance.

When we test a regression slope for significance, we are running a hypothesis test. We can set up the hypotheses in the following way, where $\Beta$ is the slope for $x$ in the population.

The null hypothesis can be written as $\mathcal{H_0}: \Beta = 0 $
And the alternative hypothesis as  $\mathcal{H_a}: \Beta \neq 0 $

Note: In regression we use the two-tailed test, as we are interested in testing whether there is **an association** and not to predict the direction of the association.
