class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)


def main():
    prefix = input("Enter Prefix Expression: ").split()
    print(prefix[::-1])
    postfix = Stack()
    for token in prefix[::-1]:
        if token in "+-*/":
            one = postfix.pop()
            two = postfix.pop()
            postfix.push(one + " " + two + " " + token)
        else:
            postfix.push(token)
    print("Converted to Postfix is:", postfix.peek())

if __name__ == "__main__":
    main()