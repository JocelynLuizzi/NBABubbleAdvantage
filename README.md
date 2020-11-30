# NBABubbleAdvantage
Calculations of whether fans have an impact on referees, studied through the difference in foul calls inside and outside of the Bubble

### webscraper.py 

  provides the code written in order to scrape basketball-reference.com and create a csv of the data used in this study.

### regression.do

  contains Stata code used to run regressions. All regressions run, as well as any new variables created from the initial dataset, are done in this file.

### 2018_19_20_dataset.csv 

  Contains the full dataset used in this study. 
  
  Each unit in the dataset is one NBA game. Data includes all games from the 2018-19 and 2019-20 season. Information about each game includes the date played, the home and away team, statistics for each team, and whether or not it took place inside of the Bubble. 
