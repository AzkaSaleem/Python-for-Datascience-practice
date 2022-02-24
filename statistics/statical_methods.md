# Choosing a Statical Method
**Test and their types**



Paramatric test | Non Paramatric test 
---------|----------
 more relaiable results | less relaiable results |
 first we have meet the assumptions | calculate the rank of data  
|                          | no need to make assumptions

# Before starting Data analysis, follow some Steps!

**1. Normality test**

   1. shapiro-wilk test( relaiable)
   2. kolmogorov-simirnon Test(less relaiable)

**2. Homogenity test**

the vartiance of the  variable in data are equal

1. levene's test
 
**3. Porpuse of your Research Question**

two types of purpose
1. Relationship / Connection
   1. e.g: can food predict weight of a group of individual
   2. we seek : 
      1. Connection
      2. Correlation 
      3. causation
      4. prediction
2. Comparision / Difference
   1. atleast two groups
   2. e.g: male vs female
   3. e.g: grouping individuals by color preferances
   4. e.g: control group vs treatment group

**4. Data types you are working with**

1. Catagorical 
   1. qualitative 
   2. As: text character or factor
2. Continous 
   1. quantitative
   2. as: numbers, int or float

**5. Choose a Statical Test**

Three families of statical test
1. Chi-squared method
   1. comparison
   2. catagories only
   3. Types
      1. Chi-squared test of homogeneity
      2. Chi-squared test of independence
2. t-test/ANOVA
   1. comparison
   2. catagorical and continous
   3. Types
      1. One-sample t-test(for one group with a known mean)
      2. Two-sample t-test
         1. unpaired t-test (two different group)
         2. paired t-test (same group twice)
      3. ANOVA (analysis of variance)
         1. One way ANOVA 
         2. two-way ANOVA
         3. repeated measures of ANOVA
3. Correlation
   1. relationship
   2. continous only
   3. types
      1. pearson's correlation (1 dependent and 1 independent var.)
      2. regression (1 dependent and 1 independent var.)
~~~
After following these 5 steps you assume that your  data is now 
**Normally distributed or follow Gaussian distribution**
if your assumption not met ! then
1. normalize your data 
   1. standardization
   2. min-max scaling
   3. log transformation
2. Use alternative non-paramatric test
~~~
**6. non-paramatric test**
   1. chi-squared 
   2. t-test/ ANOVA
         1. one sample wilcoxen 
         2. signed rank test
         3. unpaired t-test (mann whitney's u-test)
         4. paired t-test (wilcoxon)
         5. ANOVA (kruskal-wallis test)
         6. MANOVA
         7. MANCOVA
   3. Correlation
       1. pearsons cor.
       2. spearmans cor.
       3. kendalls tau regression

**7. Some other tests**
1. Reliability tests
2. validity tests
3. sample size computation