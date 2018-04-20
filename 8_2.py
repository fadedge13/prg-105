def main():
    phoneNumb = input('Enter the number in the format of 555-XXX-XXXX\n')
    phoneNumb = phoneNumb.split('-')

    for var in phoneNumb[1:2]:
        for character in var:
            if character == 'A' or character == 'B' or character == 'C':
                character = '2'
            elif character == 'D' or character == 'E' or character == 'F':
                character = '3'
            elif character == 'G' or character == 'H' or character == 'I':
                character = '4'
            elif character == 'J' or character == 'K' or character == 'L':
                character = '5'
            elif character == 'M' or character == 'N' or character == 'O':
                character = '6'
            elif character == 'P' or character == 'Q' or character == 'R':
                character = '7'
            elif character == 'S' or character == 'T' or character == 'U':
                character = '8'
            elif character == 'V' or character == 'W' or character == 'X' or character == 'Z':
                character = '9'
    print(phoneNumb)
main()
