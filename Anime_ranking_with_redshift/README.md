# S3 to Redshift

This project focuses on loading data from an S3 bucket into a Redshift database. It involves creating a table in the Redshift database and then loading the anime-ranking CSV file, which was created in the "Anime_ranking_api_pull" project. The CSV file is deleted after the data is successfully loaded into Redshift.

## Purpose

The purpose of this project is to familiarize oneself with the process of loading data into a data warehouse, specifically Redshift. By completing this project, one will gain hands-on experience in setting up the necessary infrastructure, creating a table, and loading data from an external source into Redshift.

## Features

- Creates a table in a Redshift database matching the structure of the anime-ranking data.
- Loads the anime-ranking CSV file from an S3 bucket into the Redshift table.
- Handles the connection to the Redshift cluster and performs the necessary data loading operations.
- Supports configuration through the sensitive.conf file, allowing easy customization of Redshift and S3 settings.
- Deletes the CSV file from the S3 bucket after successfully loading the data into Redshift.
- Provides a clean-up section to delete the Redshift table and remove any temporary resources created during the project.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.10)
- Pandas (version 1.4.2)
- Configparser (version 5.2.0)
- Pyspark (version 3.3.0)
