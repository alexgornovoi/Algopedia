class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.is_empty():
            return None
        
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0