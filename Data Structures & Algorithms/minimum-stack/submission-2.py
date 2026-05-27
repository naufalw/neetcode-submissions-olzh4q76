class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.currmin = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.currmin:
            self.currmin = val
        self.minstack.append(self.currmin)
        
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        if not self.minstack:
            self.currmin = float('inf')
        else:
            self.currmin = self.minstack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
