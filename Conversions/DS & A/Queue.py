import queue
from  queue import Queue

q = queue.Queue()
numqueue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numqueue:
    q.put(i)
    print("Numbers: ", i)



newnamesqueue = Queue()


newnamesqueue.put("Shell")
newnamesqueue.put("Chevron")
newnamesqueue.put("Buckeyes")
newnamesqueue.put("Loves")
newnamesqueue.put("QT")
newnamesqueue.put("Seven-Eleven")
newnamesqueue.put("Circle K")
newnamesqueue.put("Valero")
newnamesqueue.put("Exxon")

'''queueName.get()'''

''' To utilize queueName i'm making it into a list '''
print(list(newnamesqueue.queue))


