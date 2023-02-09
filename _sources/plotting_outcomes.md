# Learning Objectives

## Conceptual

This week is heavier on Python than conceptual material.

However it is important that you understand which plots successfully
show the distribution of data, the relationship within paired data.

It is also important that you view your plots critically and choose
approprate settings so that your graph successfully illustrates the
point you are trying to make.

Examples would be:
<ul>
<li> appropriate axis labels and legend
<li> appropriate axis scaling 
<li> choice of colours
<li> inclusion of reference lines (such as the line x=y in the
scatterplot example)
</ul>

This material is covered in the lecture

## Python skills

In this course we will use plotting functions from the libraries <tt>matplotlib</tt> (imported as <tt>plt</tt>) and <tt>seaborn</tt> (imported as <tt>sns</tt>). 

Therefore all the plotting commands will be preceded by either
<tt>plt.</tt> or <tt>sns</tt>.

<tt>Seaborn</tt> is designed to work seamlessly with <tt>Pandas</tt>
dataframes. It also produces aesthetically pleasing plots.

<tt>Matplotlib</tt> is another plotting library that contains, amongst
other tings, many useful functions to customize plots (for example
editing the axis ranges)


After this week you should be able to:


<ul>
<li>	Plot a data distribution using <tt>sns.histplot</tt> choosing appropriate bin sizes and
locations
<li> Plot data using a Kernel Density Estimate (KDE) plot, using 
<tt>sns.kdeplot</tt> or adding the KDE option to <tt>sns.histplot</tt>
<li> Add a rug plot to a KDE plot using <tt>sns.kdeplot</tt> and <tt>sns.rugplot</tt>
</ul>
<ul>
<li>	Plot category counts using <tt>sns.countplot</tt>
<li> Plot category means using <tt>sns.barplot</tt>
<li>	Plot data using a box and whisker plot with <tt>sns.boxplot</tt>
<li>	Plot data using a violin plot with <tt>sns.violinplot</tt>
</ul>
<ul>
<li>	Plot paired data using <tt>sns.scatterplot</tt>
<li> Plot paired data using a scatterplot + histograms using <tt>sns.jointplot</tt>
</ul>
<ul>
<li> Break down plots by a categorical variable from a <tt>pandas</tt>
dataframe, using the arguments <tt>x</tt>, <tt>y</tt> and
<tt>hue</tt> of the plotting tools
</ul>
<ul>
<li> Make a plot with multiple panels using <tt>plt.subplot</tt>
<li> Adjust axis ranges
<li> Change axis labels
</ul>





This material is covered in the Jupyter Notebooks in this section
