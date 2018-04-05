#! /usr/bin/env python

import psycopg2

DBNAME = "news"


def run_query(query):
    """Connection to the database and running query"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def popular_articles():
    """Query 1:- The most popular 3 articles"""

    query = """
        SELECT articles.title, COUNT(*) AS views
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;
    """
    results = run_query(query)

    # Print Results
    print('\nMOST POPULAR THREE ARTICLES BY VIEWS:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def article_authors():
    """Query 2:- Most popular article authors"""

    query = """
        SELECT authors.name, COUNT(*) AS views
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY views DESC;
    """
    results = run_query(query)

    # Print Results
    print('\nMOST POPULAR ARTICLE AUTHORS BY VIEWS:')
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1


def error_log():
    """Query 3:- Days with more than 1% errors"""

    query = """
        SELECT * from error_log_view where \"Percent Error\" > 1
    """
    results = run_query(query)

    # Print Results
    print('\nDAYS WITH MORE THAN 1% ERRORS:')
    for i in results:
        print ('# ' + str(i[0]) + ' --- ' + str(i[1]) + "% errors")

print('Results:-')
popular_articles()
article_authors()
error_log()
