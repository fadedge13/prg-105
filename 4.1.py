# Running on the Treadmill
# Each minute ran 4.2 calories are burned
# How many calories are burned in 10, 15, 20, 25, and 30 minutes

print("calories burned per minutes on treadmill")

cal = (4.2)

for minutes in [10,15,20,25,30]:
    print("cal burned in " + str(minutes) + " minutes: " + format(cal * minutes , ",.2f"))


