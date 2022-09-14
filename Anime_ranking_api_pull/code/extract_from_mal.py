#  request to get response from api
# json to load json
#  Configparser to pull clientinfo
# pandas to load dataframe into a csv

import requests
import json
from configparser import ConfigParser
import pandas as pd

#  'My anime list' api url
api_url = 'https://api.myanimelist.net/v2/anime/ranking'

#  Filter by favorite anime in anime rank and limit by 200
ranking_type = 'favorite'
limit = 300
rank_params = {'ranking_type' : ranking_type, 'limit' : limit}

# Read pipeline cinfiguration file
parser = ConfigParser()
parser.read(r'Extracting_With_Apis\code\sensitive.conf')

#  user agent for headers
client = parser.get("api_client_detail", "client_id")
auth = {'X-MAL-CLIENT-ID' : client }


#  Combine dicitionaries to form one
def Merge(dict1, dict2, dict3):
        """_summary_

        Args:
            dict1 (dictionary): single key and value
            dict2 (dictionary): single key and value
            dict3 (dictionary): single key and value

        Returns:
            dictionary: combination of all 3 dictionaries into 1 dictionary
        """
        res = {**dict1, **dict2, **dict3}
        return res


def main():

        api_response = requests.get(api_url, params = rank_params, headers= auth)   
        json_response = json.loads(api_response.content)

       
        #  Store values gotten from api in this var
        anime_rank = []

        #  Loop through data got get values
        for anime_info in json_response['data']:

                #  Get the important from the json response
                id  = {'id' : anime_info['node']['id']}
                title = {'title' : anime_info['node']['title']}
                rank = anime_info['ranking']

                #  Merge the dictionaries to parse them as one unit
                add_dict = Merge(id, title, rank)     

                # Add to dictionary to list
                anime_rank.append(add_dict)
              


        anime_dataframe = pd.DataFrame(anime_rank)
        anime_dataframe.index.name = 'index'  # create index coloumn name
        print(anime_dataframe.head())
        anime_dataframe.to_csv(r'Extracting_With_Apis\csv\anime_favorite_rank.csv', sep = '|')


if __name__ == '__main__':
        main()

