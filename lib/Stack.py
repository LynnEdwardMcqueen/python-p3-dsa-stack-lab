class Stack:
    def __init__(self, items = [], stack_size = None):
        self.stack_size = stack_size
        self.items = list(items)



    def push(self, pushable_item):
        if (self.stack_size == None or len(self.items) <  self.stack_size):
            self.items.append(pushable_item)
        else:
            # raise MemoryError("Maximum Stack Size Achieved")
            print("Maximum")
        print("Exiting push")
    
    def pop(self):
        if (self.isEmpty() == True):
            return None
        else:
            return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        current_stack_size = len(self.items)
        if current_stack_size == 0:
            return True
        return False
        
    def full(self):
        current_stack_size = len(self.items)
        if current_stack_size == self.stack_size:
            return True
        return False
    
    def size(self):
        return len(self.items)

    def search(self, value):
        if (value in self.items):
            return_value = self.items.index(value) 
            return_value = len(self.items) - return_value - 1
        else:
            return_value = -1
        return return_value
    
stk = Stack([])
print(stk.pop())
# test_stack = Stack(5)

# print (test_stack.__dict__)
# for i in range(6):
#    print("Pushing item ", i)
#    try:
#        test_stack.push(i)
#    except:
#        print("No luck with the push")  
#    
#    print("peek = ", test_stack.peek())
#    print("Size = ", test_stack.size())
#    print("search returns ", test_stack.search(2))
#    print("full returns ", test_stack.full())
#    print("empty returns ", test_stack.isEmpty())
#    print("")





