def main():
    total = 0
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    my_list = []

    for month in months:
        current_rainfall = int(input("How much rain did you get in " + month + " "))
        total += current_rainfall
        my_list.append(current_rainfall)

    minimum = min(my_list)
    maximum = max(my_list)
    min_index = my_list.index(minimum)
    # print("Min index " + min_index)
    max_index = my_list.index(maximum)
    ave = total/12
    print("The average amount of rainfall is ", format(ave, ",.2f"))
    print("The min amount of rainfall is ", months[min_index])
    print("The max amount of rainfall is", months[max_index])
main()
