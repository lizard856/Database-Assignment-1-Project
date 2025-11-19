from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["testdatabase"]
collection = db["library_usage"]

def exportable(mycursor):

    print("***library_usage is used for demo***")

    # asking what file type wanted
    print("\nYou have two export options to choose from:")
    print("1. Excel aka .xlsx")
    print("2. CSV aka .csv")
    choice = input("\nJust enter 1 or 2 depending on your choice: ") #btw love how input has lines not needing somthing like cout

    if choice != "1" and choice != "2": #just making sure user entered these values
        print("Umm again only 1 or 2 :/")
        return

    # getting colums using connector commands like execute for the structure of library
    # and IMPORTANTLY fetchall for getting mySQL rows into python list
    # I'm viewing it like a fixed array for C++
    sample_doc = collection.find_one()
    if not sample_doc: #just testing if empty
        print("Collection is empty.")
        return

    #Colums into vector to print out.
    columns = [k for k in sample_doc.keys() if k != "_id"] #ESsentially my vector
    
    print("\nHere is a list of the fields:")
    for col in columns:
        print(col)
    #data from above
    #going through and adding names to colum (.append built in PY)

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
        return

    # finally the SQL stuff/building a query
    projection = {field: 1 for field in selected_cols}
    # do not include _id unless the user explicitly asked for it
    projection["_id"] = 0

    cursor = collection.find({}, projection).limit(limit)
    rows = list(cursor)

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

#will run immediatly since not in function (weird python thing)
print("\nWelcome to the Handy Dandy SanFran Library App")
print("1. Export data")
print("2. Manage table")
choice = input("What option would you like today? ")

if choice == "1":
    exportable(collection)
elif choice == "2":
    # very simple management example for MongoDB
    new_name = input("Cool what would you like your new collection to be called: ").strip()
    if new_name:
        db[new_name].insert_one({"init": True})  # creates collection lazily
        print(f"Created collection {new_name} (with one placeholder document).")

    print("Here are the collections:")
    collections = db.list_collection_names()
    for c in collections:
        print(c)

    delete_input = input("Enter collection names to delete (separate with commas): ").strip()
    names = [t.strip() for t in delete_input.split(",") if t.strip()]

    VERYprotected = "library_usage"

    deleted = []
    not_found = []

    for name in names:
        if name == VERYprotected:
            print("NO NO NO deleting 'library_usage'.")
            continue
        if name in collections:
            db[name].drop()
            deleted.append(name)
        else:
            not_found.append(name)

    if deleted:
        print("Deleted collections:", ", ".join(deleted))
    if not_found:
        print("Not found:", ", ".join(not_found))
    if not deleted and not not_found:
        print("No valid collection names entered.")
else:
    print("Sorry, only 1 or 2.")