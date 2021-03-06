# Write a program that uses nested loops to collect data
# and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate 12 times,
# once for each month. Each iteration of the inner loop will ask the user
# for the inches of rainfall for that month. After all iterations,
# the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.

num_year = int(input("How many years do you want to track?"))
num_month = 12
total = 0
for years in range(num_year):
	print("_________ Year" + str(years + 1) + "________")
	for month in range(num_month):
		current_rainfall = int(input("How much rain did you get in a month " + str(month + 1) + ": "))
		total += current_rainfall


ave = total/(num_month * num_year)
print("The average amount of rainfall is ", format(ave, ",.2f"))
