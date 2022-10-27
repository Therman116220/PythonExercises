'''Similar to a Nested array, a list of lists'''
import random

lunchMenu = ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J']

print('Menu: ', lunchMenu)

random_item = random.choice(lunchMenu)
print('Breakfast: ' + str(random_item))



'''lunchMenu = [[ 'Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J']]


# printing original list
print("Original list is : " + str(lunchMenu))

# using random.choice() to
# get a random number
random_num = random.choice(lunchMenu)

# printing random number
print("Random selected number is : " + str(random_num))
'''