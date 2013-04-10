def add_phone(book, name, phone):
    book.append({"Name":name,"Phone":phone})
    return book


def find_entry():
    search_name = input("Search on name: ")
    return_entry = {}
    for entry in phone_book:
        if entry["Name"].lower() == search_name.lower():
            return_entry = entry
            break
    return return_entry


def display_list(book):
    for entry in book:
        print("{0}\t{1}".format(entry["Name"], entry["Phone"]))
    print()

phone_book = []
while True:
    selection = input("(A)dd, (L)ist, (S)ort, (F)ind, (D)elete or (Q)uit: ")
    selection = selection.upper()
    if selection == "Q":
        break
    elif selection == "A":
        name = input("Enter a name: ")
        phone = input("Enter a phone: ")
        add_phone(phone_book, name, phone)
    elif selection == "L":
        display_list(phone_book)
    elif selection == "S":
        sorted_list = sorted(phone_book, key=lambda entry: entry["Name"])
        display_list(sorted_list)
    elif selection == "F":
        display_entry = find_entry()
        print("Found: {0} - {1}".format(display_entry["Name"], display_entry["Phone"]))
    elif selection == "D":
        entry = find_entry()
        phone_book.remove(entry)
    else:
        print("Unknown selection")
