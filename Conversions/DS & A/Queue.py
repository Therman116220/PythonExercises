import queue
from  queue import Queue
'''First In First Out (FIFO)'''




library_collection = Queue()


library_collection.put("Catcher In The Rye")
library_collection.put("Brave New World")









listed_queue = list(library_collection.queue)
print(listed_queue)





q = queue.Queue()

numqueue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numqueue)):

    print(numqueue)
    print("List #: ", i)

'''

Terminal Response:
For loop loops through the "length" of the "numqueue" array exactly like java & prints the concatenation 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  0
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  6
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  7
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  8
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List #:  9

& a list of local gas stations

['Shell', 'Chevron', 'Buckeyes', 'Loves', 'QT', 'Seven-Eleven', 'Circle K', 'Valero', 'Exxon']



'''








fuelstop_queue = Queue()


fuelstop_queue.put("Shell")
fuelstop_queue.put("Chevron")
fuelstop_queue.put("Buckeyes")
fuelstop_queue.put("Loves")
fuelstop_queue.put("QT")
fuelstop_queue.put("Seven-Eleven")
fuelstop_queue.put("Circle K")
fuelstop_queue.put("Valero")
fuelstop_queue.put("Exxon")

'''queueName.get()'''

''' To utilize queueName i'm making it into a list '''
listed_queue = list(fuelstop_queue.queue)
print(listed_queue)


