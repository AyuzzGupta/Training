import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # Database connection details
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = os.getenv("DB_PORT", "5432")
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD", "password")
        self.dbname = os.getenv("DB_NAME", "complaint_tracker")
        self.connection = None
        self.cursor = None

    def create_database(self):
        """Creates the database if it doesn't exist."""
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname="postgres"
            )
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()
            cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{self.dbname}'")
            exists = cur.fetchone()
            if not exists:
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
                print(f"Database {self.dbname} created successfully.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error creating database: {e}")

    def connect(self):
        """Connects to the complaint_tracker database."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        """Closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None, fetch=False, fetch_all=True):
        """Executes a SQL query securely using parameters."""
        try:
            self.cursor.execute(query, params)
            if fetch:
                if fetch_all:
                    return self.cursor.fetchall()
                return self.cursor.fetchone()
            self.connection.commit()
            return True
        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print(f"Database error: {e}")
            return None

    def setup_tables(self):
        """Creates tables and inserts sample data."""
        self.connect()
        if not self.connection:
            return

        # Drop existing tables to start fresh
        self.execute_query("DROP TABLE IF EXISTS Complaints CASCADE")
        self.execute_query("DROP TABLE IF EXISTS Users CASCADE")
        self.execute_query("DROP TABLE IF EXISTS Admins CASCADE")

        users_table = """
        CREATE TABLE Users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """

        admins_table = """
        CREATE TABLE Admins (
            admin_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """

        complaints_table = """
        CREATE TABLE Complaints (
            complaint_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES Users(user_id),
            title VARCHAR(200) NOT NULL,
            description TEXT NOT NULL,
            category VARCHAR(50) NOT NULL,
            status VARCHAR(20) NOT NULL DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.execute_query(users_table)
        self.execute_query(admins_table)
        self.execute_query(complaints_table)
        
        # Insert sample admin account
        self.execute_query("INSERT INTO Admins (username, password) VALUES (%s, %s)", ("admin", "admin123"))
        
        # Insert sample user and complaints
        self.execute_query("INSERT INTO Users (name, email, phone, password) VALUES (%s, %s, %s, %s)", 
                           ("John Doe", "john@example.com", "1234567890", "password123"))
        self.execute_query("INSERT INTO Complaints (user_id, title, description, category, status) VALUES (%s, %s, %s, %s, %s)",
                           (1, "No Electricity in Room 101", "The power has been out since morning.", "Electricity", "Pending"))
        self.execute_query("INSERT INTO Complaints (user_id, title, description, category, status) VALUES (%s, %s, %s, %s, %s)",
                           (1, "Water leaking in bathroom", "Tap is broken.", "Water", "In Progress"))

        self.close()
