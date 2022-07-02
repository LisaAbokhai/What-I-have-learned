#  bobto3 for connection with aws
#  configparser to get sensitive data from pipiline.conf file
#  to_csv to get the variable for the csv
import boto3
import configparser



#  Parse sql.conf file
parser = configparser.ConfigParser()
path = r'C:\Users\LISA\Learning\What-I-have-learned\Extacting_data_With_S3\pipeline.conf'
parser.read(path)

#  Create environment vars
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = 'my-special-lisa-bucket'



#  Connect to s3 and create bucket
s3 = boto3.client('s3',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)

s3.create_bucket(Bucket='my-special-lisa-bucket')

#  Upload the csv into s3 bucket
path = r'Extacting_data_With_S3\csv\light_novels.csv'
s3_file = path
s3.upload_file(path, bucket_name, s3_file)

