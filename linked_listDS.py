class Node:


    def __init__(self , data):
        self.data = data
        self.next= None



node1= Node(20)

node3= Node(40)
node4= Node(50)
node2= Node(30)
node5= Node(60)

node1.next= node2
node3.next= node4
node4.next= node2
node2.next= node5


head = node4



current = head

while current:
    print(current.data , end='<-')
    current = current.next
