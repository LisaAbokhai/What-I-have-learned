# Import bs4 to novel details
# pandas to save data into a dataframe
# Requests to get the site's response.
# Configparser to parse user.conf

from bs4 import BeautifulSoup as bs
from requests import get
import pandas as pd
import configparser

#  Parse user.conf file
parser = configparser.ConfigParser()
path = r'Extacting_data_With_S3\user.conf'
parser.read(path)

#  Create environment var
my_user_agent = parser.get("useragent", "user_agent")

#  Would return 403 error if the user agent isn't present in headers
agent = {'User-Agent' : my_user_agent }
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

        # How often the novel is updated
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

#  Create dataframe for novels
novel_df = pd.DataFrame(books)
print(novel_df.head())