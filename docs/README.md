# Project Name
The Database APP

## Description
From the instructions a lot of the time was trying to figure out what I was really trying to do. From what I was able to understand I was getting the database from the San fransico library and getting this running in mysql. From here it was about implementing it with a fairly simple python command line app. I don't have a lot experience with python so that was my primary focus was to better figure it out along with using the mysql connector so that I could use python commands to work with mysql. The application itself calls from the mysql database which was added with the help of the mysql CSV wizard importer. You then just have to connect to the database with your password and data base name. When you run the application it will allow you to export data from the library_usage table or create and delete template tables within the database. When exporting data you will be asked what colums you want exported and whether you want CSV or excel formate. 

## Installation
The steps to install:
1. Download the database -> https://www.kaggle.com/code/vidhyasankari/sanfrancisco-library-usage/input (note the link to the original dataset wasn't working so I found this one)
2. Open a database in mysql workbench and right click tables and click data import wizard and go through the prompts
3. Then check it's working with simple commands 
USE testdatabase; (database name)
SHOW TABLES;
SELECT * FROM library_usage LIMIT 10; (it should show you 10 colums with data)
4. In the DatabaseApp.py just change the password and database name to yours and you should be able to run the application via terminal

## Acknowledgements
I watched a bunch of python and mysql videos in order to figure out how to use commands and do things like getting a CSV into mysql
Also like any time doing a project like this when I got stuck in the code I would search for other ways or options. 
Clear example of that is how to export csv or excel which lead me to using import pandas as pd