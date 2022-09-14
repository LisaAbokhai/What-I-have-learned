#  configparser to parse conf
#  psycopg2  execute Postgres SQL queries on a database
import configparser
import psycopg2

#  parse sensitive conf file 
parser = configparser.ConfigParser()
parser.read(r'Loading_Into_Redshift\sensitive.conf')

# parse the crediantials
database_name = parser.get("aws_creds", "database")
username = parser.get("aws_creds", "username")
password = parser.get("aws_creds", "password")
cluster_endpoint = parser.get("aws_creds", "host")
port = parser.get("aws_creds", "port")

#  parse arn
role_arn = parser.get("aws_boto_credentials","ARN")

# parse file_path
file_path = parser.get("extras", "file_path")

# connect to the redshift cluster
conn_string = "postgresql://{}:{}@{}:{}/{}".format(
    username,
    password,
    cluster_endpoint,
    port,
    database_name)

#  Make queries
drop_table =  """DROP TABLE IF EXISTS public.anime_ranking"""

table_creation ="""CREATE TABLE public.anime_ranking (
                    index INT,
                    id INT,
                    title TEXT,
                    rank INT
);"""

sql_query = f"""
    COPY anime_ranking
    FROM '{file_path}'
    IAM_ROLE '{role_arn}'
    csv
    DELIMITER '|'
    IGNOREHEADER 1
    ;
"""


def execute_sql(sql_query, conn_string, print_results = False):
    """Execute a SQL query on the database associated with
       a connection string """
    
    # Connect to the database
    conn = psycopg2.connect(conn_string)
    
    # Define cursor
    cur = conn.cursor()
    
    # Execute query
    cur.execute(sql_query)
    conn.commit()
    if print_results:
        print(cur.fetchall())

    # Close cursor
    cur.close()
    
    # Close connection
    conn.close()



def main():
    execute_sql(drop_table, conn_string)
    print('Table has been dropped\n')

    execute_sql(table_creation, conn_string)
    print('Tables has been created\n')

    execute_sql(sql_query, conn_string)
    print('Data has been loaded from s3 bucket into the tables')
    


if __name__ == '__main__':
        main()
