# To calculate saving and interest
monthly_incomes = input ("Enter your monthly income: ")
monthly_Expenses = input ("Enter your total monthly expenses: ")
monthly_incomes = float(monthly_incomes)
monthly_Expense = float (monthly_Expenses)
monthly_savings = monthly_incomes - monthly_Expenses
monthly_savings = float (monthly_savings)
save = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are " , monthly_savings)
print ("Projected savings after one year, with interest, is:" , save)
