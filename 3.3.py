age = int(input("What age group does a person fall under?"))
if age <= 1:
    print("This person is an infant.")
elif age < 13:
    print("This person is a child.")
elif age < 20:
    print("This person is a teenager.")
elif age >= 20:
    print("This person is an adult.")
else:
    print("Incorrect value.")
