class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack)-1)
        

    def pop(self) -> None:
        if not self.stack:
            return
        
        stack_index = len(self.stack)-1
        if stack_index <= self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return 
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return 
        # print('self.min_stack[-1]: ', self.min_stack[-1])
        # print('self.stack: ', self.stack)
        return self.stack[self.min_stack[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()