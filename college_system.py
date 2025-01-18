import mysql.connector as mysql

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

finally:
    # Close the connection
    if db.is_connected():
        db.close()
        print("Connection closed.")


def main():
    while 1:
        print('WELCOME TO THE COLLELGE SYSTEM')
        print("")
        print("1,Log as student")
        print("2.Log as teacher")
        print("3.Log as admin")

        user_option = input(str("Option:"))
        if user_option == "1":
            print("Student login")
        elif user_option == "2":
            print("Teacehr login")
        elif user_option == "3":
            print("Admin login")
        else:
            print("Invalid opton was selected")

main()