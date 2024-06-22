# To calculate saving and interest
monthly_income = input ("Enter your monthly income: ")
monthly_Expense = input ("Enter your total monthly expenses: ")
monthly_income = float(monthly_income)
monthly_Expense = float (monthly_Expense)
monthly_saving = monthly_income - monthly_Expense
save = monthly_saving * 12 + (monthly_saving * 12 * 0.05)
print ("Your monthly savings are " , monthly_saving)
print ("Projected savings after one year, with interest, is:" , save)
