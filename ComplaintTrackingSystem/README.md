# Complaint Tracking System

A simple CLI-based Complaint Tracking System built with Python and PostgreSQL. This project is designed for beginners learning Object-Oriented Programming (OOP) and SQL.

## Features
- **User Module**: Register, Login, Raise Complaints, View, Update, and Delete your own complaints.
- **Admin Module**: Login, View All Complaints, Update Status, and Delete any complaint.
- **Database**: PostgreSQL backend using `psycopg2`.

## Prerequisites
- Python 3
- PostgreSQL
- `pip`

## Installation

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the root directory and configure your PostgreSQL database credentials:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=your_postgres_user
   DB_PASSWORD=your_postgres_password
   DB_NAME=complaint_tracker
   ```

3. Make sure PostgreSQL is running on your machine.

4. Run the application:
   ```bash
   python main.py
   ```
   *Note: Running `main.py` for the first time will automatically create the database `complaint_tracker`, set up the tables, and insert sample data.*

## Step-by-Step Guide: How to Use the System

Here is a step-by-step example of how to interact with the Complaint Tracking System.

### Step 1: Start the Application
Run `python main.py` in your terminal. You will be presented with the Main Menu:
```
==============================
 Complaint Tracking System 
==============================
1. Register
2. User Login
3. Admin Login
4. Exit
------------------------------
```

### Step 2: Register a New User
1. Select option **`1`** (Register).
2. Enter your details:
   - Name: `Alice`
   - Email: `alice@example.com`
   - Phone: `9876543210`
   - Password: `mypassword`
3. You will see a success message.

### Step 3: Login as a User
1. From the Main Menu, select option **`2`** (User Login).
2. Enter the email and password you just created (`alice@example.com` / `mypassword`).
3. You are now in the **User Menu**.

### Step 4: Raise a Complaint
1. From the User Menu, select option **`1`** (Raise Complaint).
2. Enter a **Title** (e.g., "Internet not working").
3. Enter a **Description** (e.g., "The Wi-Fi router is completely dead.").
4. Select the category by entering its number (e.g., **`3`** for Internet).
5. The system will confirm your complaint has been registered.

### Step 5: View and Update Your Complaint
1. Select option **`2`** (View My Complaints) to see a list of your complaints and note the Complaint ID.
2. Select option **`3`** (Update Complaint).
3. Enter the Complaint ID.
4. Provide a new title or description (or press Enter to keep them the same).
5. Finally, select option **`5`** to Logout and return to the Main Menu.

### Step 6: Login as Admin and Update Status
1. From the Main Menu, select option **`3`** (Admin Login).
2. Enter the sample admin credentials:
   - Username: `admin`
   - Password: `admin123`
3. You are now in the **Admin Menu**.
4. Select option **`1`** (View All Complaints) to see all complaints raised by all users, including Alice's new complaint.
5. Select option **`2`** (Update Complaint Status).
6. Enter the Complaint ID of Alice's complaint.
7. Select a new status (e.g., **`2`** for In Progress).
8. The status is now updated! You can view all complaints again to verify the change.

### Step 7: Delete a Complaint and Exit
1. If you wish to delete a complaint, select option **`3`** from the Admin Menu.
2. Enter the Complaint ID to delete it permanently.
3. Select option **`4`** to Logout.
4. From the Main Menu, select option **`4`** to Exit the system.

## Sample Accounts

- **Admin Account:**
  - Username: `admin`
  - Password: `admin123`

- **Sample User Account:**
  - Email: `john@example.com`
  - Password: `password123`

## Project Structure
- `main.py`: The main loop and menu system.
- `database.py`: Handles PostgreSQL connection and table setup.
- `user.py`: Handles user registration and login.
- `complaint.py`: Handles raising, viewing, updating, and deleting complaints.
- `admin.py`: Handles admin login and complaint management.
