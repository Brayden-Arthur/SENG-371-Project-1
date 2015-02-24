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

Steps to apply this on a repository
* apply gitstats to chosen repo
* move the parser.py and lines_of_code.plot files to the gitstats output
* run both using python parser.py and gnuplot lines_of_code.plot respectively
* check out the simply fantasticly nice new bars on your graph indicating where a big project contributor made their first contribution

#### Predictions
I'm hoping to find that when there is a new author commiting heavily to a project we can see a visible change in the growth of the project(just using total LoC). However, I feel that since I have not factored in a ton of data it seems unlikely.


#### Data





#### Issues

So the data isn't very precise. Lines of code is not a good measure of project size and a users first contribution to a project doesn't really indicate their involvement. However it's sort of neat seeing about half the time after a top contributor makes their first contribution to a project the lines spike. With Bootstrap you can see the third contributor might have been the one to contribute the massive spike in LoC around February 2012.

Continuing on the project I would want to try and determine better ways of applying the data I can retrieve. 

For determining project size
* Having LoC and average file size compared to other similar projects to determine when one is larger that another
* Have the number of contributors factor into the project size, more contributors means a proportionally smaller project
* Factor in approximate time to completion comparing to actual completion times

For determining user contribution to a project
* See when the users are contributing most and have that factor into the graph
* Determine when a user has made a pull request and have that be their starting point
* Try and find projects that have set out deadlines to see if users are added nearer to deadlines and how that affects the new growth
* Seperate out progressive and anti-regressive changes

If all of these changes were utilized it'd be interesting to see whether or not an added user will actually change how the product grows.

