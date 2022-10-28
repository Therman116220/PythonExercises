
# Predicting the Boolean type output

# 1
x = 2
print(x * 5 == 10)
# True

# 2
y = 27
print(y >= 100)
# False

# 3
coins = 35
coins += 10
print(coins > 40)
# True

# Change Checker
quarters = 16
dimes = 25
pennies = 500

totalPennies = pennies * .01
totalDimes = dimes * .10
totalQuarters = quarters * .25

totalChange = (pennies * .01) + (quarters * .25) + (dimes * .10)
print('Total Quarters: ', totalQuarters)
print('Total Dimes: ', totalDimes)
print('Total Pennies: ', totalPennies)
print(totalChange)
print(totalChange <= 10.00)


