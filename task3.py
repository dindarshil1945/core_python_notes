phonebook = {}

while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = int(input("Enter phone number: "))
        email = input("Enter email: ")


        if name in phonebook:
            phonebook[name]['Phone'].append(phone)
            print("Phone number added to existing contact.")
        else:
            phonebook[name] = {'Phone': [phone], 'Email': email}
            print("Contact added.")

    elif choice == '2':
        if not phonebook:
            print("No contacts to show.")
        else:
            for name, info in phonebook.items():
                print({
                    'Name': name,
                    'Phone': info['Phone'],
                    'Email': info['Email']
                })

    elif choice == '3':
        name = input("Enter the name to update: ")
        if name in phonebook:
            update_phone = input("Do you want to add a new phone number? (y/n): ").lower()
            if update_phone == 'y':
                phone = int(input("Enter new phone number: "))
                phonebook[name]['Phone'].append(phone)
                print("Phone number added.")

            update_email = input("Do you want to update the email? (y/n): ").lower()
            if update_email == 'y':
                email = input("Enter new email: ")
                phonebook[name]['Email'] = email
                print("Email updated.")
        else:
            print("Contact not found.")

    elif choice == '4':
        name = input("Enter the name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == '5':
        print("Exited...")
        break

    else:
        print("Invalid choice. Try again.")
