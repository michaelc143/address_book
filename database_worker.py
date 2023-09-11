import sqlite3

# Step 3: Create Database Connection
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Step 4: Define Database Schema
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Step 5: Perform CRUD Operations
def insert_contact(conn, name, email):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def get_contacts(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts')
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
    return []

def update_contact(conn, contact_id, name, email):
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE contacts SET name = ?, email = ? WHERE id = ?', (name, email, contact_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_contact(conn, contact_id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Step 6: Main Program
if __name__ == "__main__":
    database_file = 'py_data.db'
    conn = create_connection(database_file)

    if conn is not None:
        create_table(conn)

        while True:
            print("Address Book Menu:")
            print("1. Add Contact")
            print("2. List Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Quit")
            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                insert_contact(conn, name, email)
                print("Contact added successfully.")
            elif choice == '2':
                contacts = get_contacts(conn)
                for contact in contacts:
                    print(f"ID: {contact[0]}, Name: {contact[1]}, Email: {contact[2]}")
            elif choice == '3':
                contact_id = input("Enter contact ID to update: ")
                name = input("Enter updated name: ")
                email = input("Enter updated email: ")
                update_contact(conn, contact_id, name, email)
                print("Contact updated successfully.")
            elif choice == '4':
                contact_id = input("Enter contact ID to delete: ")
                delete_contact(conn, contact_id)
                print("Contact deleted successfully.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()
    else:
        print("Error: Unable to connect to the database.")
