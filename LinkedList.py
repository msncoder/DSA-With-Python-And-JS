class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3) 

# a.next = b
# print(a)
# print(c.next)


class LinkedList:
    def __init__(self):

        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    #Insert from HEAD

    def insert_head(self,value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self.n = self.n+1  

    # Traverseal operation 

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            # print(curr.data)
            result = result + str(curr.data) + '->'
            curr = curr.next
        
        return result[:-2]
            
    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1

        else: 
            curr = self.head

            while curr.next != None:
                curr = curr.next
            
            curr.next = new_node
            self.n = self.n + 1


    def insert_after(self,after,value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node

        else:
            return 'Item not Found'

L = LinkedList()
# print(len(L))

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(3)
# L.append(8)
# L.append(8)
L.insert_after(1,90)
# print(len(L))
print(L)

