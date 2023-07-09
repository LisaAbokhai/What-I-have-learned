# Anime Ranking Data

This repository contains a Python project that pulls anime rankings data from MyAnimeList using the site's API and performs various data processing tasks using Python, Pandas, Configparser, Pyspark, and Jupyter Notebook.

## Features

- Pulls anime rankings data from MyAnimeList API using Requests
- Stores the data as a CSV file using Pandas
- Loads the CSV file into an S3 bucket created in the code file
- Retrieves data from S3 and performs column manipulations and renaming using Pyspark
- Saves the processed data as a parquet file

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.10)
- Pandas (version 1.4.2)
- Configparser (version 5.2.0)
- Pyspark (version 3.3.0)
- Jupyter Notebook (version 6.4.12)
