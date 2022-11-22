
dictionary = {
    'Key': 'Value',
    'KeyTwo': 'ValueTwo',

    'KeyThree': 'ValueThree',
    'KeyFour': 'Value'
}
'''Reminder: Values Can repeat'''

CollectionOfData = 'Key' + 'KeyTwo'
COD = dictionary.get('Key') + dictionary.get('KeyTwo')
print(COD)
print(dictionary['Key'])
print(dictionary['KeyTwo'])

del dictionary['Key']
del dictionary['KeyFour']
print(dictionary)



person = {

    'FirstName': 'John',
    'LastName': 'Doe',
    'age': '23',
}
print(person.get('FirstName'), person.get('LastName'), person.get('age'))
print('Hi, my name is', person.get('FirstName'), person.get('LastName'))