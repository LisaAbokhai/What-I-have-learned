#  pymysql to crate connection to mysql
#  csv to write the query result into a csv file
# configparser to pull sensitive infomation from csql.conf file
import pymysql
import csv
import configparser

#  Parse sql.conf file
parser = configparser.ConfigParser()
path = r'C:\Users\LISA\Learning\What-I-have-learned\Extacting_data_With_S3\sql.conf'
parser.read(path)

#  Create environment vars
hostname = parser.get('mysql', 'hostname')
username = parser.get('mysql', 'username')
port = parser.get('mysql', 'port')
database = parser.get('mysql', 'database')
password = parser.get('mysql', 'password')

#  Connect to mysql database
con = pymysql.connect(host = hostname,
                      user = username,
                      password = password,
                      db = database,
                      port = int(port))

if con is None:
 print("Error! check variables")
else:
 print("good to go")


# Query for fulll extraction of data from mysql db
book_query = "SELECT * FROM books;"
book_cursor = con.cursor()
book_cursor.execute(book_query)
results = book_cursor.fetchall()

#  Make csv file to hld them querry result
csv_filename = "light_novels.csv"

with open(csv_filename, 'w', encoding= 'utf-8') as file:
    csv_writer = csv.writer(file, delimiter='|')
    csv_writer.writerows(results)

    #  Close file and connection
    file.close()
    book_cursor.close()
    con.close()

