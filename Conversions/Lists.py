import random

lunchMenu = ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J']
'''dinnerMenu = ['Lasagna', 'Hawaiian Pizza', 'Tacos', 'Chicken & Rice' ]'''
print('Menu: ', lunchMenu)

random_item = random.choice(lunchMenu)
print('Breakfast: ' + str(random_item))

print('-----------------------------------------')


'''Dictionary of Lists'''

daily_menu = {
    'Breakfast': ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J'],
    'Lunch': ['Salad', 'Pizza', 'Sandwich'],
    'Dinner': ['Chicken & Rice', 'Pizza', 'Sandwich']
}


print('Breakfast:\t', daily_menu['Breakfast'])
print('Lunch:\t', daily_menu['Lunch'])
print('Dinner:\t', daily_menu['Dinner'])





