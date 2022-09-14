#  boto3 to connect to aws
# configparse to parse sisitive vars
import boto3
import configparser


# parse sensitive.conf
parser = configparser.ConfigParser()
parser.read(r'Loading_Into_Redshift\sensitive.conf')

access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")


# Create redshift client
redshift = boto3.client( "redshift",
                        region_name = "us-east-1",  
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_key)

# Create cluster identifier
cluster_identifier = 'redshift-cluster-1'


try:
    # Delete Cluster
    redshift.delete_cluster(
        ClusterIdentifier = cluster_identifier,
        SkipFinalClusterSnapshot = True,
    )

    print(f"A cluster named {cluster_identifier} exists")
    print(f"Deleting existing cluster named {cluster_identifier}...")


    # Wait for the cluster status change to deleted
    delete_waiter = redshift.get_waiter("cluster_deleted")
    delete_waiter.wait(
        ClusterIdentifier = cluster_identifier,
        WaiterConfig = {
            "Delay": 30,
            "MaxAttempts": 20
        }
    )

    print(f"Cluster named {cluster_identifier} deleted")

except:
    print(f"A cluster named {cluster_identifier} does not exist") 