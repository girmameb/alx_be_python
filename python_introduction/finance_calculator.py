# To calculate saving and interest
minc = input ("Enter your monthly income: ")
mexpen = input ("Enter your total monthly expenses: ")
minc = float(minc)
mexpen = float (mexpen)
sav = minc - mexpen
save = sav * 12 + (sav* 12 * 0.05)
print ("Your monthly savings are " , sav)
print ("Projected savings after one year, with interest, is:" , save)
