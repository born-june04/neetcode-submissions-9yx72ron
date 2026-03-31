class MinStack:

    def __init__(self): 
        # initialize the stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # push val into the stack
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # remove the element top of the stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # gets the top element
        return self.stack[-1]

    def getMin(self) -> int:
        # retrieves the minimum element
        return self.min_stack[-1]
