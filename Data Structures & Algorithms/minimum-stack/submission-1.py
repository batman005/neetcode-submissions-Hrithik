class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:  # O(1) TC , O(1) SC
        self.stack.append(val)
        

    def pop(self) -> None:  # O(1) TC , O(1) SC
        self.stack.pop()

    def top(self) -> int:  # O(1) TC , O(1) SC
        return self.stack[-1]

    def getMin(self) -> int:  # O(N) TC , O(N) SC
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
