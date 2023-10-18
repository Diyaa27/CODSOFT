# Define a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added successfully.")

# Function to view the contact list
def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("\n")

# Function to search for a contact
def search_contact():
    query = input("Enter a name or phone number to search: ")
    results = []
    for name, details in contacts.items():
        if query in name or query in details['Phone']:
            results.append((name, details))
    if results:
        print("Search Results:")
        for name, details in results:
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("\n")
    else:
        print("No results found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print("Update the contact details:")
        phone = input(f"New phone number for {name} (leave empty to keep it unchanged): ")
        email = input(f"New email for {name} (leave empty to keep it unchanged): ")
        address = input(f"New address for {name} (leave empty to keep it unchanged): ")
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found in the list.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in the list.")

# Main menu
while True:
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the Contact Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
