def maths(total_cost, annual_salary, monthly_savings):
    deposit = total_cost*0.2
    current_savings = 0
    counter = 0
    while current_savings < deposit and counter != 250:
        current_savings += current_savings*(0.04/12) + (annual_salary*monthly_savings)
        counter +=1
    print(counter)


def inputs():
    total_cost = float(input("Please enter how much your ideal house cost:"))
    annual_salary = float(input("Please enter your annual salary:"))
    monthly_savings = float(input("Please enter how much you want to save per month:"))
    maths(total_cost, annual_salary, monthly_savings)

inputs()
