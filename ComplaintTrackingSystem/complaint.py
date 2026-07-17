class Complaint:
    def __init__(self, db):
        self.db = db

    def add_complaint(self, user_id):
        print("\n--- Raise Complaint ---")
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        
        categories = ['Electricity', 'Water', 'Internet', 'Hostel', 'Mess', 'Cleaning', 'Security', 'Other']
        print("\nCategories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
            
        try:
            cat_choice = int(input("Select Category (1-8): "))
            if 1 <= cat_choice <= 8:
                category = categories[cat_choice - 1]
            else:
                print("Invalid category. Complaint not registered.")
                return
        except ValueError:
            print("Invalid input. Complaint not registered.")
            return

        query = "INSERT INTO Complaints (user_id, title, description, category) VALUES (%s, %s, %s, %s)"
        if self.db.execute_query(query, (user_id, title, description, category)):
            print("Complaint registered successfully!")
        else:
            print("Failed to register complaint.")

    def view_my_complaints(self, user_id):
        print("\n--- My Complaints ---")
        query = "SELECT complaint_id, title, category, status, created_at FROM Complaints WHERE user_id = %s ORDER BY created_at DESC"
        results = self.db.execute_query(query, (user_id,), fetch=True)
        
        if results:
            print(f"{'ID':<5} | {'Title':<20} | {'Category':<15} | {'Status':<12} | {'Date'}")
            print("-" * 75)
            for row in results:
                # Format string to handle long titles gracefully
                title = row[1]
                if len(title) > 20:
                    title = title[:17] + "..."
                print(f"{row[0]:<5} | {title:<20} | {row[2]:<15} | {row[3]:<12} | {str(row[4])[:10]}")
        else:
            print("No complaints found.")

    def update_complaint(self, user_id):
        print("\n--- Update Complaint ---")
        self.view_my_complaints(user_id)
        
        complaint_id = input("\nEnter Complaint ID to update: ").strip()
        
        # Check if complaint belongs to user
        query = "SELECT title, description FROM Complaints WHERE complaint_id = %s AND user_id = %s"
        result = self.db.execute_query(query, (complaint_id, user_id), fetch=True, fetch_all=False)
        
        if result:
            new_title = input(f"New Title (leave blank to keep '{result[0]}'): ").strip()
            new_desc = input(f"New Description (leave blank to keep current): ").strip()
            
            title_to_update = new_title if new_title else result[0]
            desc_to_update = new_desc if new_desc else result[1]
            
            update_query = "UPDATE Complaints SET title = %s, description = %s WHERE complaint_id = %s AND user_id = %s"
            if self.db.execute_query(update_query, (title_to_update, desc_to_update, complaint_id, user_id)):
                print("Complaint updated successfully!")
            else:
                print("Failed to update complaint.")
        else:
            print("Complaint not found or you don't have permission to update it.")

    def delete_complaint(self, user_id):
        print("\n--- Delete Complaint ---")
        complaint_id = input("Enter Complaint ID to delete: ").strip()
        
        # Check if complaint belongs to user
        query = "SELECT * FROM Complaints WHERE complaint_id = %s AND user_id = %s"
        result = self.db.execute_query(query, (complaint_id, user_id), fetch=True, fetch_all=False)
        
        if result:
            delete_query = "DELETE FROM Complaints WHERE complaint_id = %s AND user_id = %s"
            if self.db.execute_query(delete_query, (complaint_id, user_id)):
                print("Complaint deleted successfully!")
            else:
                print("Failed to delete complaint.")
        else:
            print("Complaint not found or you don't have permission to delete it.")
