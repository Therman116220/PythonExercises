import  random
''' Simple Password Generator'''
'''Eventually it will store passwords in the array of subscription names and randomize them all on call'''

size = int(input("Enter desired password length\n"))
characters = "qwertyuiopasdfghjklzxcvbnm,./;'[]\<>?:()QWERTYUIOPASDFGHJKLZXCVBNM0987654321"
randomize = "".join(random.sample(characters, size))
print("You picked " + str(size))
print("Your Password is " + randomize)
''' n is of elements as input'''
n = int(input("Enter number of elements : "))

lst = []



for i in range(0, n):



    lst.append(randomize)
print(randomize)
print(lst)






''' Hashing '''


