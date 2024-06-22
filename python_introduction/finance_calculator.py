# To calculate saving and interest
minc = input ("Enter your Monthly Income ")
mexpen = input ("Enter your Monthly Expense ")
minc = float(minc)
mexpen = float (mexpen)
sav = minc - mexpen
save = sav * 12 + (sav* 12 * 0.05)
print ("Your monthly savings are " , sav)
print ("Projected savings after one year, with interest, is:" , save)
