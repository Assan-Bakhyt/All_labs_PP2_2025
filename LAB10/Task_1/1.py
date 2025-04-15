import psycopg2
import csv

connection = psycopg2.connect( # Connecting to the PhoneBook db
    database = "PhoneBook",
    user = "postgres",
    password = "123789789",
    host = "localhost"
)

def create_table():

    command = """
            CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255),
            user_phone VARCHAR(20)
            )
        """
    with connection.cursor() as cur:
        # execute the command
        cur.execute(command)
    connection.commit() # save change to the db

def insert_user():

    user_name = input("Enter user name: ")
    user_phone = input("Enter user phone: ")

    command = """
        INSERT INTO users(user_name,user_phone) VALUES (%s,%s)
    """

    with connection.cursor() as cur:
        # execute the command
        cur.execute(command, (user_name,user_phone))

    connection.commit()
    print("\nuser added successfully!")

def insert_from_csv(file_path):
    try:
        with connection.cursor() as cur:
            with open(file_path,'r') as f:
                csvreader = csv.reader(f)
                next(csvreader) # skip the title
                for row in csvreader:
                    cur.execute("INSERT INTO users (user_name,user_phone) VALUES (%s,%s)",(row[0],row[1]))

            connection.commit()
            print("\nData from CSV added successfully!")
    except:
        print("\nX Invalid file entered X")

        
def update_user_phone():
    name = input("Enter user_name to update: ")
    new_phone = input("Enter new phone number: ")

    command = "UPDATE users SET user_phone = %s WHERE user_name = %s"

    with connection.cursor() as cur:
        cur.execute(command, (new_phone,name))

    connection.commit()
    print("\nContact updated!")

def update_user_name():
    name = input("Enter user_name to update: ")
    new_name = input("Enter new user_name: ")

    command = "UPDATE users SET user_name = %s WHERE user_name = %s"

    with connection.cursor() as cur:
        cur.execute(command,(new_name,name))

    connection.commit()
    print("\nContact updated!")

def filter_by_first_letter():
    letter = input("Enter letter: ")
    command = " SELECT * FROM users WHERE user_name ILIKE %s"
  
    with connection.cursor() as cur: 
        cur.execute(command, (letter + '%',))
        results = cur.fetchall()
        for row in results:
            print(row)
    print("\nfiltering by first letter completed!")

def filter_by_part():
    keyword = input("Enter letters: ")
    command = "SELECT * FROM users WHERE user_name ILIKE %s"

    with connection.cursor() as cur:
        cur.execute(command,("%" + keyword + "%",))
        results = cur.fetchall()
        for row in results:
            print(row)

    print("\nfiltering by part completed!")

def delete_user():

    name = input("Enter a name to delete: ")

    command = "DELETE FROM users WHERE user_name = %s"

    with connection.cursor() as cur:
        cur.execute(command, (name,))

    connection.commit()
    print("\nContact deleted X")

def truncate_table():
    command = "TRUNCATE TABLE users RESTART IDENTITY"

    with connection.cursor() as cur:
        cur.execute(command)

    connection.commit()

    print("\nThe table has been cleared!")

def show_all_users():
    command = "SELECT * FROM users"

    with connection.cursor() as cur:
        cur.execute(command)
        result = cur.fetchall()
        print("user_id  user_name  user_phone")
        for row in result:
            print(row[0], row[1], row[2])

    connection.commit()

if __name__ == "__main__":
    create_table() # create a table if it doesn't exist yet

    while True:
        print("\n PHONEBOOK MENU: ")
        print("1. Add new user")
        print("2. Load users from CSV")
        print("3. Update user's phone")
        print("4. Update user's name")
        print("5. Filter by first letter")
        print("6. Filter by part")
        print("7. Delete user")
        print("8. Clear table")
        print("9. Show all users")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            insert_user() 
        elif choice == '2':
            path_csv = input("Enter csv path: ")
            insert_from_csv(path_csv)
        elif choice == '3':
            update_user_phone()
        elif choice == '4':
            update_user_name()
        elif choice == '5':
            filter_by_first_letter()
        elif choice == '6':
            filter_by_part()
        elif choice == '7':
            delete_user()
        elif choice == '8':
            truncate_table()
        elif choice == '9':
            show_all_users()
        elif choice == '0':
            print("You have exited the PhoneBook!")
            break
        else:
            print("Invalid option X")