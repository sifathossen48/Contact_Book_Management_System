from file_handler import save_contact, load_contacts, overwrite_contacts

class ContactBook:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = load_contacts(filename)

    def add_contact(self, contact):
        if any(c["phone"] == contact.phone for c in self.contacts):
            print("Error: A contact with this phone number already exists.")
        else:
            self.contacts.append(contact.to_dict())
            save_contact(contact, self.filename)
            print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

    def search_contact(self, query):
        results = [c for c in self.contacts if query.lower() in c["name"].lower() or query in c["phone"] or query.lower() in c["email"].lower()]
        if results:
            for contact in results:
                print(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
        else:
            print("No contacts found.")

    def edit_contact(self, phone):
        for contact in self.contacts:
            if contact["phone"] == phone:
                contact["name"] = input(f"Enter new name ({contact['name']}): ") or contact["name"]
                contact["email"] = input(f"Enter new email ({contact['email']}): ") or contact["email"]
                contact["address"] = input(f"Enter new address ({contact['address']}): ") or contact["address"]
                overwrite_contacts(self.contacts, self.filename)
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, phone):
        self.contacts = [c for c in self.contacts if c["phone"] != phone]
        overwrite_contacts(self.contacts, self.filename)
        print("Contact deleted successfully.")
