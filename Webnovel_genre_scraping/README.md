# Web scraping with python

## What the program does

This program goes to the Novelfull website to pull novel names, where the chapter ends, the author of the novel and the link to the novel on the site. It filters the novels through the tags on the site called full and hot which means they are completed and popular. It alters the URL based on the genre and the page.

After pulling this date it stores it in a list of dictionaries with the frozen set function used to prevent duplication because the same novel can appear in different genres. The list of dictionaries is later converted into a CSV file called novels.csv and that file is stored in a directory called novel
