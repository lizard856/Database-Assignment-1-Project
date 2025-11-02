import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CreatingDatabaseU4Me@",
    database="testdatabase"
)
mycursor = db.cursor()

def exportable(mycursor):

    print("***library_usage is used for demo***")

    # asking what file type wanted
    print("\nYou have two export options to choose from:")
    print("1. Excel aka .xlsx")
    print("2. CSV aka .csv")
    choice = input("\nJust enter 1 or 2 depending on your choice: ") #btw love how input has lines not needing somthing like cout

    if choice != "1" and choice != "2": #just making sure user entered these values
        print("Umm again only 1 or 2 :/")
        exit()

    # getting colums using connector commands like execute for the structure of library
    # and IMPORTANTLY fetchall for getting mySQL rows into python list
    # I'm viewing it like a fixed array for C++
    mycursor.execute("DESCRIBE library_usage") #apparently f needed to formate string
    columns_data = mycursor.fetchall()

    #Colums into vector to print out.
    columns = [] #ESsentially my vector
    for row in columns_data: #data from above
        columns.append(row[0]) #going through and adding names to colum (.append built in PY)

    #Nothing fancy here just printing it
    print("\nHere's a list of the colums:")
    for col in columns:
        print(col)

    # colums to export
    print("Warning:: if you enter multiple and some are invalid only valid names/correct will export")
    cols_input = input("Otherwise Enter the names you want to see (, is separater for multiple or just use ALL): ")

    #I don't want caps to matter! otherwise all easy just keep all.
    if cols_input.lower() == "all":
        selected_cols = columns
        #essentially same as SELECT * FROM library_usage in SQL
    else:
        selected_cols = []
        #got a cool function for separating colium this case "," using .split
        #then loop checks if in list and keeps it if so.2
        pieces = cols_input.split(",")
        for p in pieces:
            p = p.strip()
            if p in columns:
                selected_cols.append(p)

        if len(selected_cols) == 0:
            print("No valid columns found")
            exit()

    # how many rows are wanted to be visible
    limit = input("How many rows do you want to see ")
    try:
        limit = int(limit)
    except:
        print("Really just really! All you needed was a number.")
        exit()

    # finally the SQL stuff/building a query
    for i in range(len(selected_cols)): #basic for loop going through all selected
        selected_sql_cols += "`" + selected_cols[i] + "`"
        if i != len(selected_cols) - 1:
            selected_sql_cols += ", "

    #Really I'm just telling mysql the command: SELECT `Age Range`, `Patron_Type` FROM library_usage LIMIT 50;
    query = "SELECT " + selected_sql_cols + " FROM `library_usage` LIMIT " + str(limit)
    mycursor.execute(query)
    rows = mycursor.fetchall()

    #I imported pandas after finding out it easily creates the data table and has functions for EXCEL/CSV
    #this is putting selected colums into the data table so that it's formated for excel/CSV
    easyData = pd.DataFrame(rows, columns=selected_cols)

    #NowAgain using the pandas import I'm able to export to CSV or ecel using the data created.
    if choice == "1":
        easyData.to_excel("export.xlsx", index=False)
        print("Nice it's saved as export.xlsx")
    else:
        easyData.to_csv("export.csv", index=False)
        print("Nice it's saved as export.csv")

#simple function for creating and deleting mysql tables
def OhTables(mycursor, db):
    newTable = input("Cool what would you like your new table to be called: ").strip() # BTW.strip is awesome! Removes whitespaces so you can just enter names!
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS `{newTable}` (id INT, note TEXT)") # just a very simple table with two colums id and note (nothing added to them though)
    # oh also IF NOT EXISTS so it doesn't crash from duplication

    #just getting all table names and printing them
    mycursor.execute("SHOW TABLES")
    tables_data = mycursor.fetchall()
    tables = []
    for row in tables_data:
        tables.append(row[0])
    print("Here are the tables:")
    for t in tables:
        print(t)

    #Allowing you to delete the tables and again using , to know separated with strip
    delete_input = input("Enter table names to delete (separate with commas): ").strip()
    names = [t.strip() for t in delete_input.split(",") if t.strip()]  # clean list

    deleted = []
    notFound = []

    VERYprotected = "library_usage"

    # for loop that is deleting names except library_usage since that's the demo
    for name in names:
        if name == VERYprotected:
            print("NO NO NO deleting 'library_usage'.")
            continue
        if name in tables:
            mycursor.execute(f"DROP TABLE `{name}`")
            deleted.append(name)
        else:
            notFound.append(name)

    #pushing to the database and saying what deleted or not
    db.commit()

    if deleted:
        print("Deleted tables:", ", ".join(deleted))
    if notFound:
        print("Not found:", ", ".join(notFound))
    if not deleted and not notFound:
        print("No valid table names entered.")

#will run immediatly since not in function (weird python thing)
print("\nWelcome to the Handy Dandy SanFran Library App")
print("1. Export data")
print("2. Manage table")
choice = input("What option would you like today? ")
if choice == "1":
    exportable(mycursor)
elif choice == "2":
    OhTables(mycursor, db)
else:
    print("Sorry, only 1 or 2.")

#just finishing database
mycursor.close()
db.close()
