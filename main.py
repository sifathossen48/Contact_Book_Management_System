from contact_book import ContactBook
from contact import Contact
from validators import validate_email, validate_phone, get_valid_input

book = ContactBook()
print("Welcome to the Contact Book Management System!")

while True:
    print("\nMenu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = get_valid_input(
            "Enter phone: ",
            validate_phone,
            "Invalid phone number. It must be 11 digits."
        )

        email = get_valid_input(
            "Enter email: ",
            validate_email,
            "Invalid email format."
        )
        address = input("Enter address: ")
        book.add_contact(Contact(name, phone, email, address))

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        query = input("Enter name, phone, or email to search: ")
        book.search_contact(query)

    elif choice == "4":
        phone = input("Enter phone of contact to edit: ")
        book.edit_contact(phone)

    elif choice == "5":
        phone = input("Enter phone of contact to delete: ")
        book.delete_contact(phone)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")