import pickle

look_up = 1
add = 2
change = 3
delete = 4
quit = 5

def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
        # print(customers)
    except (FileNotFoundError, IOError):
        print("file not found, please add a customer then quit to create the file ")
        customers = {}
    choice = 0

    while choice != quit:
        choice = menu()
        if choice == look_up:
            look_up(customers)
        elif choice == add:
            add(customers)
        elif choice == change:
            change(customers)
        elif choice == delete:
            delete(customers)
        elif choice == quit:
            save(customers)

def main():
    print()
    print("Customer email lookup")
    print("----------------------")
    print("1. Look up a customer's email account")
    print("2. Add a new customer's email account")
    print("3. Change an email account")
    print("4. Delete a customer's email account")
    print("5. Quit the program\n")

    choice = int(input("Enter the number of your choice:   "))
    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid choice: '))
    return choice

def look_up(customers):
    name = input("Enter a customer name: ")
    print(customers.get(name, 'Not Found'))

def add(custumers):
    name = input("Enter a customer name: ")
    email = input("Enter a customer email account")
    if name not in customers:
        customer[name] = phone
    else:
        print('That entry already exists.')

def change(cutomers):
    name =input("Enter the customer name: ")
    if name in customers:
        email = input('Enter the new email account: ')
        customers[name] = email
    else:
        print("That customer is not found.")

def delete(customers):
    name = input("Enter the customer name:  ")
    if name in customers:
        del customers[name]
    else:
        print("That customer was not found. ") 

