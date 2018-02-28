
def main():
	input_file = open('names.txt', 'r')

	count = 0
	record = input_file.readline()
	while record != "":
		print(record)
		record = input_file.readline()
		count += 1


	input_file.close()
	print("You have :" + str(count) + " records")


main()
