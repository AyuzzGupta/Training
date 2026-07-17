import psycopg2

class User:
    def __init__(self, db):
        self.db = db

    def register(self):
        print("\n--- User Registration ---")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        password = input("Password: ").strip()

        if not name or not email or not password:
            print("Name, Email, and Password are required!")
            return

        try:
            query = "INSERT INTO Users (name, email, phone, password) VALUES (%s, %s, %s, %s)"
            self.db.execute_query(query, (name, email, phone, password))
            print("Registration successful! You can now login.")
        except psycopg2.IntegrityError:
            print("Error: Email already exists.")
        except Exception as e:
            print(f"Error during registration: {e}")

    def login(self):
        print("\n--- User Login ---")
        email = input("Email: ").strip()
        password = input("Password: ").strip()

        query = "SELECT user_id, name FROM Users WHERE email = %s AND password = %s"
        result = self.db.execute_query(query, (email, password), fetch=True, fetch_all=False)

        if result:
            user_id = result[0]
            name = result[1]
            print(f"\nWelcome, {name}!")
            return user_id
        else:
            print("Invalid email or password.")
            return None
