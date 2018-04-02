total = 0
def main():
    global total
    total_fat_consumed = ask_for_fat()
    total_carbs_consumed = ask_for_carbs()
    total_protein_consumed = ask_for_protein()
    print("The total amount of calories consumed: " + str(total))

def ask_for_fat():
    global total
    fat_grams = float(input("What was the total amount of fat calories you consumed: "))
    calories_from_fat = fat_grams * 9
    total = calories_from_fat

def ask_for_carbs():
    global total
    carbs_grams = float(input("What was teh total amount of carb calories you consumed: "))
    calories_from_carbs = carbs_grams * 4
    total = calories_from_carbs

def ask_for_protein():
    global total
    protein_grams = float(input("What was the total amount of protein calories you consumed: "))
    calories_from_protein = protein_grams * 4
    total = calories_from_protein

main()
