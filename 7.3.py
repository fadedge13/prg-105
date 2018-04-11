def main():
    user_input = input("Enter a boy or girls name: ")
    input_file = open('BoyNames.txt', 'r')
    boy_names = input_file.readlines()
    input_file_2 = open('GirlNames.txt', 'r')
    girl_names = input_file_2.readlines()

    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index += 1
    print(boy_names)

    index = 0

    while index < len(girl_names):
        girl_names[index] = girl_names[index].rstrip('\n')
        index += 1

    print(girl_names)

    if user_input in boy_names:
        print(user_input, "is one of the top boy names.")
    else:
        print(user_input, "is not one of the top boy names.")

    if user_input in girl_names:
        print(user_input, "is one of the top girl names")
    else:
        print(user_input, "is not one of the top girl names.")
    input_file.close()

main()

