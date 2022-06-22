#import bs4 to extract based on my filter, 
# csv to transform the data extracted into a csv,
#  os to put the csv file in a folder,
#  requests to get the site.

from bs4 import BeautifulSoup as bs
import csv
import os
from requests import get


genres = ['Comedy', 'Martial+Arts', 'Sci-fi', 'Gender+Bender',\
     'Mature', 'Fantasy', 'Tradedy', 'Adventure', 'Psychological', 'Xianxia',\
         'Wuxia', 'Historical', 'Slice+of+Life','Adult', 'Josei', 'Mecha', 'Yaoi' ]
         
url = 'https://novelfull.com/genre/'

# list to hold the novel output
p_and_c_novels = []

#loop through each gerne to get the contents
for genre in genres:
    for page in range(1, 18):
    
        pg = str(page)
        connector = f'{url}{genre}?page={pg}'
        response = get(connector)

        soup = bs(response.text, 'html.parser')

        #there are multiple class=row headers that point to different things 
        # so this variable is used to limit the range of the search
        limiter = soup.find('div', attrs={'class' : 'list list-truyen col-xs-12'}) 
        novels = limiter.findAll(attrs= {'class' : 'row'})




        for novel in novels:

            search = str(novel.find_all('span'))

            # the tags full and hot
            popular= '<span class="label-title label-hot"></span>'
            complete = '<span class="label-title label-full"></span>'

            
            # filter through the novels to find the completed and popular novels
            if (popular in search) and (complete in search):

                to_get_title = novel.find('h3', attrs= {'class': 'truyen-title'})
                title = to_get_title.find('a').text
                whitespace_author = novel.find('span', attrs= {'class' : 'author'}).text
                to_get_chapter= novel.find('div' , attrs ={'class' : 'col-xs-2 text-info'})
                chapter = to_get_chapter.find('a').text
                end_of_url = to_get_title.a['href']
                url_to_novel = f'https://novelfull.com{end_of_url}'

                author = whitespace_author.strip()
                
    

                
                p_and_c_novels.append({'Title' : title, 'Author' : author,\
                     'Chapter End' : chapter, 'Link' : url_to_novel})
                    
                # prevent duplication
                # the for loop would cause duplication and the same novel occurs in different genres
                dict_set = set(frozenset(d.items()) for d in p_and_c_novels)
                all_novels = [dict(s) for s in dict_set]
                print('Adding to list')

            else:
                continue
            
print(all_novels) 


# Create folder called novel to hold the csv file
directory_name = 'novel'

if not os.path.exists(directory_name):   # Make novel folder if it does not exist
     os.makedirs(directory_name)

#header
keys = all_novels[0].keys()

with open('novel/novels.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_novels)


