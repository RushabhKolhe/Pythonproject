import mysql.connector

def liabrary():
    print("Welcome to admin pannel")
    user = input("Which type of operation you want to do 'I' insert 'U' update 'D' delete 'V' view records: ")
    if user in ['I', 'i']:
        db = mysql.connector.connect(host='localhost', user='root', password='1234', database='rushabh')
        sql = "insert into liabrary values(null,%s,%s,%s,%s,%s,%s)"
        mcursor = db.cursor()
        bookid=input("Enter your book ID : ")
        bookname=input("Enter your book name : ")
        subject=input("Enter your book subject : ")
        quatity=input("Enter your book quantity : ")
        studentid=input("Enter your student ID : ")
        adminuser=input("Enter your admin ID : ")
        # d=CURRENT_TIMESTAMP()
        update_value = (bookid,bookname,subject,quatity,studentid,adminuser)
        mcursor.execute(sql, update_value)
        db.commit()
        print("Your '{}' book successfully add to liabrary".format(bookname))
        print("Your data successfully stored in database....")
    elif user in ['U', 'u']:
        db = mysql.connector.connect(host='localhost', user='root', password='1234', database='rushabh')
        sql = "update liabrary set Book_name=%s,Subject=%s,Quantity=%s where Book_id=%s"
        mcursor = db.cursor()
        #bookid=input("Enter your book ID : ")
        bookname=input("Enter your book name : ")
        subject=input("Enter your book subject : ")
        quatity=input("Enter your book quantity : ")
        bookid1 = input("Which book ID record you want to update : ")
        # d=CURRENT_TIMESTAMP()
        update_value = (bookname,subject,quatity,bookid1)
        mcursor.execute(sql, update_value)
        db.commit()
        print("Your '{}' book successfully add to liabrary".format(bookname))
        print("Your data successfully stored in database....")
    elif user in ['D', 'd']:
        db = mysql.connector.connect(host='localhost', user='root', password='1234', database='rushabh')
        sql = ("delete from liabrary where Book_id=%s and Book_name=%s")
        mcursor = db.cursor()
        bookid = input("Enter your bookid : ")
        bookname=input("Enter Your bookname : ")
        delete_value = (bookid,bookname)
        mcursor.execute(sql, delete_value)
        db.commit()
        print("Your data successfully deleted in database....")
    elif user in ['V', 'v']:
        db = mysql.connector.connect(host='localhost', user='root', password='1234', database='rushabh')
        sql = "select * from liabrary where Book_id=%s and Book_name=%s"
        mcursor = db.cursor()
        bookid=input("Enter your book ID : ")
        bookname = input("Enter Your bookname : ")
        # d=CURRENT_TIMESTAMP()
        update_value = (bookid,bookname)
        mcursor.execute(sql, update_value)
        result=mcursor.fetchall()
        print(result)

def students():
    print("Welcome Student")
    user=input("You want to see books in the liabrary 'Y' and 'N' : ")
    if user in['Y','y']:
        db = mysql.connector.connect(host='localhost', user='root', password='1234', database='rushabh')
        #sql = "select * from liabrary where Book_id=%s and Book_name=%s"
        mcursor = db.cursor()
        #bookid=input("Enter your book ID : ")
        #bookname = input("Enter Your bookname : ")
        # d=CURRENT_TIMESTAMP()
        #update_value = (bookid,bookname)
        mcursor.execute('select * from liabrary')
        result=mcursor.fetchall()
        print(result)
def apassw():
    admin=input("Enter your username : ")
    if admin in['Rushabh']:
        apassw=input("Enter password : ")
        if apassw in ['Rushabh']:
            liabrary()
        else:
            print("Wrong Password....")
def spassw():
    student=input("Enter your username : ")
    if student in['student']:
        spassw=input("Enter password : ")
        if spassw in ['student']:
            students()
        else:
            print("Wrong Password....")
def verify():
    user=input("If you are admin then press 'A' and for student login press 'S' : ")
    if user in['A','a']:
        apassw()
    elif user in['S','s']:
        spassw()
    else:
        ("Wrong input entered...")

verify()
