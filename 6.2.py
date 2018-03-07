
def main():
	input_file = open('numbers.txt', 'r')
	total_sum = 0
	count = 0
	for line in input_file:
		count += 1
		record = float(line)
		total_sum += record

	input_file.close()
	ave = total_sum/count
	print("There were a total of", str(count), "numbers")
	print('The average of the numbers was', format(ave, '.2f'))
main()
