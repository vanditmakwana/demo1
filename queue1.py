from queue import Queue

q=Queue(maxsize=3)
print("queue size",q.qsize())

q.put(1)
q.put(2)
q.put(3)
print("queue is full",q.full())

print("element queue")
print(q.get())
print(q.get())
print(q.get())
print("queue is full or not",q.empty())

q.put(1)
print("queue is full or not",q.full())
print("queue is full or not",q.empty())
