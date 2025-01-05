class Stack:
    def __init__(self):
        self.items = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Add an item to the stack
    def push(self, item):
        self.items.append(item)

    # Remove an item from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Peek at the top item of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Get the size of the stack
    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())    # Output: 30
print("Popped element:", stack.pop())  # Output: 30
print("Is stack empty?", stack.is_empty())  # Output: False
print("Stack size:", stack.size())     # Output: 2