import mysql.connector as mysql
import getpass
import time
import sys
try:
    # Connect to the database
    db = mysql.connect(
        host='localhost',
        user='root',
        password='padamdamai',
        database='CollegeAuthentication'
    )

    # Check if the connection was successful
    if db.is_connected():
        print("Connection successful!")
        # Create a cursor object
        command_handler = db.cursor(buffered=True)
    else:
        print("Connection failed!")

except mysql.Error as err:
    print(f"Error: {err}")


def admin_session():
    print("---------------------------------------------------")
    print("Login Successful")
    print("admin menu")
    print("1. Register new student")
    print("2. Register new Teacher")    
    print("3. Delete existing Student")    
    print("4. Delete existing Teacher")    
    print("5. Logout ")

    user_option = input(str("Option: "))
    if user_option == "1":
        print(" ")
        print("Register new student")
        username = input(str("Enter student name : "))
        password = getpass.getpass("Enter the Password : ")
        conform_password = getpass.getpass("conform your password : ")
        if password  == conform_password :
            sql_query = (username,password)
            command_handler.execute("INSERT INTO users (username,password,previllege) VALUES (%s,%s,'student')",sql_query)
            db.commit()
            time.sleep(3)
            print(f"{username} has been successfully registered as student successfully ")

        else:
            print("The password didn't matched,please try again ")
            admin_session()
                

    elif user_option == "2":
        print(" ")
        print("Register new Teacher")
        username = input(str("Enter Teacher name : "))
        password = getpass.getpass("Enter the Password : ")
        conform_password = getpass.getpass("conform your password : ")
        if password  == conform_password :
            sql_query = (username,password)
            command_handler.execute("INSERT INTO users (username,password,previllege) VALUES (%s,%s,'Teacher')",sql_query)
            db.commit()
            time.sleep(3)
            print(f"{username} has been successfully registered as Teacher successfully ")

        else:
            print("The password didn't matched,please try again ")
            admin_session()


    elif user_option == "3":
        print(" ")
        print("Delete student")
        username = input(str("Enter the username : "))
        query_sql = (username,'student')
        command_handler.execute("DELETE FROM users WHERE username = (%s) and previllege = (%s)",query_sql)
        db.commit()
        if command_handler.rowcount < 1:
            print(f"Student {username} not found ")
            admin_session()
        else:
            time.sleep(3)
            print(f"Student {username} was deleted successfully ")
    elif user_option == '4':
        print(" ")
        print("Delete Teacher")
        username= input(str("Enter the username : "))
        query_sql = (username,'Teacher')
        command_handler.execute("DELETE FROM users WHERE username = (%s) and previllege = (%s)",query_sql)
        db.commit()
        if command_handler.rowcount < 1:
            print(f"Teacher {username} not found")
            admin_session()
        else:
            time.sleep(3)
            print(f"Teacher {username} was deleted successfully ")
    elif user_option == "5":
        print("logging out...")
        time.sleep(4)
        return 
    else:
        print("The option is not available i.e invalid option")

def auth_admin():
    print(" ")
    print("ADMIN LOGIN PAGE")
    print("")
    username = input(str("Username : "))
    password = getpass.getpass("Password : ")
    if username ==  "username" and password == "password":
        time.sleep(3)
        admin_session()
    else:
        print("Incorrec password or username")

def main():
    while 1:
        print("\n")
        print("------------------------------------------------------------")
        print('WELCOME TO THE COLLELGE MANAGEMENT SYSTEM')
        print("")
        print("1,Log as student")
        print("2.Log as teacher")
        print("3.Log as admin")
        print("4.Exit")

        user_option = input(str("Option:"))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacehr login")
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid opton was selected")

main()