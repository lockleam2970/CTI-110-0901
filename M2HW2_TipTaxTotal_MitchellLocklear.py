
#CTI-110
#M2HW2-Tip Tax Total
#Mitchell Locklear
#09/06/2017

user_input = input('How much did the meal cost? ')
tipAmount = .18*int(user_input)
salesTax = .07* int(user_input)
totalCost = int(user_input)+int(salesTax)+int(tipAmount)

print ('The tip amount for your meal is', tipAmount)
print ('The sales tax for your meal is', salesTax)
print ('The total cost for your meal is', totalCost)
