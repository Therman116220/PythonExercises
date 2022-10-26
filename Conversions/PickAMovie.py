

morning_movies_in_theaters = {
    'Inception': '12:00am',
    'The Internship': '4:00am',
    'Black Adam': '11:00am',
    'Santa Clause': '10:30am'
}

evening_movies_in_theaters = {
    'Bicentennial Man': '10:30pm',
    'Remember The Titans': '11:00pm',
    'In Time': '9:30pm'

}

'''Adding()'''
morning_movies_in_theaters['Deadpool 3'] = '11:00am'
morning_movies_in_theaters['The Pursuit Of Happiness'] = '6:00am'
morning_movies_in_theaters['movieName'] = 'soon to be deleted'


'''Removing()'''
print('Pre: ')
print(morning_movies_in_theaters)
morning_movies_in_theaters.pop('movieName')
print('Post: ')
print(morning_movies_in_theaters)

'''Delete Last in'''
morning_movies_in_theaters['Last in'] = 'FirstOut'
print('LIFO kinda: ')
print(morning_movies_in_theaters)
morning_movies_in_theaters.popitem()
print(morning_movies_in_theaters)
print('Remove by key name: ')
del morning_movies_in_theaters['Deadpool 3']
print(morning_movies_in_theaters)


'''Clear'''
print('Clearing dictionary: ')
morning_movies_in_theaters.clear()
print(morning_movies_in_theaters)


