import  random
''' Simple Password hasher'''
size = int(input("Enter desired password length\n"))
characters = "qwertyuiopasdfghjklzxcvbnm,./;'[]\<>?:()QWERTYUIOPASDFGHJKLZXCVBNM0987654321"
randomize = "".join(random.sample(characters, size))
print("You picked " + str(size))
print("Your Password is " + randomize)

''' Hashing '''


