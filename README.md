# movie-statz : Flatiron Data Science Mod 1 Project
Contributors: Ali Hussain and Brian Yee
In this project, we set out to determine what kind of movie would be the most profitable.
## Process
We set up an AWS RDS to store our data from different sources.
Using primarily used Python in this project for: 
- Web-scraping and API calls.
- Parsing and cleaning data.
- Executing mySQL queries to access our DB.
- Making visuals using the Matplotlib library.
## Getting our data
We used python's Beautiful Soup library to webscrape from https://www.the-numbers.com/ to get our movie data. We got data on 906 movies released from 1978-2019, and for each movie we got:
- the title
- the budget
- the domestic gross
- the international gross
- the runtime
- the MPAA rating
- the release date
- the genre
- the production type
- the creative type
We then made API calls to oMDB for each movie to get a total of 466 associated directors, writers, and actors/actresses.
After getting our data, we uploaded it into our AWS RDS using SQL queries. We used also created a junction table to associate the correct people to their respective movies so that we can determine his/her experience and average profit.
