# My Fun Projects

This repository contains a collection of projects that I built myself while learning new things and exploring various tools. Each project was a learning experience and an opportunity to have fun while building something from scratch.

## Projects

Here are some of the projects included in this repository:

1. **Anime_ranking_api_pull**: This project utilizes the MyAnimeList API to retrieve the list of ranked favorite anime from the MyAnimeList website. The API endpoint used is <https://api.myanimelist.net/v2/anime/ranking>.
   - Tools used: Pandas, AWS S3, Requests
   - Key features: Pulls the list of ranked favorite anime from MyAnimeList website, Utilizes the MyAnimeList API, Retrieves 300 entries from the ranking

2. **Anime_ranking_with_redshift**: This project focuses on loading data from an S3 bucket into a Redshift database. It involves creating a table in the Redshift database and then loading the anime-ranking CSV file, which was created in the "Extracting_With_Apis" project. The CSV file is deleted after the data is successfully loaded into Redshift.

   - Tools used: AWS S3, AWS Redshift, Pandas
   - Key features: Creates a table in a Redshift database matching the structure of the anime-ranking data., Loads the anime-ranking CSV file from an S3 bucket into the Redshift table., Handles the connection to the Redshift cluster and performs the necessary data loading operations.

3. **Copy_Files_Function**: This program copies file(s) from the original path and loads the copied file(s) into folder(s) based on the number of pages of each file.

   - Tools used: Glob, Shutil
   - Key features: Based on the number of pages, the program creates a new folder within the program directory, This process is repeated for each file found in the original path, Once all file(s) are copied and loaded into the respective folder(s), the program completes.

## Motivation

The motivation behind creating these projects was to apply my learning and explore new tools in a practical and hands-on manner. I believe that building projects is a great way to solidify concepts, discover challenges, and gain a deeper understanding of various technologies.

## Technologies Used

Throughout these projects, I had the opportunity to work with a diverse set of technologies, including:

- AWS
- Pandas
- Jupyter Notebook

These tools provided me with valuable insights and expanded my skillset, allowing me to tackle a wide range of challenges.

## Contributing

Feel free to explore the projects in this repository and provide feedback or suggestions. If you have any ideas for new projects or improvements to existing ones, contributions are always welcome! Simply fork this repository, make your changes, and submit a pull request.

Let's learn and have fun together!
