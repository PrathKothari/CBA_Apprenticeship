import csv
import os

CSV_FILE = 'patients.csv'
CSV_HEADER = ['PatientID', 'Name', 'Age', 'Disease', 'DoctorAssigned']

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

# 1. Create (Add a new patient record)
def add_record():
    """Adds a new patient record to the CSV file."""
    print("\n--- Add New Patient Record ---")
    patient_id = input("Enter Patient ID: ")

    # Validation: Check if the PatientID already exists
    records = read_records()
    for record in records:
        if record['PatientID'] == patient_id:
            print(f"\n⚠️ Error: Patient with ID '{patient_id}' already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Assigned: ")

    new_record = {
        'PatientID': patient_id,
        'Name': name,
        'Age': age,
        'Disease': disease,
        'DoctorAssigned': doctor
    }

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADER)
        writer.writerow(new_record)

    print("\n✅ Patient record added successfully!")

# 2. Read (View all and Search for records)
def view_records():
    """Displays all patient records from the CSV file."""
    records = read_records()
    if not records:
        print("\n⚠️ No records found.")
        return

    print("\n--- All Patient Records ---")
    print(f"{'PatientID':<12} | {'Name':<20} | {'Age':<5} | {'Disease':<20} | {'Doctor Assigned':<20}")
    print("-" * 85)
    for record in records:
        print(f"{record['PatientID']:<12} | {record['Name']:<20} | {record['Age']:<5} | {record['Disease']:<20} | {record['DoctorAssigned']:<20}")
    print("-" * 85)

def search_record():
    """Searches for patients assigned to a specific doctor."""
    doctor_name = input("Enter Doctor's Name to search for: ")
    records = read_records()
    
    found_records = [record for record in records if record['DoctorAssigned'].lower() == doctor_name.lower()]

    if found_records:
        print(f"\n--- Records Found for Dr. {doctor_name} ---")
        print(f"{'PatientID':<12} | {'Name':<20} | {'Age':<5} | {'Disease':<20}")
        print("-" * 65)
        for record in found_records:
            print(f"{record['PatientID']:<12} | {record['Name']:<20} | {record['Age']:<5} | {record['Disease']:<20}")
        print("-" * 65)
    else:
        print(f"\n❌ No records found for a doctor named '{doctor_name}'.")

# 3. Update (Modify an existing record)
def update_record():
    """Updates an existing patient record identified by PatientID."""
    patient_id = input("Enter Patient ID of the record to update: ")
    records = read_records()
    record_found = False
    updated_records = []

    for record in records:
        if record['PatientID'] == patient_id:
            record_found = True
            print("\n--- Updating Record ---")
            print("Enter new details (leave blank to keep current value):")
            
            new_name = input(f"New Name (current: {record['Name']}): ")
            new_age = input(f"New Age (current: {record['Age']}): ")
            new_disease = input(f"New Disease (current: {record['Disease']}): ")
            new_doctor = input(f"New Doctor Assigned (current: {record['DoctorAssigned']}): ")

            if new_name: record['Name'] = new_name
            if new_age: record['Age'] = new_age
            if new_disease: record['Disease'] = new_disease
            if new_doctor: record['DoctorAssigned'] = new_doctor
            
        updated_records.append(record)

    if record_found:
        write_records(updated_records)
        print("\n✅ Record updated successfully!")
    else:
        print(f"\n❌ No record found with Patient ID '{patient_id}'.")

# 4. Delete (Remove a record)
def delete_record():
    """Deletes a patient record from the CSV file by PatientID."""
    patient_id = input("Enter Patient ID of the record to delete: ")
    records = read_records()
    
    records_to_keep = [record for record in records if record['PatientID'] != patient_id]

    if len(records) == len(records_to_keep):
        print(f"\n❌ No record found with Patient ID '{patient_id}'.")
    else:
        write_records(records_to_keep)
        print("\n🗑️ Record deleted successfully!")

# --- Main Menu and Program Execution ---
def menu():
    """Displays the main menu and handles user choices."""
    initialize_csv()
    
    while True:
        print("\n========= Patient Record System =========")
        print("1. Add Patient Record")
        print("2. View All Patient Records")
        print("3. Search Records by Doctor")
        print("4. Update a Patient Record")
        print("5. Delete a Patient Record")
        print("6. Exit")
        print("=========================================")
        
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
