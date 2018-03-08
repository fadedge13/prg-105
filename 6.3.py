
def main():
    try:
        input_file = open('numbers2.txt', 'r')
        total_sum = 0
        count = 0
        for line in input_file:
            try:
                count += 1
                record = float(line)
                total_sum += record
            except ValueError:
                print("This item is not a number:")
                print("\t" + str(line))
                break
        input_file.close()
        ave = total_sum/count
        print("There were a total of " + str(count) + " numbers")
        print('The average of the numbers was ' + format(ave, '.2f'))
    except IOError:
        print("Could not find the file: " + input_file)
main()
