"""
    Deliverable: Homework07.py


    References:

        https://runestone.academy/runestone/books/published/pythonds3/Trees/toctree.htmlLinks to an external site.
        (Sections 6.1-6.11)
        https://en.wikipedia.org/wiki/Double-ended_priority_queue#OperationsLinks to an external site.
        https://en.wikipedia.org/wiki/Min-max_heapLinks to an external site.


    Sample Input/Output:

        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework07.py 
        ******************************
        Printing main() source code:
        ******************************
        def main():
            import inspect
            import random

            print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
            print(str(inspect.getsource(main)))
            print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

            print("This program implements a double-ended priority queue class using a min-max heap.")
            max_range = int(input("Enter max range: "))
            list_size = int(input("Enter list size: "))

            my_list = [random.randrange(1, max_range+1, 1) for i in range(list_size)]
            print("Original List:", my_list)

            my_depq = DEPQ(my_list)
            print("DEPQ min-max heap:", my_depq)

            print("size() = ", my_depq.size())
            print("is_empty() = ", my_depq.is_empty())
            print("remove_min() = ", my_depq.remove_min())
            print("DEPQ min-max heap:", my_depq)
            print("remove_max() = ", my_depq.remove_max())
            print("DEPQ min-max heap:", my_depq)
            print("remove_min() = ", my_depq.remove_min())
            print("DEPQ min-max heap:", my_depq)
            print("remove_max() = ", my_depq.remove_max())
            print("DEPQ min-max heap:", my_depq)
            print("put(max_range) = ", my_depq.put(max_range))
            print("DEPQ min-max heap:", my_depq)
            print("get_min() = ", my_depq.get_min())
            print("get_max() = ", my_depq.get_max())
            print("DEPQ min-max heap:", my_depq)

        ******************************
        Printing main() source output:
        ******************************
        This program implements a double-ended priority queue class using a min-max heap.
        Enter max range: 100
        Enter list size: 10
        Original List: [93, 62, 82, 36, 4, 96, 54, 68, 97, 53]
        DEPQ min-max heap: [4, 97, 96, 36, 53, 82, 54, 68, 62, 93]
        size() =  10
        is_empty() =  False
        remove_min() =  4
        DEPQ min-max heap: [36, 97, 96, 62, 53, 82, 54, 68, 93]
        remove_max() =  97
        DEPQ min-max heap: [36, 93, 96, 62, 53, 82, 54, 68]
        remove_min() =  36
        DEPQ min-max heap: [53, 93, 96, 62, 68, 82, 54]
        remove_max() =  96
        DEPQ min-max heap: [53, 93, 82, 62, 68, 54]
        put(max_range) =  100
        DEPQ min-max heap: [53, 93, 100, 62, 68, 54, 82]
        get_min() =  53
        get_max() =  100
        DEPQ min-max heap: [53, 93, 100, 62, 68, 54, 82]
        >>> 


    To Do:

        1. Read all about Trees and Tree Algorithms in Chapter 6.1-6.10
        2. Read about Double-Ended Priority Queues and Min-Max Heaps via the provided Wikipedia links
        3. Implement a Min-Max Heap class
        4. Implement a Double-Ended Priority Queue class using a Min-Max Heap
        5. Copy my main() method from the sample output to test your code
        6. Start early, work diligently, and ask me if you have any questions
        7. Submit the completed code via Canvas
    

    100	CS132S Rubric HW07:
        2.5	class Binary_Min_Max_Heap:
        2.5	    def __init__(self, alist):
        2.5	    def is_min_level(self, i):
        2.5	    def grandparent(self, i):
        2.5	    def parent(self, i):
        2.5	    def left_child(self, i):
        2.5	    def has_children(self, i):
        2.5	    def has_grandparent(self, i):
        2.5	    def index_smallest_child_or_grandchild(self, i):
        2.5	    def index_largest_child_or_grandchild(self, i):
        2.5	    def push_down_min(self, m):
        2.5	    def push_down_max(self, m):
        2.5	    def push_down(self, i):
        2.5	    def push_up_min(self, i):
        2.5	    def push_up_max(self, i):
        2.5	    def push_up(self, i):
        2.5	    def insert(self, i):
        2.5	    def find_min(self):
        2.5	    def find_max(self):
        2.5	    def remove_min(self):
        2.5	    def remove_max(self):
        2.5	    def build_binary_min_max_heap(self,alist):
        2.5	class DEPQ:
        2.5	    def __init__(self, alist):
        2.5	    def is_empty(self):
        2.5	    def size(self):
        2.5	    def get_min(self):
        2.5	    def get_max(self):
        2.5	    def put(self, i):
        2.5	    def remove_min(self):
        2.5	    def remove_max(self):
        2.5	def main():
        5	Readability
        15	Quality of Solution
"""

class Binary_Min_Max_Heap:
    def __init__(self, alist):
        self._heap = []
        if alist:
            self.build_binary_min_max_heap(alist)

    def is_min_level(self, i):
        level = 0
        index = i + 1
        while index > 1:
            index = index // 2
            level += 1
        return level % 2 == 0

    def grandparent(self, i):
        parent = self.parent(i)
        return None if parent is None else self.parent(parent)

    def parent(self, i):
        return None if i == 0 else (i - 1) // 2

    def left_child(self, i):
        child = 2 * i + 1
        return None if child >= len(self._heap) else child
    
    def right_child(self, i):
        child = 2 * i + 2
        return None if child >= len(self._heap) else child

    def has_children(self, i):
        return self.left_child(i) is not None

    def has_grandparent(self, i):
        return self.grandparent(i) is not None

    def index_smallest_child_or_grandchild(self, i):
        canidates = []
        left = self.left_child(i)
        right = self.right_child(i)

        if left is not None:
            canidates.append(left)
        if right is not None:
            canidates.append(right)

        for child in [left, right]:
            if child is not None:
                ll = self.left_child(child)
                lr = self.right_child(child)
                if ll is not None:
                    canidates.append(ll)
                if lr is not None:
                    canidates.append(lr)

        if not canidates:
            return None
        smallestIndex = canidates[0]
        for candidate in canidates:
            if self._heap[candidate] < self._heap[smallestIndex]:
                smallestIndex = candidate
        return smallestIndex
    
    def index_largest_child_or_grandchild(self, i):
        canidates = []
        left = self.left_child(i)
        right = self.right_child(i)

        if left is not None:
            canidates.append(left)
        if right is not None:
            canidates.append(right)

        for child in [left, right]:
            if child is not None:
                grandLeft = self.left_child(child)
                grandRight = self.right_child(child)
                if grandLeft is not None:
                    canidates.append(grandLeft)
                if grandRight is not None:
                    canidates.append(grandRight)

        if not canidates:
            return None
        largestIndex = canidates[0]
        for canidate in canidates:
            if self._heap[canidate] > self._heap[largestIndex]:
                largestIndex = canidate
        return largestIndex
    
    def _is_grandchild(self, i, m):
        return m >= 4 * i + 3
    
    def push_down_min(self, i):
        if self.has_children(i):
            m = self.index_smallest_child_or_grandchild(i)
            if m is not None and self._heap[m] < self._heap[i]:
                self._heap[m], self._heap[i] = self._heap[i], self._heap[m]
                if self._is_grandchild(i, m):
                    p = self.parent(m)
                    if p is not None and self._heap[m] > self._heap[p]:
                        self._heap[m], self._heap[p] = self._heap[p], self._heap[m]
                    self.push_down(m)
 
    def push_down_max(self, i):
        if self.has_children(i):
            m = self.index_largest_child_or_grandchild(i)
            if m is not None and self._heap[m] > self._heap[i]:
                self._heap[i], self._heap[m] = self._heap[m], self._heap[i]
                if self._is_grandchild(i, m):
                    p = self.parent(m)
                    if p is not None and self._heap[m] < self._heap[p]:
                        self._heap[m], self._heap[p] = self._heap[p], self._heap[m]
                    self.push_down(m)

    def push_down(self, i):
        if self.is_min_level(i):
            self.push_down_min(i)
        else:
            self.push_down_max(i)

    def push_up_min(self, i):
        if self.has_grandparent(i) and self._heap[i] < self._heap[self.grandparent(i)]:
            gp = self.grandparent(i)
            self._heap[i], self._heap[gp] = self._heap[gp], self._heap[i]
            self.push_up_min(gp)

    def push_up_max(self, i):
        if self.has_grandparent(i) and self._heap[i] > self._heap[self.grandparent(i)]:
            gp = self.grandparent(i)
            self._heap[i], self._heap[gp] = self._heap[gp], self._heap[i]
            self.push_up_max(gp)

    def push_up(self, i):
        p = self.parent(i)
        if p is None:
            return
        if self.is_min_level(i):
            if self._heap[i] > self._heap[p]:
                self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
                self.push_up_max(p)
            else:
                self.push_up_min(i)
        else:
            if self._heap[i] < self._heap[p]:
                self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
                self.push_up_min(p)
            else:
                self.push_up_max(i)

    def insert(self, i):
        self._heap.append(i)
        self.push_up(len(self._heap) - 1)

    def find_min(self):
        if not self._heap:
            return None
        return self._heap[0]
    
    def find_max(self):
        if not self._heap:
            return None
        elif len(self._heap) == 1:
            return self._heap[0]
        elif len(self._heap) == 2:
            return self._heap[1]
        else:
            return max(self._heap[1], self._heap[2])

    def remove_min(self):
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()

        minVal = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.push_down(0)
        return minVal

    def remove_max(self):
        if not self._heap:
            return None
        if len(self._heap) == 1 or len(self._heap) == 2:
            return self._heap.pop()

        max_index = 1 if self._heap[1] > self._heap[2] else 2
        max_val = self._heap[max_index]
        self._heap[max_index] = self._heap.pop()
        self.push_down(max_index)
        return max_val
    
    def build_binary_min_max_heap(self, alist):
        self._heap = alist[:]
        for i in reversed(range(len(self._heap)//2)):
            self.push_down(i)
    
    def __str__(self):
        return str(self._heap)

class DEPQ:
    def __init__(self, alist):
        self.mm_heap = Binary_Min_Max_Heap(alist)

    def is_empty(self):
        if len(self.mm_heap._heap) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.mm_heap._heap)

    def get_min(self):
        return self.mm_heap.find_min()
    
    def get_max(self):
        return self.mm_heap.find_max()
    
    def put(self, i):
        self.mm_heap.insert(i)
        return i

    def remove_min(self):
        return self.mm_heap.remove_min()
    
    def remove_max(self):
        return self.mm_heap.remove_max()
    
    def __str__(self):
        return str(self.mm_heap._heap)

def main():
    import inspect
    import random

    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

    print("This program implements a double-ended priority queue class using a min-max heap.")
    max_range = int(input("Enter max range: "))
    list_size = int(input("Enter list size: "))

    my_list = [random.randrange(1, max_range+1, 1) for i in range(list_size)]
    print("Original List:", my_list)

    my_depq = DEPQ(my_list)
    print("DEPQ min-max heap:", my_depq)

    print("size() = ", my_depq.size())
    print("is_empty() = ", my_depq.is_empty())
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("put(max_range) = ", my_depq.put(max_range))
    print("DEPQ min-max heap:", my_depq)
    print("get_min() = ", my_depq.get_min())
    print("get_max() = ", my_depq.get_max())
    print("DEPQ min-max heap:", my_depq)

if __name__ == "__main__":
    main()