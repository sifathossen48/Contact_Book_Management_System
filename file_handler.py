import csv

def save_contact(contact, filename):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([contact.name, contact.phone, contact.email, contact.address])

def load_contacts(filename):
    contacts = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("Contacts file not found. A new file will be created.")
    return contacts

def overwrite_contacts(contacts, filename):
    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)