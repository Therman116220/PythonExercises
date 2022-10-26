

movies_in_theaters = {
    'Inception': '12:00pm',
    'The Internship': '4:00pm',
    'Black Adam': '11:00pm',
    'Santa Clause': '10:30pm'
}
'''Adding()'''
movies_in_theaters['Deadpool 3'] = '11:00pm'
movies_in_theaters['The Pursuit Of Happiness'] = '6:00pm'
movies_in_theaters['movieName'] = 'soon to be deleted'


'''Removing()'''
print('Pre: ')
print(movies_in_theaters)
movies_in_theaters.pop('movieName')
print('Post: ')
print(movies_in_theaters)

'''Delete Last in'''
movies_in_theaters['Last in'] = 'FirstOut'
print('LIFO kinda: ')
print(movies_in_theaters)
movies_in_theaters.popitem()
print(movies_in_theaters)
print('Remove by key name: ')
del movies_in_theaters['Deadpool 3']
print(movies_in_theaters)