from Flatmates_bill import Bill, Flatmate 





if __name__ == "__main__":
    print("Welcome to Flatmate bill app")
    bill_amount = float(input('Please enter bill amount: '))
    billed_month_year = input('Please enter bill month and year. Ex: March 2024: ')

    flatmate_1_name = input('Please enter name of flatmate 1: ')
    flatmate_1_days = int(input('Please enter days stayed by flatmate 1: '))

    flatmate_2_name = input('Please enter name of flatmate 2: ')
    flatmate_2_days = int(input('Please enter days stayed by flatmate 2: '))

    b1 = Bill(amount=bill_amount, period=billed_month_year)

    f1 = Flatmate(name=flatmate_1_name, no_of_days=flatmate_1_days)
    f2 = Flatmate(name=flatmate_2_name, no_of_days=flatmate_2_days)

    print("Flatmate 1 pays: ", f1.bill_generation(b1, f2))
    print("Flatmate 2 pays: ", f2.bill_generation(b1, f1))





