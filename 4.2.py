#How many days will you work for pennies a day? 15

print("Money gained after x days for pennies a day")

pay = (0.01)
days = int(input("How many days did you work?"))
total = 0

for day in range(days):
    print "Days of work:  " + format((day + 1), "15,.0f") + " Pay: $ " + format(pay, "15,.2f")
    pay *= 2
    total += pay







