# Data Analysis Report

Three charts were generated to tell the stories about the data acquired to the reader, according to the approved research questions discussed in Milestone One. These questions explored connections between two variables that influences the outcomes of a Major League Baseball (“MLB”) game - salary to Run Batted In (“RBI”), and RBI to the player's month born. Three charts were developed using Matplotlib and pandas, and each will be discussed in isolation from the other.

## Player Salary to RBI
    
The authors investigated if the player’s salary is aligned with the number of RBIs made who have since retired from MLB in 2024. A scatter chart was developed.

![Chart 1: Player Salary to RBI](chart1.png)
*Figure 1. Player Salary to RBI*

The authors decided a scatter chart with a trendline would best communicate if there is a relationship between RBIs and salary. The highest paid player had zero RBIs. Additionally, a p-value, or a measurement of randomness in the data, was calculated to be over 0.05, showing no relationship between salary and RBI. The coefficient of determination, known as “r-squared” throughout the remainder of this document, was used to test if one variable influences the other. This value was calculated to be close to zero, showing no correlation between salary and RBI. Clearly, there is another variable that affects the salary a player receives other than an RBI.

## Player Birth Month to RBI

The authors investigated if the month the retired player was born aligns with the total number of RBIs a player made who have since retired from the MLB in 2024. To tell this story, a bar chart was developed. 

![Chat2: Player Birth Month to RBI](chart2.png)
*Figure 2. Player Birth Month to RBI*

The X axis had the birth month, and the Y axis had the total RBIs of all players who were born within that month. The lowest RBI month was May, with a total RBI was about 135,000. The highest RBI was October, with a total RBI of about 172,000. The difference between low and highs is about 25%. Per the decided cutoff as discussed in Milestone 1, this exceeds the cutoff showing a correlation between the two variables. Other factors may influence this, including the average birth month of the global population, or related factors. Unlike the first cart, p-values and r-squared was not calculated.

## PLayer's Salary from 1984 to 2024 in 2026 Dollars

The authors decided to explore the yearly salary of all players from 1984 - 2024. This chart explains how much the average player makes. The X axis contains the year, and the Y axis contains the yearly average sum of all player's saleries, adjusted to 2026 dollars. 

![Chart 3: Player Average Salary from 1984 - 2024](chart3.png)
*Figure 3. Player Average Salary from 1984 - 2024* 

This shows the baseball players are making more money each year, on average. In theory, this shows how good they are as players and could have a connection to how many RBIs the average player hits. Like the second chart, p-values and r-squared was not calculated. 