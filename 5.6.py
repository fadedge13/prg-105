
def main():
    total_grade = ask_for_score()
    final_grade = determine_grade(total_grade)

def determine_grade(total_grade):
    if total_grade > 100:
        print("+A")
    elif 100 > total_grade >= 90:
        print("A")
    elif 90 > total_grade > 80:
        print("B")
    elif 80 > total_grade > 70:
        print("C")
    elif 70 > total_grade > 60:
        print("D")
    else:
        print("F")

def ask_for_score():
    test1 = float(input("Please enter your first test score: "))
    test2 = float(input("Please enter your second test score: "))
    test3 = float(input("Please enter your third test score: "))
    test4 = float(input("Please enter your fourth test score: "))
    test5 = float(input("Please enter your fifth test score: "))
    total_test_score = (test1 + test2 + test3 + test4 + test5)
    total_score = total_test_score / 5
    print("Your average test score is: " + format(total_score, ',.2f'))
    return total_score

main()

