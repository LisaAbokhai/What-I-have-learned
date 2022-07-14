#  boto3 for connection with aws
#  configparser to get sensitive data from pipiline.conf file
#  to_csv to get the variable for the csv
import boto3
import configparser

#  Parse sql.conf file
parser = configparser.ConfigParser()
path = r'Extracting_With_Apis\code\sensitive.conf'
parser.read(path)

#  Create environment vars
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")


#  Connect to s3 and create bucket
s3 = boto3.client('s3',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)

s3.create_bucket(Bucket='mal-api-anime-bucket')

#  Upload the csv into s3 bucket
path = r'Extracting_With_Apis\csv\anime_favorite_rank.csv'
s3_file_name = 'anime_rank_300'
bucket_name = 'mal-api-anime-bucket'
s3.upload_file(path, bucket_name, s3_file_name)

# Check if bucket has been created
# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print(f"Bucket List: {buckets}")

