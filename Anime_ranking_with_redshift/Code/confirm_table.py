import boto3
import pandas as pd
import io
import configparser

#  Parse sql.conf file
parser = configparser.ConfigParser()
path = r'Loading_Into_Redshift\sensitive.conf'
parser.read(path)

#  Create environment vars
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")


#  Connect to s3 
s3 = boto3.client('s3',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)



# Get object containing file to be staged
obj = s3.get_object(Bucket = "mal-api-anime-bucket", Key = "anime_rank_300.csv")


# Print colummns info for the dataset
pd.read_csv(io.BytesIO(obj["Body"].read()), sep= '|').info()