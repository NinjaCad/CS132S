import random

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

def radix_sort(nums):
    print("Radix Pass 0:", *nums)

    maxDigits = len(str(max(nums)))
    place = 1

    for i in range(maxDigits):
        Q0 = Queue()
        Q1 = Queue()
        Q2 = Queue()
        Q3 = Queue()
        Q4 = Queue()
        Q5 = Queue()
        Q6 = Queue()
        Q7 = Queue()
        Q8 = Queue()
        Q9 = Queue()

        queues = [Q0, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]

        for num in nums:
            digit = (num // place) % 10
            queues[digit].enqueue(num)

        nums.clear()
        for q in queues:
            while not q.is_empty():
                nums.append(q.dequeue())

        place *= 10

        print("Radix Pass " + str(i+1) + ":", *nums)
        
    return True

def main():
    max_range = int(input("Enter max range: "))
    size = int(input("Enter list size: "))

    ranList = []
    for i in range(size):
        ranList.append(random.randint(0, max_range))

    radix_sort(ranList)

if __name__ == "__main__":
    main()