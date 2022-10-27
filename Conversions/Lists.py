import random

lunchMenu = ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J']
'''dinnerMenu = ['Lasagna', 'Hawaiian Pizza', 'Tacos', 'Chicken & Rice' ]'''
print('Menu: ', lunchMenu)

random_item = random.choice(lunchMenu)
print('Breakfast: ' + str(random_item))
