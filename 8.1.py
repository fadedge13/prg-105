def main():
   full_name = input("Enter your first, middle, and last name. ")
   split_name = full_name.split()
   for initial in split_name:
       print(initial[0].upper() + '.', end='')
   print()
main()
