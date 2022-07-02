# import bs4 to extract based on my filter, 
#  Save data from web scraope into a
# requests to get the site.

from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd


#  Would return 403 error if the user agent isn't present in headers
agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
url = 'https://www.novelupdates.com/series-ranking/?rank=popular&pg='

# list to hold the novel output
books = []

# loop through each page to get the contents
for page in range(1, 518):

    pg = str(page)
    connector = f'{url}{pg}'
    response = get(connector, headers= agent)

    soup = bs(response.text, 'html.parser')
    novels = soup.findAll('div', attrs= {'class' : 'search_body_nu'})


    for novel in novels:     
        
        #  Title of the book
        to_get_title_rank = novel.find(attrs= {'class': 'search_title'})
        title = to_get_title_rank.find('a').text

        # ranking of the novel on the site
        rank_str = to_get_title_rank.find(attrs = {'class' : 'genre_rank'}).text
        rank_num = rank_str.lstrip("#")
        rank = int(rank_num)


        # number of chapters in book
        to_get_chapter= novel.find('span' , attrs ={'class' : 'ss_desk'})
        chapter_str = to_get_chapter.text
        chapter_num = chapter_str.rstrip(" Chapters")
        chapter = int(chapter_num)

        #  Link to book info
        url_to_novel_info = to_get_title_rank.a['href']

        #  find if the complete tag exists
        complete= novel.findAll('a', attrs = {'class' : 'gennew complete'})

        # How often the novel is updated if it's not complete
        update_frequency = to_get_chapter.find_next('span' , attrs ={'class' : 'ss_desk'}).text

        #  if the complete tag exists in the novel then yes if not no
        if len(complete) > 0:
            completed = 'Yes'
        else:
            completed = 'No'

        
        books.append({'Title' : title, 'Rank' : rank,
                    'Chapters' : chapter, 
                    'Link' : url_to_novel_info , 'Completed' : completed, 
                    'Update_Frequency' : update_frequency})


df = pd.DataFrame(books)
print(df.head())