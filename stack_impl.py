class Stack(list):
    def push(self, value):
        self.append(value)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self) == 0

# Test program
def main():
    stack = Stack()

    print("Enter five strings:")
    for i in range(5):
        string = input()
        stack.push(string)

    print("Strings in reverse order:")
    while not stack.is_empty():
        print(stack.pop())

if __name__ == "__main__":
    main()
