'''Drill One'''

'''* Yield Utility Statement : https://www.simplilearn.com/tutorials/python-tutorial/yield-in-python'''


def fibonacci():
    x = 1
    y = 1
    while True:
        yield x
        x, y = y, x + y


for i, num in enumerate(fibonacci()):
    print(f"%d" % num)
    if i == 15:
        break
