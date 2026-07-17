import sys
from database import Database
from user import User
from complaint import Complaint
from admin import Admin

def main():
    print("Initializing Database...")
    db = Database()
    db.create_database()
    db.setup_tables()
    
    user_module = User(db)
    complaint_module = Complaint(db)
    admin_module = Admin(db)
    
    db.connect()

    while True:
        print("\n" + "="*30)
        print(" Complaint Tracking System ")
        print("="*30)
        print("1. Register")
        print("2. User Login")
        print("3. Admin Login")
        print("4. Exit")
        print("-" * 30)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            user_module.register()
            
        elif choice == '2':
            user_id = user_module.login()
            if user_id:
                user_menu(user_id, complaint_module)
                
        elif choice == '3':
            admin_id = admin_module.login()
            if admin_id:
                admin_menu(admin_module)
                
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def user_menu(user_id, complaint_module):
    while True:
        print("\n" + "="*30)
        print(" User Menu ")
        print("="*30)
        print("1. Raise Complaint")
        print("2. View My Complaints")
        print("3. Update Complaint")
        print("4. Delete Complaint")
        print("5. Logout")
        print("-" * 30)
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            complaint_module.add_complaint(user_id)
        elif choice == '2':
            complaint_module.view_my_complaints(user_id)
        elif choice == '3':
            complaint_module.update_complaint(user_id)
        elif choice == '4':
            complaint_module.delete_complaint(user_id)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

def admin_menu(admin_module):
    while True:
        print("\n" + "="*30)
        print(" Admin Menu ")
        print("="*30)
        print("1. View All Complaints")
        print("2. Update Complaint Status")
        print("3. Delete Complaint")
        print("4. Logout")
        print("-" * 30)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            admin_module.view_all_complaints()
        elif choice == '2':
            admin_module.update_complaint_status()
        elif choice == '3':
            admin_module.delete_complaint()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting system...")
        sys.exit(0)
