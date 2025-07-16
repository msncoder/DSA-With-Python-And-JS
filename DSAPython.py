
#Dynamic Array

import ctypes

class MeraList():
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '['+result[:-1]+']'
    
    def __getItem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        self.A[self.n] = item
        self.n = self.n+1

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'Value Error - not in list'

    def __resize(self,new_capcity):
        #create a new array with new capacity
        B = self.__make_array(new_capcity)
        self.size = new_capcity
        #copy the content A to B
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign A
        self.A = B

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()


L = MeraList()
print(type(L))
L.append("hhel")
L.append(1)
L.append(True)

print(len(L))
print(L)
L.pop()
L.pop()
L.find(20)
L.find("hhel")
L.clear()
print(type(L))
print(L)