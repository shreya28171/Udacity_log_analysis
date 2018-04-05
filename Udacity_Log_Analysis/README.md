# Log-Analysis
## Udacity Project 3

## Description
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

## Project contents

This project consists of the following files:

* log_analysis.py - This file contains the queries which will display the desired result.
* log_output.txt - This file shows the output of log_analysis.py file in text format.
* README.md- It describes documnetation of the project.

## How to run the project

### PreRequisites:
* Python3 should be installed.
* Vagrant should be installed.
* Virtual-Box should be installed.

### Setup-
* Install Vagarant and Virtual-Box.
* Download this folder.
* Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip" rel="nofollow">data</a> from here.</li>
* Unzip this folder.

### Launch-
* Launch the Vagrant VM inside the Vagrant directory in the downloaded folder using command-
$ vagrant up

* Then log into using this command-
$ vagrant ssh

* Change directory to /vagrant and ls looking for this folder downloaded.

### Setting up the Database
* Load file newsdata.sql into local database using command-
  psql -d news -f newsdata.sql
* Use psql -d news to connect to database.

### Creating Views-
* Created error_log_view-
  create view error_log_view as select date(time),round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) order by "Percent Error" desc;

### Running the queries
* From the vagrant directory inside virtual machine run log_analysis.py using-
$ python3 log_analysis.py

## Bugs and feature requests

Have a bug or a feature request? contact me (See Contact info BELOW)

## Contact

* shreya28171@gmail.com

