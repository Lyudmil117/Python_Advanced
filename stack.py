class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return f"{self.data.pop()}"

    def top(self):
        return f"{self.data[-1]}"

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data)-1, -1, -1)]) + "]"


