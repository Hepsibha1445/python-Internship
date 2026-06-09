# ================================================
#   Contact Book - CLI Application
#   Features: Add, View, Search, Delete contacts
#   Storage: List of dictionaries (in-memory)
# ================================================

contacts = []  # List of dictionaries to store contacts


def add_contact():
    """Add a new contact to the contact book."""
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    # Check for duplicate name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"⚠️  A contact with the name '{name}' already exists.")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"✅ Contact '{name}' added successfully!")


def view_all_contacts():
    """Display all contacts in the contact book."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("📭 No contacts found. Add some contacts first!")
        return

    print(f"{'No.':<5} {'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 60)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i:<5} {contact['name']:<20} {contact['phone']:<15} {contact['email']}")
    print(f"\nTotal contacts: {len(contacts)}")


def search_contact():
    """Search for a contact by name."""
    print("\n--- Search Contact ---")
    query = input("Enter name to search: ").strip().lower()
    if not query:
        print("❌ Search query cannot be empty.")
        return

    results = [c for c in contacts if query in c["name"].lower()]

    if not results:
        print(f"🔍 No contacts found matching '{query}'.")
    else:
        print(f"\nFound {len(results)} result(s):\n")
        print(f"{'Name':<20} {'Phone':<15} {'Email'}")
        print("-" * 55)
        for contact in results:
            print(f"{contact['name']:<20} {contact['phone']:<15} {contact['email']}")


def delete_contact():
    """Delete a contact by name."""
    print("\n--- Delete Contact ---")
    name = input("Enter the name of contact to delete: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            confirm = input(f"⚠️  Are you sure you want to delete '{contact['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                contacts.remove(contact)
                print(f"🗑️  Contact '{contact['name']}' deleted successfully.")
            else:
                print("❌ Deletion cancelled.")
            return

    print(f"🔍 No contact found with the name '{name}'.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("       📒  CONTACT BOOK")
    print("=" * 40)
    print("  1. ➕  Add New Contact")
    print("  2. 📋  View All Contacts")
    print("  3. 🔍  Search by Name")
    print("  4. 🗑️   Delete Contact")
    print("  5. 🚪  Exit")
    print("=" * 40)


def main():
    """Main function to run the contact book CLI app."""
    print("Welcome to your Contact Book! 📒")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n👋 Goodbye! Your contacts session has ended.")
            break
        else:
            print("⚠️  Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()