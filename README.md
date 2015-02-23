## SENG-371-Project-1

### An analysis of brooks law/a look into how a new programmer working on a project might affect its evolution on github projects

Since my previous question was a bit too hard to accomplish I have set about on something I can hopefully accomplish

1.Using CodeAnalyzer/Gitstats to determine where there are expansions in a codebase based on lines of code/amounts of files
2.Using the github api to see where and when there have been pull requests as well as if they have been merged

revised project completion date: February 23
*trying to finish new data collection by 20th
*hopefully will be done analysis of data by sunday 22nd
*might have a day to try and automate it



-----------------------------------------------------------------------------------------------------------------------------


#### Data analysis
I found that using gitstats on a repo gave me access to pretty much all the data I needed. It has each authors start date, the file count on a given date, the LoC on a given date and the commits by author.

The gitstats example folder contains the output when gitstats was used to analyze bootstrap.

I've modified the lines of code gnuplot to also show when an author has begun contributing to a project. This will only show when the biggest contributors started.

#### Predictions
I'm hoping to find that when there is a new author commiting heavily to a project we can see a visible change in the growth of the project(just using total LoC)



