#import tkinter
#import tkinter.messagebox
import pickle

look_up = 1
add = 2
change = 3
delete = 4
quit = 5

def main():
    try:
        input_file = open("history_file.dat", "rb")
        history = pickle.load(input_file)

    except (FileNotFoundError, IOError):
        print("file not found, please add historical entry then quit to create the file.")
        history = {}
    choice = 0

    while choice != quit:
        choice = menu()
        if choice == look_up:
            look_up(history)
        elif choice == add:
            add(history)
        elif choice == change:
            change(history)
        elif choice == delete:
            delete(history)
        elif choice == quit:
            save(history)

def menu():
    print()
    print("Enter Historical Information")
    print("____________________________")
    print("1. Look up a Historical Entry")
    print("2. Add a Historical Entry")
    print("3. Change a Historical Entry")
    print("4. Delete a Historical Entry")
    print("5. Quit the program\n")

    choice = int(input("Enter the number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input('Enter a valid choice: '))
    return choice

def look_up(history):
    name = input("Enter a Historical name")
    print(history.get(name, 'not found'))

def add(history):
    name = input("Enter a Historical name")
    date = input("Enter the Historical date")
    if name not in history:
        history[name] = date
    else:
        print('That entry already exists.')

def change(history):
    name = input("Enter the Historical name")
    if name in history:
        email = input('Enter the new Historical name: ')
        history[name] = email
    else:
        print("This Historical figure has not been found.")

def delete(history):
    name = input("Enter the Historical figure's name:  ")
    if name in history:
        del history[name]
    else:
        print("That historical figure was not found. ")

def save(history):
    print("The Data file has been updated with your changes. ")
    save_file = open('history_file.dat', 'wb')
    pickle.dump(history, save_file)
    save_file.close()

main()

#class historyGUI:
    #def __init__(self):
        #self.main_window = tkinter.Tk()
        #self.top_frame = tkinter.Frame(self.main_window)
        #self.middle_frame = tkinter.Frame(self.main_window)
        #self.bottom_frame = tkinter.Frame(self.main_window)




