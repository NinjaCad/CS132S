"""
    Deliverable: Homework03.py


    References:

        https://runestone.academy/runestone/books/published/pythonds3/BasicDS/toctree.htmlLinks to an external site.
        (Sections 3.10-3.14, Section 3.27: Programming Exercise #9)


    Sample Input/Output:

        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework03.py 
        Enter max range: 99999
        Enter list size: 10

        Radix Pass 0: 26986 93976 42096 38500  5119 89437 74564 17357  4735 66223 
        Radix Pass 1: 38500 66223 74564  4735 26986 93976 42096 89437 17357  5119 
        Radix Pass 2: 38500  5119 66223  4735 89437 17357 74564 93976 26986 42096 
        Radix Pass 3: 42096  5119 66223 17357 89437 38500 74564  4735 93976 26986 
        Radix Pass 4: 42096 93976 74564  4735  5119 66223 26986 17357 38500 89437 
        Radix Pass 5:  4735  5119 17357 26986 38500 42096 66223 74564 89437 93976 
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework03.py 
        Enter max range: 9999999999
        Enter list size: 6

        Radix Pass  0:  708339229 5558806485 6709687841 1979780173 5368163781 8060403289 
        Radix Pass  1: 6709687841 5368163781 1979780173 5558806485  708339229 8060403289 
        Radix Pass  2:  708339229 6709687841 1979780173 5368163781 5558806485 8060403289 
        Radix Pass  3: 1979780173  708339229 8060403289 5558806485 5368163781 6709687841 
        Radix Pass  4: 1979780173 8060403289 5368163781 5558806485 6709687841  708339229 
        Radix Pass  5: 8060403289 5558806485  708339229 5368163781 1979780173 6709687841 
        Radix Pass  6: 5368163781  708339229 8060403289 6709687841 1979780173 5558806485 
        Radix Pass  7: 8060403289 5368163781  708339229 5558806485 6709687841 1979780173 
        Radix Pass  8:  708339229 6709687841 5558806485 8060403289 5368163781 1979780173 
        Radix Pass  9: 8060403289 5368163781 5558806485  708339229 6709687841 1979780173 
        Radix Pass 10:  708339229 1979780173 5368163781 5558806485 6709687841 8060403289 
        >>> 
        

        Note: If you manage to align the columns of numbers in exactly the manner above, regardless of the number of digits in each number, that is worth a little bit of extra credit. :)


    100	CS132S Rubric HW03:
        8	Initial I/O
        8	Random Number Generation
        8	Main Queue + 1 Queue/Digit
        8	List of Digit Queues
        8	Radix Passes Right-to-Left
        8	Radix Passes One Per Digit
        8	Radix Stable Sort
        8	Radix Small Numbers OK
        8	Print Each Iteration
        8	Readability
        20	Quality of Solution
        5	Extra Credit: Column Spacing
"""

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