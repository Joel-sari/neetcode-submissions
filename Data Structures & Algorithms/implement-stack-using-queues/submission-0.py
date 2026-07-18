class MyStack: 
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        # For queues we use .append() instead of saying push
        self.queue.append(x)
    def pop(self) -> int:

        # We pretty much popleft everything until the very last one
        for i in range(len(self.queue)- 1):
            self.push(self.queue.popleft())
        # We still have to pop / delete the last one but we need to RETURN it whcih is why we do it differently!
        return self.queue.popleft()
    
    def top(self) -> int:
        return self.queue[-1]
    def empty(self)-> bool:
        return len(self.queue) == 0






# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()