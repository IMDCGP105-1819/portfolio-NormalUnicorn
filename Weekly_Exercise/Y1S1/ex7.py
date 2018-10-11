def maths(deposit, monthly_saved):
    savings = 0.0
    months = 0
    while savings < deposit and months !=250:
        savings += savings*(0.04/12) + monthly_saved
        months += 1
        print(savings)

    if months < 250:
        print("It will take you ", months, " moth(s) to save up for a deposit for your ideal house")
    else:
        print("You may be dreaming a bit too big there buddy")


def inputs():
    total_cost = float(input("Please enter how much your ideal house costs: (£)"))
    deposit = total_cost*0.2
    #Cost of the house, you only need to save up for the deposit
    annual_salary = float(input("Please enter how much you earn annualy: (£)"))
    monthly_salary = annual_salary/12
    #How much is earned every month
    monthly_savings = float(input("Please enter how much you plan on saving each month"))
    monthly_saving = monthly_savings/100
    monthly_saved = monthly_salary*monthly_saving
    #How much money is invested to the deposit each month
    maths(deposit, monthly_saved)

inputs()
