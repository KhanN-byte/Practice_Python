'''

Haris Khan

Linked-List

Traversing Forward Nodes

'''

class Node: 

    # Initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    #Initialize the linked list object

    def __init__(self):
        self.head = None

    def contentlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next
            


if __name__ == "__main__":

    l_list = LinkedList()
    l_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    l_list.head.next = second
    second.next = third
    l_list.contentlist()



'''
Stack Data Structure 

LIFO / FIFO 

Last In First Out / First In First Out
'''

stk = []

stk.append('1')
stk.append('2')
stk.append('3')
# ['1', '2', '3']

stk.pop() # '3' goes out first
stk.pop() # '2' goes out next
stk.pop() # '1' goes out last

print(stk)


'''

Queue --> First In - First Out (FIFO)

Similar to Stack DS
'''


queue = []

queue.append('g')
queue.append('f')
queue.append('g')

print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)



'''

Priority Queue:  Queue with an importance of value i.e. 
                one is a higher priority then the other that exits first


                If 2 elements have the same priority level, then they are dequeued based on their order of entrance. 
'''

class PriorityQ(object):

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def empty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)

    def delete(self):

        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
    
            del self.queue[max]
            return item
        
        except IndexError as e:
            print("Check error: " + e)
            exit()

if __name__ == "__main__":
    myQueue = PriorityQ()
    myQueue.insert(10)
    myQueue.insert(0)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)   

    while not myQueue.empty():
        print(myQueue.delete())
        