total_cost = float(input("Please enter how much your ideal house should cost:"))
annual_salary = float(input("Please enter your annual salary:"))
monthly_savings_value = float(input("Please enter the %  of your annual salary you intend to save each month:"))
monthly_savings = (annual_salary/12)*monthly_savings_value
semi_annual_raise = float(input("Please enter how much of a raise you receieve every 6 months"))
#All of these variables are used input based

deposit = total_cost*0.2
current_savings = 0.0
months = 1

while current_savings < deposit and months != 250:
    if months % 6 == 0:
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
        monthly_savings = (annual_salary/12)*monthly_savings_value
    current_savings += current_savings*(0.04/12) + monthly_savings
    print(current_savings)
    months += 1

print(months)
