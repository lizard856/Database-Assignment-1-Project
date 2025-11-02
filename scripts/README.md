#Scripts
Like I mentioned in first readme I was having an error with the original link and found another one that I think is probably it which happened to be a CSV file
With the CSV file I was able to use the MySQL workbench wizard to get it in.

As far as MySQL commands through this project here are some listed below:
1. USE testdatabase;
2. SHOW TABLES;
3. DESCRIBE library_usage;
4. SELECT * FROM library_usage LIMIT 10;
5. SELECT COUNT(*) FROM library_usage WHERE `Age Range` = '0 to 9 years';
6. SELECT AVG(`Total Checkouts`) AS avg_checkouts, AVG(`Total Renewals`)  AS avg_renewals FROM library_usage;
7. CREATE TABLE IF NOT EXISTS `{sometableName}` (put colum data)
8. CREATE DATABASE somename;
9. DROP DATABASE somename;
