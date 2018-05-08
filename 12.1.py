def main():
    number(int(input('How many monkeys are jumping on the bed?')))

def number(times):
    count = 0
    while count < times:
        print(times, ' times the monkeys fell of the bed')
        print(times, ' time the mother called the doctor')
        times -= 1
        print(times, 'number of monkeys still jumping on the bed? \n\n')

main()
