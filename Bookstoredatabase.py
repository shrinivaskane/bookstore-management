#Program to demonstrate database
#Import the required packages

import sqlite3

#create a database or open connection if exists
conn=sqlite3.connect("bookstore.db") #establishes the connection with database
print("Opened database succesfully")


#statement to create table
conn.execute("CREATE TABLE ADMIN(\
                                     A_USERNAME CHAR(50) PRIMARY KEY NOT NULL,\
                                     A_PASSWORD CHAR(50) NOT NULL);")

conn.execute("CREATE TABLE BOOK(\
                                     B_NAME CHAR(30) PRIMARY KEY NOT NULL,\
                                     B_AUTHOR CHAR(40) NOT NULL,\
                                     B_PRICE INT NOT NULL,\
                                     NO_OF_BOOKS INT NOT NULL,\
                                     A_USERNAME CHAR(50),\
                                     FOREIGN KEY(A_USERNAME) REFERENCES ADMIN(A_USERNAME));")
conn.execute("CREATE TABLE CUSTOMER(\
                                     C_EMAILID CHAR(40) PRIMARY KEY NOT NULL,\
                                     C_PASSWORD CHAR(20) NOT NULL,\
                                     C_ADDRESS CHAR(50) NOT NULL,\
                                     C_PHONE INT NOT NULL);")

conn.execute("CREATE TABLE BUYS(\
                                     B_NAME CHAR(30) NOT NULL,\
                                     C_EMAILID CHAR(40) NOT NULL,\
                                     PRIMARY KEY(B_NAME,C_EMAILID));")

#print the result
print("Table created succesfully")

