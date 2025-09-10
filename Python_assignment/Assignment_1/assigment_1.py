
# Mini Project: Console-based CRUD Operations (Student Management)

# This list will act as our in-memory database to store student records.
students = []

# --- Create Operation ---
def add_student():
    """Prompts for student details and adds a new student record."""
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ")
    # Check for duplicate roll numbers
    for s in students:
        if s['roll'] == roll:
            print("\n⚠️ Error: A student with this roll number already exists.\n")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    # Create a dictionary for the new student
    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    print("\n✅ Student added successfully!\n")

# --- Read Operations ---
def display_students():
    """Displays all student records in a formatted table."""
    if not students:
        print("\n⚠️ No student records found. The database is empty.\n")
        return

    print("\n📋 Student Records:")
    print("-" * 60)
    print(f"{'Roll No.':<10} | {'Name':<20} | {'Age':<5} | {'Course':<15}")
    print("-" * 60)
    for s in students:
        print(f"{s['roll']:<10} | {s['name']:<20} | {s['age']:<5} | {s['course']:<15}")
    print("-" * 60)

def search_student():
    """Searches for a specific student by their roll number."""
    if not students:
        print("\n⚠️ No student records to search from.\n")
        return

    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s['roll'] == roll:
            print("\n🔎 Student Found:")
            print(f"  Roll: {s['roll']}")
            print(f"  Name: {s['name']}")
            print(f"  Age: {s['age']}")
            print(f"  Course: {s['course']}\n")
            return
    print("\n❌ Student with the given roll number not found.\n")

# --- Update Operation ---
def update_student():
    """Updates the details of an existing student."""
    if not students:
        print("\n⚠️ No student records to update.\n")
        return

    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s['roll'] == roll:
            print("\nEnter new details (leave blank to keep current value):")
            
            new_name = input(f"New Name (current: {s['name']}): ")
            new_age = input(f"New Age (current: {s['age']}): ")
            new_course = input(f"New Course (current: {s['course']}): ")

            if new_name:
                s['name'] = new_name
            if new_age:
                s['age'] = new_age
            if new_course:
                s['course'] = new_course

            print("\n✅ Student details updated successfully!\n")
            return
    print("\n❌ Student with the given roll number not found.\n")

# --- Delete Operation ---
def delete_student():
    """Deletes a student record by their roll number."""
    if not students:
        print("\n⚠️ No student records to delete.\n")
        return
        
    roll = input("Enter Roll Number to Delete: ")
    for i, s in enumerate(students):
        if s['roll'] == roll:
            students.pop(i) # Use pop(i) for safe removal
            print("\n🗑️ Student deleted successfully!\n")
            return
    print("\n❌ Student with the given roll number not found.\n")

# --- Main Menu Function ---
def menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search for a Student")
        print("4. Update a Student's Details")
        print("5. Delete a Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("\n👋 Exiting the program. Thank you!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 6.\n")

# --- Run the project ---
if __name__ == "__main__":
    menu()