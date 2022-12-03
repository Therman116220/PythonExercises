'''Basic Recursion in Python'''

def countdown(num):
    if num == 0:
        print('Insert loud bang here')
    else:
        print(num)
        countdown(num - 1)

countdown(5)