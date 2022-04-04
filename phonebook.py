hasQuit = False
phonebook = {}

menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
"""

phonebook = {}

while not(hasQuit):
    print (menu)

    selected_option = input("what do you want to do (1-5)?")

    if selected_option == "2":
        name = input("What is the contact's name?")
        phone_number = input("What is their number?")
        phonebook[name] = phone_number
        print("Contact added succesfully!")

    elif selected_option == "1":
        name = input("What contact's number would you like")
        print("Here's their number:", phonebook[name])
    
    elif selected_option == "3":
        print("Remove Name and Number")
        name = input("Name: ")
        if name in phonebook:
            del phonebook[name]
        else:
            print(name, "Was not found")
    
    elif selected_option == "4":
        print("Lookup Number")
        name = input("Name: ")
        if name in phonebook:
            print("The number is", phonebook[name])
        else:
            print(name, "Was not found")

    elif selected_option == "5":
        hasQuit = True
        
