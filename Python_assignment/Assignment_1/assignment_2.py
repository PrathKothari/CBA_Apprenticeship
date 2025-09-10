import csv
import os

# --- Constants ---
CSV_FILE = 'students.csv'
# Define the header for the CSV file. This also helps in accessing dictionary keys.
CSV_HEADER = ['StudentID', 'Name', 'Age', 'Course', 'Grade']

# --- Helper Functions ---
def initialize_csv():
    """Creates the CSV file with a header if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADER)

def read_records():
    """Reads all records from the CSV file."""
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_records(records):
    """Writes a list of records back to the CSV file, overwriting it."""
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(records)

# --- CRUD Operations ---

# 1. Create (Add a new record)
def add_record():
    """Adds a new student record to the CSV file."""
    print("\n--- Add New Student Record ---")
    student_id = input("Enter Student ID: ")

    # Validation: Check if the StudentID already exists
    records = read_records()
    for record in records:
        if record['StudentID'] == student_id:
            print(f"\n⚠️ Error: Student with ID '{student_id}' already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    grade = input("Enter Grade: ")

    new_record = {
        'StudentID': student_id,
        'Name': name,
        'Age': age,
        'Course': course,
        'Grade': grade
    }

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADER)
        writer.writerow(new_record)

    print("\n✅ Student record added successfully!")

# 2. Read (View all and Search for a record)
def view_records():
    """Displays all student records from the CSV file."""
    records = read_records()
    if not records:
        print("\n⚠️ No records found.")
        return

    print("\n--- All Student Records ---")
    # Pretty print the records in a table format
    print(f"{'StudentID':<12} | {'Name':<20} | {'Age':<5} | {'Course':<15} | {'Grade':<8}")
    print("-" * 70)
    for record in records:
        print(f"{record['StudentID']:<12} | {record['Name']:<20} | {record['Age']:<5} | {record['Course']:<15} | {record['Grade']:<8}")
    print("-" * 70)


def search_record():
    """Searches for a student by their StudentID."""
    student_id = input("Enter Student ID to search for: ")
    records = read_records()
    found_record = None
    for record in records:
        if record['StudentID'] == student_id:
            found_record = record
            break

    if found_record:
        print("\n--- Record Found ---")
        print(f"Student ID: {found_record['StudentID']}")
        print(f"Name:       {found_record['Name']}")
        print(f"Age:        {found_record['Age']}")
        print(f"Course:     {found_record['Course']}")
        print(f"Grade:      {found_record['Grade']}")
    else:
        print(f"\n❌ No record found with Student ID '{student_id}'.")

# 3. Update (Modify an existing record)
def update_record():
    """Updates an existing student record."""
    student_id = input("Enter Student ID of the record to update: ")
    records = read_records()
    record_found = False
    updated_records = []

    for record in records:
        if record['StudentID'] == student_id:
            record_found = True
            print("\n--- Updating Record ---")
            print("Enter new details (leave blank to keep current value):")
            
            new_name = input(f"New Name (current: {record['Name']}): ")
            new_age = input(f"New Age (current: {record['Age']}): ")
            new_course = input(f"New Course (current: {record['Course']}): ")
            new_grade = input(f"New Grade (current: {record['Grade']}): ")

            if new_name: record['Name'] = new_name
            if new_age: record['Age'] = new_age
            if new_course: record['Course'] = new_course
            if new_grade: record['Grade'] = new_grade
            
        updated_records.append(record)

    if record_found:
        write_records(updated_records)
        print("\n✅ Record updated successfully!")
    else:
        print(f"\n❌ No record found with Student ID '{student_id}'.")


# 4. Delete (Remove a record)
def delete_record():
    """Deletes a student record from the CSV file."""
    student_id = input("Enter Student ID of the record to delete: ")
    records = read_records()
    
    # Create a new list of records, excluding the one to be deleted
    records_to_keep = [record for record in records if record['StudentID'] != student_id]

    if len(records) == len(records_to_keep):
        print(f"\n❌ No record found with Student ID '{student_id}'.")
    else:
        write_records(records_to_keep)
        print("\n🗑️ Record deleted successfully!")


# --- Main Menu and Program Execution ---
def menu():
    """Displays the main menu and handles user choices."""
    initialize_csv() # Ensure the CSV file exists
    
    while True:
        print("\n========= Student Management System =========")
        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Search for a Student Record")
        print("4. Update a Student Record")
        print("5. Delete a Student Record")
        print("6. Exit")
        print("===========================================")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_record()
        elif choice == '4':
            update_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            print("\n👋 Exiting the program. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 6.")

# Run the project
if __name__ == "__main__":
    menu()
