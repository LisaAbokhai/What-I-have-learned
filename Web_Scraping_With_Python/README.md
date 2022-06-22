# Web scraping with python

## What the program does

This program goes to the novelfull website to pull novel names, chapter ends, author name and the link to the novel on the site. It filters the novels through the tags on the site called full and hot which mean they are popular and completed. It alters the url based on the site and the page. After pulling this date it stores it in a list of dictionaries that have the frozen set function used on to prevent duplication cause the same novel can appear in different genres. The list of dictionaries is later converted into a csv file called novels.csv and that file is stored in a directory called novel
