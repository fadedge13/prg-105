import random
def main():
    number = get_number()
    my_list = get_list(number)
    filter_number(my_list, number)

def get_list(number_from_user):
    my_randoms = random.sample(range(number_from_user, 101), 20)
    return my_randoms

def get_number():
    while True:
        try:
            x = int(input("Please enter a number: "))
            if x <= 100:
                return x
            else:
                print("Number not in range 1 to 100")
        except ValueError:
                print("That was no valid number. Try again...")



def filter_number(my_list, number):
    filter_numbers = []
    for num in my_list:
        if num > number:
            filter_numbers.append(num)
        if len(filter_numbers) <= 0:
            print("No result found")
#        else:
    print(filter_numbers)


main()
