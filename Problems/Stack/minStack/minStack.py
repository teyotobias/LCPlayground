class minStack:
    def __init__(self):
        #initialize stack
        self.stack = []
    

    def push(self,val):
        if not self.stack:
            min = val
        else:
            min = self.getMin()
        if val < min:
            min = val
        self.stack.append([val, min])
    

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]
    

    def getMin(self):
        return self.stack[-1][1]
