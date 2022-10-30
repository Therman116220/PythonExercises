import queue
from  queue import Queue
'''First In First Out (FIFO)'''


q = queue.Queue()

numqueue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for i in range(len(numqueue)):

    if i == i:
     q.put(i)
    print(numqueue)
    print("List #: ", i)


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


