import sqlite3
import re

#create a database or open connection if exists
conn=sqlite3.connect("bookstore.db") #establishes the connection with database
print("Opened database succesfully")


#display the data from BOOKSTORE database


print("Enter 1 for admin\nEnter 2 for Customer")
num=int(input("Enter your choice"))
if num==1:
    print("ADMIN LOGIN")
    cursor=conn.execute("SELECT * FROM ADMIN")
    
    a_username=str(input("Enter admin username:"))
    for row in cursor:
        searchObj=re.search(row[0],a_username,re.M|re.I)
    
    if searchObj:
        a_password=str(input("Enter admin password:"))
        
        searchObj1=re.search(row[1],a_password,re.M|re.I)
    
        if searchObj1:
            print("Admin logged in")
            print("1:INSERT\n2:DELETE\n3:UPDATE\n4:DISPLAY")

            n=int(input("\nEnter your choice:"))
            if n==1:
                a0=str(input("Enter the book name"))
                a1=str(input("Enter the book author:"))
                a2=int(input("Enter the book price:"))
                a3=int(input("Enter the number of books:"))
                a4=str(input("Enter the admin username:"))
                conn.execute("INSERT INTO BOOK(B_NAME,B_AUTHOR,B_PRICE,NO_OF_BOOKS,A_USERNAME) VALUES(?,?,?,?,?)",(a0,a1,a2,a3,a4))
                conn.commit();
                print("Record inserted successfully")
            elif n==2:
                a0=str(input("Enter the book name to be deleted:"))
                conn.execute("DELETE FROM BOOK WHERE B_NAME=?",(a0,))
                conn.commit()
                print("deletion operation done successfully")
            elif n==3:
                a0=str(input("Enter the book name"))
                print("Enter the updated details")
                
                a1=str(input("book author:"))
                a2=int(input("book price:"))
                a3=int(input("number of books:"))
                a4=str(input("admin username:"))
                conn.execute("UPDATE BOOK SET B_AUTHOR=?,B_PRICE=?,NO_OF_BOOKS=?,A_USERNAME=? WHERE B_NAME=?",(a1,a2,a3,a4,a0,))
                conn.commit()
                print("operation done successfully")
            elif n==4:
                #DISPLAY BOOK TABLE
                cursor=conn.execute("SELECT * FROM BOOK")

                #ITERATE OVER THE DATA
                for row in  cursor:
                    print("\nBOOK NAME:",row[0])
                    print("BOOK AUTHOR:",row[1])
                    print("BOOK PRICE:",row[2])
                    print("NO OF BOOK COPIES:",row[3])
                    print("ADMIN ADDIING THE BOOK:",row[4])
        else:
            print("Wrong admin password")
    else:
        print("Wrong username entered")
    
  

elif num==2:
    print("Enter 1 for Login\nEnter 2 for Register")
    n=int(input("Enter your choice"))
    if n==1:
        list1=[]
        list2=[]
        sum1=0
        user = str(input("User Email:"))
        pswd = str(input("Password"))

        db = sqlite3.connect('bookstore.db')
        c = db.cursor()
        c.execute('SELECT * from CUSTOMER WHERE C_EMAILID="%s" AND C_PASSWORD="%s"' % (user, pswd))
        if c.fetchone() is not None:
            print("lOGIN SUCCESSFUL")
            n_bk=int(input("Enter the number of books to be searched:"))
            for i in range(0,n_bk):
                name = str(input("Enter the %d book:"%(i+1)))
                c.execute('SELECT * from BOOK WHERE B_NAME="%s"'% (name))
                if c.fetchone() is not None:
                    print("Book found")
                    
                    accept=str(input("Do you want to buy the book?"))
                    if accept=="yes":
                        print("Book added to cart")
                        
                        sql='SELECT B_PRICE from BOOK WHERE B_NAME=?'
                        cur=conn.cursor()
                        cur.execute(sql,(name,))
                        p=cur.fetchone()
                        list1.append(name)
                        list2.append(p[0])
                        sum1=sum1+int(p[0])
                        
 
                else:
                    print("Not found")
            #print(list1)
            gst=(5/100)*sum1
            sum2=sum1+gst
            for i in range(0,n_bk):
                print("%d %s"%((i+1),list1[i]))
                print("Cost:%d"%list2[i])
            print("GST=%f"%gst)
            print("The total amount is:",sum2)

        else:
            print("Login failed")
          
            
    if n==2:
        print("Customer Details:")
        a0=str(input("Email ID:"))
        a1=str(input("Password:"))
        a2=str(input("Address:"))
        a3=int(input("Phone Number:"))
        conn.execute("INSERT INTO CUSTOMER(C_EMAILID,C_PASSWORD,C_ADDRESS,C_PHONE) VALUES(?,?,?,?)",(a0,a1,a2,a3))
        conn.commit();
        print("Customer Registered successfully")


    
    
        
