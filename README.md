Degree Prospects 
In this project we will be analysing the salaries at entry level and mid-career of different degree holders across discipline (degree major),regions and type of univerisities.
We have utilized the following 3 datasets which are stored in the resources folder.
1 degrees-that-pay-back.csv
2 salaries-by-college-type.csv
3 salaries-by-region.csv

Technologies used:
Pandas and related libraries.

Analysis  :

The first step was to clean the data which included making sure that the data in the salary columns was numeric so we could use mathematical functions on it. We then proceeded to either get rid of the nan values by either removing them or  substituting it with the mean so as to have a more accurate representation in our graph.


Analysis Based on Average Salary:
Not all degrees grant an average pay above the national average.
The difference in average pay amongst degree holders can be substantial depending on the degree.
These degrees pay above both the national average and the average of degree holders
Some degrees don’t even pay above the national average salary



Analysis by Degree Major :
We found that not all professionals increase their salary at the same rate . 
The degrees that provide the higher salaries right out of college are not the ones that have a greater salary mid-career necessarily.
Some degrees don’t have a high starting salary but may even double by mid-career.
The rate of growth varies substantially across the different majors . Maths followed by philosophy , international relations , Economics and marketing seem to be at the top. Education , nursing, nutrition , physical assistant at the bottom . Civil engineering , business management , accounting  in the middle.

Analysis By Discipline :
We grouped the degree majors/subjects into 4 major categories of Engg, healthcare , science and arts. We found  that the  starting salaries are highest in Engineering , followed by healthcare, science and arts . By mid career the order seems to shift with science overtaking healthcare
Analysis across Type of Universities:
The salaries are the highest for Ivy league graduates followed by  Engineering, Liberal Arts , Party and state respectively in this order. The order seems to stay the same through the starting and mid career salaries and also across the percentiles . 
Ivy League grad salaries jump exponentially , they takes a lead from Engineering at about Mid_25th percentile . One interesting thing we notice is Engineering salaries starts falling behind Liberal Arts at Mid_75 percentile,even though at the start, they were much lower
The state school salaries are significantly lower than the rest of college types  and that theme. continues along the centiles , even at 90% they are way lower. There are many more state colleges in comparison to other and more no of students going there, still the salaries are much lower
The salaries at higher percentiles are higher , so it pays to get good grades. There is strong positive corelation (0.89) between Starting median salary and Mid-career median Salary.
A more specific analysis of the schools:
Top 3 starting career salaries  : CIT,MIT,Harvey Mudd with starting salaries.
Top 3 Mid career: Princeton, Yale and MIT
Lowest starting  : Morehead State University of Technology hill, Black Hills State University
Lowest Mid career: Black Hills State University and Montana 

Analysis of university salaries by region :
The best salaries are found in universities in the north-eastern region,
where the Ivy schools are, followed by the universities found in California, 
which again, not that surprising as that region has universities that are at 
the level of Ivy League schools. 

