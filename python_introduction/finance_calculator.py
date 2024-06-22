# To calculate saving and interest
monthly_incomes = float(input ("Enter your monthly income: "))
monthly_Expenses = float(input ("Enter your total monthly expenses: "))
monthly_savings = monthly_incomes - monthly_Expenses
monthly_savings = float (monthly_savings)
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are " , monthly_savings)
print ("Projected savings after one year, with interest, is:" , Projected_Savings)
