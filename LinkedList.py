# Singly Linked List using single class Node

class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None

    def isempty(self):
        return self.value is None

    # Recursive append
    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next is None:
            self.next = Node(v)
        else:
            self.next.append(v)

    # Iterative append
    def appendi(self, v):
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next is not None:
            temp = temp.next 
        temp.next = Node(v)

    def insert(self, v):
        if self.isempty():
            self.value = v
            return
        newNode = Node(v)
        self.value, newNode.value = newNode.value, self.value
        self.next, newNode.next = newNode, self.next

    def delete(self, v):
        if self.isempty():
            return
        elif self.value == v:
            self.value = None
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next is not None:
                self.next.delete(v)
                if self.next.value is None:
                    self.next = None

    def display(self):
        if self.isempty():
            print('None')
        else:
            temp = self
            while temp is not None:
                print(str(temp.value), end=" ")
                temp = temp.next
            print()  


if __name__ == "__main__":
    head = Node(None)
    head.insert(50)
    head.append(20)
    head.append(30)
    head.appendi(40)
    head.appendi(50)
    head.insert(10)
    head.delete(90)
    head.display()
