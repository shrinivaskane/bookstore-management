import sqlite3
#create a database or open connection if exists
conn=sqlite3.connect("bookstore.db") #establishes the connection with database
print("Opened database succesfully")

#display the data from BOOKSTORE database

#DISPLAY ADMIN TABLE
cursor=conn.execute("SELECT * FROM ADMIN")

#ITERATE OVER THE DATA
for row in  cursor:
    print("ADMIN USERNAME:",row[0])
    print("ADMIN PASSWORD:",row[1])

print("\n\n")
#DISPLAY BOOK TABLE
cursor=conn.execute("SELECT * FROM BOOK")

#ITERATE OVER THE DATA
for row in  cursor:
    print("\nBOOK NAME:",row[0])
    print("BOOK AUTHOR:",row[1])
    print("BOOK PRICE:",row[2])
    print("NO OF BOOK COPIES:",row[3])
    print("ADMIN ADDIING THE BOOK:",row[4])

print("\n\n")
#DISPLAY CUSTOMER TABLE
cursor=conn.execute("SELECT * FROM CUSTOMER")

#ITERATE OVER THE DATA
for row in  cursor:
    print("\nCUSTOMER EMAIL_ID:",row[0])
    print("CUSTOMER PASSWORD:",row[1])
    print("CUSTOMER ADDRESS:",row[2])
    print("PHONE NUMBER:",row[3])

print("\n\n")
#DISPLAY CUSTOMER TABLE
cursor=conn.execute("SELECT * FROM BUYS")

#ITERATE OVER THE DATA
for row in  cursor:
    print("\nBOOK NAME:",row[0])
    print("EMAIL ID:",row[1])

print("Operation done successfully")

#close the database
conn.close()
