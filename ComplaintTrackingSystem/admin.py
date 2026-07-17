class Admin:
    def __init__(self, db):
        self.db = db

    def login(self):
        print("\n--- Admin Login ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        query = "SELECT admin_id, username FROM Admins WHERE username = %s AND password = %s"
        result = self.db.execute_query(query, (username, password), fetch=True, fetch_all=False)

        if result:
            admin_id = result[0]
            username = result[1]
            print(f"\nWelcome, Admin {username}!")
            return admin_id
        else:
            print("Invalid username or password.")
            return None

    def view_all_complaints(self):
        print("\n--- All Complaints ---")
        query = """
            SELECT c.complaint_id, u.name, c.title, c.category, c.status, c.created_at
            FROM Complaints c
            INNER JOIN Users u ON c.user_id = u.user_id
            ORDER BY c.created_at DESC
        """
        results = self.db.execute_query(query, fetch=True)
        
        if results:
            print(f"{'ID':<5} | {'User':<15} | {'Title':<20} | {'Category':<15} | {'Status':<12} | {'Date'}")
            print("-" * 90)
            for row in results:
                title = row[2] if len(row[2]) <= 20 else row[2][:17] + "..."
                user_name = row[1] if len(row[1]) <= 15 else row[1][:12] + "..."
                print(f"{row[0]:<5} | {user_name:<15} | {title:<20} | {row[3]:<15} | {row[4]:<12} | {str(row[5])[:10]}")
        else:
            print("No complaints found in the system.")

    def update_complaint_status(self):
        print("\n--- Update Complaint Status ---")
        complaint_id = input("Enter Complaint ID to update: ").strip()
        
        query = "SELECT status FROM Complaints WHERE complaint_id = %s"
        result = self.db.execute_query(query, (complaint_id,), fetch=True, fetch_all=False)
        
        if result:
            print(f"Current Status: {result[0]}")
            statuses = ['Pending', 'In Progress', 'Resolved']
            print("\nAvailable Statuses:")
            for i, status in enumerate(statuses, 1):
                print(f"{i}. {status}")
                
            try:
                status_choice = int(input("Select New Status (1-3): "))
                if 1 <= status_choice <= 3:
                    new_status = statuses[status_choice - 1]
                    update_query = "UPDATE Complaints SET status = %s WHERE complaint_id = %s"
                    if self.db.execute_query(update_query, (new_status, complaint_id)):
                        print("Status updated successfully!")
                    else:
                        print("Failed to update status.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Complaint not found.")

    def delete_complaint(self):
        print("\n--- Delete Complaint ---")
        complaint_id = input("Enter Complaint ID to delete: ").strip()
        
        query = "SELECT * FROM Complaints WHERE complaint_id = %s"
        result = self.db.execute_query(query, (complaint_id,), fetch=True, fetch_all=False)
        
        if result:
            delete_query = "DELETE FROM Complaints WHERE complaint_id = %s"
            if self.db.execute_query(delete_query, (complaint_id,)):
                print("Complaint deleted successfully!")
            else:
                print("Failed to delete complaint.")
        else:
            print("Complaint not found.")
