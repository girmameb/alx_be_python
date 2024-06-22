# To calculate saving and interest
monthly_income = int (input ("Enter your monthly income: "))
monthly_Expense = int (input ("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_Expense
monthly_savings = int (monthly_savings)
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are " , monthly_savings)
print ("Projected savings after one year, with interest, is:" , Projected_Savings)
