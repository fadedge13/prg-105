class list:

    def __init__(self, name, age, address, phone):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

    # TODO Set methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

def main():
    teacher = list("Meri", "47", "8900 Route 14", "815-455-8939")
    me = list("Brandon", "26", "812 Brookside dr", "704-214-6412")
    friend = list("Erich", "29", "507 Lincoln Ave", "815-555-9870")

    # Plus or commas never both
    print(teacher.get_name(), teacher.get_age(), teacher.get_address(), teacher.get_phone())
    print(me.get_name(), me.get_age(), me.get_address(), me.get_phone())
    print(friend.get_name(), friend.get_age(), friend.get_address(), friend.get_phone())

main()
