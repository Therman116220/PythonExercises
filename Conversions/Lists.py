import random


print('Randomizer:')
lunchMenu = ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J']
'''dinnerMenu = ['Lasagna', 'Hawaiian Pizza', 'Tacos', 'Chicken & Rice' ]'''
print('Menu: ', lunchMenu)

random_item = random.choice(lunchMenu)
print('Breakfast: ' + str(random_item))

print('-----------------------------------------')


'''Dictionary of Lists'''

daily_menu = {
    'Breakfast:': ['Pop Tart', 'Croissant', 'Chicken Soup', 'PB & J'],
    'Lunch:': ['Salad', 'Pizza', 'Sandwich'],
    'Dinner:\n': ['Chicken & Rice', 'Pizza', 'Sandwich']
}
'''print('Print Keys but not values')
for item in daily_menu:
    print(item)'''

for name, daily_menu in daily_menu.items():
    print(name)
    for item in daily_menu:
        print('\t' + item)
    print('-----------------------------------------')
'''print('Breakfast:', daily_menu['Breakfast'])
print('Lunch:', daily_menu['Lunch'])
print('Dinner:', daily_menu['Dinner'])
'''




