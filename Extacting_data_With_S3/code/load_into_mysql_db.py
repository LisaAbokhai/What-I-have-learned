# pandas for dataframe
# sqlalchemy to create engine fore connection
# configparser to parse sql.conf file
# get_novel to get the dataframe with the data

import pandas as pd
from sqlalchemy import create_engine
import configparser
import get_novels

#  Parse sql.conf file
parser = configparser.ConfigParser()
path = r'C:\Users\LISA\Learning\What-I-have-learned\Extacting_data_With_S3\sql.conf'
parser.read(path)

#  Create environment variables
hostname = parser.get('mysql', 'hostname')
username = parser.get('mysql', 'username')
database = parser.get('mysql', 'database')
password = parser.get('mysql', 'password')


#  Create engine for coneneection
sqlEngine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

#  Load dataframe into MySQL database
get_novels.df.to_sql(con=sqlEngine, name='books', if_exists='replace', index=False)