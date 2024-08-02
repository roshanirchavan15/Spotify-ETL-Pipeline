Dataset
The dataset used for this project is available on Kaggle: https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023

Project Overview
This project involves developing an ETL (Extract, Transform, Load) data pipeline for Spotify data using various AWS services. The main components of the pipeline include Amazon S3 for data storage, AWS Glue for data transformation, and Amazon Athena for querying the transformed data. The goal is to clean, join, and transform the raw data, resulting in a structured data warehouse in S3, and create a database with tables using AWS Glue Crawler.


Components and Process
Amazon S3 (Staging Folder):

The raw Spotify dataset is stored in the Amazon S3 staging folder.
Amazon Glue:

Data transformation tasks are performed using AWS Glue. This includes data cleaning, joining tables, and dropping unnecessary fields.
Amazon S3 (Target Folder):

The transformed data is stored in the Amazon S3 target folder as a data warehouse.
Amazon Glue Crawler:

AWS Glue Crawler is used to create databases and tables from the transformed data stored in S3.
Amazon Athena:

Amazon Athena is used for querying the transformed data to derive insights and perform analysis.
Detailed Description
Data Extraction:

The raw Spotify dataset is first uploaded to the Amazon S3 staging folder. This is the starting point of the ETL pipeline.
Data Transformation:

AWS Glue is used to perform data transformation tasks. The raw data undergoes cleaning to remove any irrelevant or corrupted entries. Tables from the dataset are joined based on key fields such as artist_id and track_id. Unnecessary fields are dropped to streamline the dataset.
Data Storage:

The transformed data is then stored in the Amazon S3 target folder. This serves as the data warehouse, which is organized and optimized for querying.
Database and Table Creation:

AWS Glue Crawler scans the transformed data in S3 and automatically creates the necessary databases and tables. This makes the data ready for analysis with minimal manual intervention.
Data Querying:

Amazon Athena is used to run SQL queries on the transformed data stored in S3. This allows for efficient querying and analysis to derive actionable insights from the Spotify dataset.
