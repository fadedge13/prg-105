def main():
    phoneNumb = input('Enter the number in the format of 555-XXX-XXXX\n')
    newPhoneNumb = ''
    for var in phoneNumb:
        if var.isalpha():
            var = var.upper()
            if var == 'A' or var == 'B' or var == 'C':
                newPhoneNumb += '2'
            elif var == 'D' or var == 'E' or var == 'F':
                newPhoneNumb += '3'
            elif var == 'G' or var == 'H' or var == 'I':
                newPhoneNumb += '4'
            elif var == 'J' or var == 'K' or var == 'L':
                newPhoneNumb += '5'
            elif var == 'M' or var == 'N' or var == 'O':
                newPhoneNumb += '6'
            elif var == 'P' or var == 'Q' or var == 'R':
                newPhoneNumb += '7'
            elif var == 'S' or var == 'T' or var == 'U':
                newPhoneNumb += '8'
            elif var == 'V' or var == 'W' or var == 'X' or var == 'Z':
                newPhoneNumb += '9'
        else:
            newPhoneNumb += str(var)

    print(newPhoneNumb)
main()
