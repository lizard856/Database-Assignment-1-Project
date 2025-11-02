import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CreatingDatabaseU4Me@",
    database="testdatabase"
)

mycursor = db.cursor()

#simple result to get 0-9 year olds.
query = """SELECT COUNT(*) FROM `library_usage` WHERE `Age Range` = '0 to 9 years';"""
mycursor.execute(query)
result = mycursor.fetchone()[0] #not fetchall because wanting just a single one.
print("number aged 0 to 9 years:", result)

# overall averages
query = """SELECT AVG(`Total Checkouts`) AS avg_checkouts, AVG(`Total Renewals`)  AS avg_renewals FROM `library_usage`;"""
mycursor.execute(query)
avg_checkouts, avg_renewals = mycursor.fetchone()
print("total checkouts:", avg_checkouts)
print("total renewals:", avg_renewals)

mycursor.close()
db.close()