def main():
    total_monthly_payment = ask_for_expenses()
    yerto = yearly_expense(total_monthly_payment)



def ask_for_expenses():
    monthly_loan_payment = float(input("How much do you pay for your loan every month: $"))
    monthly_insurance_payment = float(input("How much do you pay for your insurance every month: $"))
    monthly_gas_payment = float(input("How much do you pay for gas every month: $"))
    monthly_maintenance_payment = float(input("How much do you pay for maintenance every month: $"))
    total_monthly_payment = ( monthly_gas_payment + monthly_insurance_payment + monthly_loan_payment
                              + monthly_maintenance_payment)
    # if you are about to hit the page brake in a string hit 'enter' before the proper sign (in this case the plus).
    print("Your total monthly payment is: $", format(total_monthly_payment, ',.2f'))
    # it is better to add the decimal points towards the end when dealing with money formating.
    return total_monthly_payment
def yearly_expense(monthly):
    year = monthly * 12
    print("Your total monthly payment is: $" + format(year, ',.2f')) #for this type of string don't use commas.


main()
