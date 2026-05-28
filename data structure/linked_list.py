import node

class Linkedlist():

    __slots__ = ["size", "tail", "head"]

    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def add(self, value):
        new_node = node.Node(value)
        
        if self.size == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.set_next(new_node)
            next_node = self.head.get_next()
            self.head = next_node

        self.size += 1

    def delete(self, value):

        if self.size == 0:
            return 

        if self.tail.get_value() == value:
            self.tail = self.tail.get_next()
            self.size -= 1

            if self.size == 0:
                self.head = None


        prev = self.tail
        curr = self.tail.get_next()

        while curr is not None:

            if curr.get_value() == value:

                prev.set_next(curr.get_next())

                if curr == self.head:
                    self.head = prev

                self.size -= 1
                return

            prev = curr
            curr = curr.get_next()

    def get(self, index):
        temp = self.tail

        for _ in range(index):
            temp = temp.get_next()
        
        return temp.get_value()
        

    def insert(self, value, index):

        new_node = node.Node(value)

        if index == 0:
            temp = self.tail
            self.tail = new_node
            self.tail.set_next(temp)

        prev = self.tail
        for _ in range(index):
            prev = prev.get_next()

        next_node = prev.get_next()
        prev.set_next(new_node)
        prev.get_next().set_next(next_node)

        self.size += 1

    def find(self, value):

        temp = self.tail
        index = 0

        for _ in range(self.size):
            if temp.get_value() == value:
                return index
            temp = temp.get_next()
            index += 1
        
        return None



    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail

    def __str__(self):
        s = "["
        copy_tail = self.tail
        for i in range(0, self.size):
            s += str(copy_tail.get_value())
            if i != self.size - 1:
                s += ", "
            copy_tail = copy_tail.get_next()

        s += "]"

        return s
    
    def __len__(self):
        return self.size
                

def main():
    linkedL = Linkedlist()
    linkedL.add(4)
    linkedL.add(5)
    linkedL.add(6)
    linkedL.add(10)
    linkedL.add(234)
    linkedL.add(347)
    linkedL.delete(10)
    # print(linkedL.get(0))
    # print(linkedL.get(4))
    linkedL.insert(23, 2)
    linkedL.insert(5992, len(linkedL)-1)
    linkedL.insert(-2343, 0)
    print(linkedL.find(89))
    print(linkedL.find(6))
    print(linkedL)

if __name__ == "__main__":
    main()