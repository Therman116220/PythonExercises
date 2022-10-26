
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



'''    
Grabbing a item that might not be there will result in a
KeyError: ' ' error

'''