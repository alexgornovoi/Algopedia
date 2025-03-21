class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, val):
        self.queue.append(val)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        return None
            
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(Queue)
    
    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]
        return None
    
    def clear(self):
        self.queue = []
    
    def contains(self, val):
        for i in self.queue:
            if i == val:
                return True
        return False