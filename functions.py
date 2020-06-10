import csv
import sys
import SECRETS
import SEARCH

def readCsv():
    with open(SECRETS.csvFile) as csv_file:
        list = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                list.append(row)
                line_count += 1
        #print(list)
        return list


def writeCsv(list):
    with open(SECRETS.csvFile, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in list:
            csv_writer.writerow(row)

def addDB():
    last_id = 0

    db = readCsv()
    last_id = int(db[db.__len__() - 1][0])
    id = last_id + 1
    base = input("Base: >")
    modifier = input("Modifier: >")
    flavoring = input("Flavoring: >")
    filler = input("Filler: >")
    solids = input("Solids: >")
    spices = input("Spices: >")
    name = input("Name: >")

    item = [str(id), base, modifier, flavoring, filler, solids, spices, name]
    writeCsv([*db, item])

    print("The new record were added, too see it select -Display-")

def displayDB():
    db = readCsv()
    first = True
    for row in db:

        print('%-20s | %-20s | %-20s | %-20s | %-20s | %-20s | %-20s | %-20s' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        if first:
            print("---------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------")
            first = False
        #print(row)

def searchDB(possible_searches):

    # read csv

    csv_file = csv.reader(open('cock.csv', "rb"), delimiter=",")

    # loop through csv list

    for row in csv_file:
        if SEARCH.search_id == row[0]:
            print('row')
        elif SEARCH.search_base == row[1]:
            print('row')
        elif SEARCH.search_modifier == row[3]:
            print('row')
        elif SEARCH.search_flavoring == row[4]:
            print('row')
        elif SEARCH.search_filler == row[5]:
            print('row')
        elif SEARCH.search_solids == row[6]:
            print('row')
        elif SEARCH.search_spice == row[7]:
            print('row')
        else:
            print('Please try again.')

def delDB():
    searchDB(SEARCH.possible_searches)
    print("\n")
    toDel = input("Pls write the ID of the row to delete: >")
    ans = input("do you rly wanna del this shit? yes/no >")
    if ans.lower() == "yes":
        db = readCsv()
        for row in db:
            if str(row[0]) == str(toDel):
                db.remove(row)
        writeCsv(db)
        print("The item with the ID: %s were removed" % toDel)
    else:
        print("Deleting canceled")

def cocktailSelection():
    # possible choices: AddNew, Display, Search
    # fields = ['ID', 'Base', 'Modifier', 'Flavoring', 'Filler', 'Solids', 'Spices', 'Name']

    choice = ""

    while choice.lower() != 'x':
        print("""What would you like to do?
            1 - Add new record
            2 - Display
            3 - Search
            4 - Delete a record
            Press x to exit.""")

        choice = input(">")

        if choice == "1":
            addDB()

        elif choice == "2":
            displayDB()

        elif choice == "3":
            search_choice = input("""What would you like to search for?
                                     Enter ID, Base, Modifier, Flavoring, Filler, Solids or Spices""")
                    
            if search_choice.lower() == 'id':
                searchDB(SEARCH.search_id)

            if search_choice.lower() == 'base':
                searchDB(SEARCH.search_base)

            if search_choice.lower() == 'modifier':
                searchDB(SEARCH.search_modifier)

            if search_choice.lower() == 'flavoring':
                searchDB(SEARCH.search_flavoring)

            if search_choice.lower() == 'filler':
                searchDB(SEARCH.search_filler)

            if search_choice.lower() == 'solids':
                searchDB(SEARCH.search_solids)

            if search_choice.lower() == 'spices':
                searchDB(SEARCH.search_spice)            

        elif choice == "4":
            delDB()
            
        elif choice.lower() == "x":
            print("Thank you! Shutting down.")
        else:
            print("Sorry, I didnt recognise that option")

        if not choice.lower() == "x":
            print("\n\n"
                  "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")