# Extract And Load data

## Description

This project scraps data from <https://www.novelupdates.com/series-ranking/?rank=popular> and gets the details of light novels, such as; title, chapters, links to the novel description etc then it pulls all that data into a pandas datframe which is then loaded into a mysql database.

Later, it pulls all the data from the mysql database and stores it into a csv file which is then loaded into a S3 bucket that is created in the same code file.

## Purpose

This project is used to practice the first two stages of an elt pipeline and the full extraction process.
