class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self, value) -> None:
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_values(self) -> None:

        print(f"self.length = {self.length}")
        
        ptr = self.head

        if ptr is None:
            return

        while True:
            print(ptr.value)

            if ptr.next is None:
                break

            ptr = ptr.next

    def append(self , value):
        new_node = Node(value)

        if self.head is None:
            # If LinkedList is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def __find_one_before_the_last_node(self)->Node:
        
        before_iteration = None
        current_iteration = self.head

        while True:
            if current_iteration.next is None:
                break
            
            before_iteration = current_iteration
            current_iteration = current_iteration.next         

        return before_iteration

    def pop(self):
        if self.length == 0:
            raise Exception("There is no item to pop")
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        one_before_the_last_node = self.__find_one_before_the_last_node()
        one_before_the_last_node.next = None
        self.tail = one_before_the_last_node

        self.length -= 1

    def prepend(self, value):
        """ Add to the beginning of the LinkedList"""

        # TODO : Complete me .......

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length +=1
        
    def pop_first(self):
        
        if self.length == 0:
            raise Exception("There is no item to pop")
        elif self.length == 1:
            self.head.next = None
            self.head = None
        else:
            second_element = self.head.next
            self.head.next = None
            self.head = second_element

        self.length -=1

    def __validate_index(self, index) -> None:
        if self.length < 0 or index > self.length - 1 :
            raise IndexError("Index is out of range")

    def __get_node_by_index(self, index: int) -> Node:
        self.__validate_index(index=index)
        
        current_one = self.head

        for _ in range(index):
            current_one = current_one.next

        return current_one

    def get(self, index):
        """ Indexes start from 0 """

        node : Node = self.__get_node_by_index(index=index)

        return node.value
    
    def set_value(self, index, value):

        node : Node = self.__get_node_by_index(index=index)

        node.value = value
 

my_linked_list = LinkedList(4)

print("Appending some items ...")
my_linked_list.append(10)
my_linked_list.append(8)
my_linked_list.append(3)
my_linked_list.append(2)


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


my_linked_list.print_values()

print("Popping The last item ...")
my_linked_list.pop()                                                                                     

my_linked_list.print_values()

print("Prepending The item ...")
my_linked_list.prepend(7)
my_linked_list.print_values()

print("Popping The First item ...")
my_linked_list.pop_first()
my_linked_list.print_values()

print("getting only the item With Index = `2`")
print(my_linked_list.get(2))

print("`set_value` The item ...")
my_linked_list.set_value(index=0, value=99)
my_linked_list.print_values()