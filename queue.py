#queue=[]
#queue.append(1)
#queue.append(2)
#queue.append(3)
#queue.append(4)

#while (queue):
    #print(queue[0])
   # queue.pop(0)



def enqueue(ele):
    queue.append(ele)
def dequeue():
    print(queue[0])
    queue.pop(0)

queue=[]
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)

dequeue()
