"""
    Deliverable: Homework06.py
 

    References:

        https://runestone.academy/runestone/books/published/pythonds3/SortSearch/toctree.htmlLinks to an external site.
    

    Sample Output:

        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework06.py 
        Number of list comparisons and assignments for Chapter 5 sorting algorithms on identical random lists of N elements
        (NOTE: use of temp variables in swaps replaced by simultaneous assignment)

            N     Bubble Sort        Selection Sort      Insertion Sort        Shell Sort          Merge Sort          Quick Sort    
            (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns)
        10 (      45,      54) (      45,      18) (      27,      45) (      15,      59) (      25,      68) (      22,      10) 
        100 (    4950,    4890) (    4950,     198) (    2445,    2643) (     449,    1455) (     545,    1344) (     598,     275) 
        1000 (  499500,  500924) (  499500,    1998) (  250462,  252460) (    7756,   23768) (    8700,   19952) (   11461,    4058) 
        10000 (49995000,50340250) (49995000,   19998) (25170125,25190123) (  150655,  390665) (  120379,  267232) (  146618,   57021) 
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework06.py 
        Number of list comparisons and assignments for Chapter 5 sorting algorithms on identical random lists of N elements
        (NOTE: use of temp variables in swaps replaced by simultaneous assignment)

            N     Bubble Sort        Selection Sort      Insertion Sort        Shell Sort          Merge Sort          Quick Sort    
            (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns)
        10 (      45,      56) (      45,      18) (      28,      46) (      14,      58) (      22,      68) (      27,      10) 
        100 (    4950,    4734) (    4950,     198) (    2367,    2565) (     401,    1407) (     541,    1344) (     607,     264) 
        1000 (  499500,  517940) (  499500,    1998) (  258970,  260968) (    7354,   23366) (    8713,   19952) (    9889,    4191) 
        10000 (49995000,50379298) (49995000,   19998) (25189649,25209647) (  151729,  391739) (  120486,  267232) (  162675,   55889) 
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework06.py 
        Number of list comparisons and assignments for Chapter 5 sorting algorithms on identical random lists of N elements
        (NOTE: use of temp variables in swaps replaced by simultaneous assignment)

            N     Bubble Sort        Selection Sort      Insertion Sort        Shell Sort          Merge Sort          Quick Sort    
            (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns)
        10 (      45,      42) (      45,      18) (      21,      39) (      15,      59) (      22,      68) (      21,      14) 
        100 (    4950,    4226) (    4950,     198) (    2113,    2311) (     451,    1457) (     541,    1344) (     635,     239) 
        1000 (  499500,  497704) (  499500,    1998) (  248852,  250850) (    7304,   23316) (    8705,   19952) (   11211,    4044) 
        10000 (49995000,49981564) (49995000,   19998) (24990782,25010780) (  148918,  388928) (  120491,  267232) (  152763,   56617) 
        >>> 
    

    To Do:

        1. Read all about Sorting and Searching in Chapter 5
        2. Copy the code from the various sorting algorithms listed in the sample output
        3. Modify the code to replace all swaps via temp variable with swaps via simultaneous assignment
        4. Modify the code by adding counters for each key comparison and key assignment (swaps count as two key assignments)
        5. Create code to create a randomly generated list of length 10 (using identical copies of that list for each sorting algorithm), and print the resulting counter values as in the sample output
        6. Do the same for randomly generated lists of length 100, 1000, and 10000
        7. Start early, work diligently, and ask me if you have any questions
        8. Submit the completed code via Canvas
    

    100	CS132S Rubric HW06:
        10	Output "Table" Compares/Assigns
        10	Bubble Sort Implementation
        10	Selection Sort Implementation
        10	Insertion Sort Implementation
        10	Shell Sort Implementation
        10	Merge Sort Implementation
        10	Quick Sort Implementation
        10	Readability
        20	Quality of Solution
"""

import random

print("Number of list comparisons and assignments for Chapter 5 sorting algorithms on identical random lists of N elements:")
print("(NOTE: use of temp variables in swaps replaced by simultaneous assignment")


# Bubble Sort
def bubble_sort(a_list):
    compares, assigns = 0, 0

    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            compares += 1
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                assigns += 2

    return compares, assigns


# Selection Sort
def selection_sort(a_list):
    compares, assigns = 0, 0

    for i in range(len(a_list)):
        mx_idx = 0
        for j in range(len(a_list) - i):
            compares += 1
            if a_list[j] > a_list[mx_idx]:
                mx_idx = j
        if mx_idx != len(a_list) - i - 1:
            a_list[mx_idx], a_list[len(a_list) - i - 1] = a_list[len(a_list) - i - 1], a_list[mx_idx]
            assigns += 2

    return compares, assigns


# Insertion Sort
def insertion_sort(a_list):
    compares, assigns = 0, 0

    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            compares += 1
            a_list[cur_pos] = a_list[cur_pos - 1]
            assigns += 1
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val
        assigns += 1

    return compares, assigns


# Shell Sort
def shell_sort(a_list):
    compares, assigns = 0, 0

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            c, a = gap_insertion_sort(a_list, pos_start, sublist_count)
            compares += c
            assigns += a

        sublist_count = sublist_count // 2

    return compares, assigns

def gap_insertion_sort(a_list, start, gap):
    compares, assigns = 0, 0

    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            compares += 1
            a_list[cur_pos] = a_list[cur_pos - gap]
            assigns += 1
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val
        assigns += 1

    return compares, assigns


# Merge Sort
def merge_sort(a_list):
    compares, assigns = 0, 0

    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        c, a = merge_sort(left_half)
        compares += c
        assigns += a

        c, a = merge_sort(right_half)
        compares += c
        assigns += a

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            compares += 1
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                assigns += 1
                i = i + 1
            else:
                a_list[k] = right_half[j]
                assigns += 1
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            assigns += 1
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            assigns += 1
            j = j + 1
            k = k + 1

    return compares, assigns


# Quick Sort
def quick_sort(a_list):
    compares, assigns = quick_sort_helper(a_list, 0, len(a_list) - 1)
    return compares, assigns

def quick_sort_helper(a_list, first, last):
    compares, assigns = 0, 0

    if first < last:
        split, c, a = partition(a_list, first, last)
        compares += c
        assigns += a

        c, a = quick_sort_helper(a_list, first, split - 1)
        compares += c
        assigns += a

        c, a = quick_sort_helper(a_list, split + 1, last)
        compares += c
        assigns += a
    
    return compares, assigns

def partition(a_list, first, last):
    compares, assigns = 0, 0

    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            compares += 1
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            compares += 1
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
            assigns += 2
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    assigns += 2

    return right_mark, compares, assigns

def main():
    print("    N     Bubble Sort        Selection Sort      Insertion Sort        Shell Sort          Merge Sort          Quick Sort    ")
    print("      (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns) (compares, assigns)")

    # random lists of 10, 100, 1000, and 10000 elements
    n10 = [random.randint(0, 100) for _ in range(10)]
    n100 = [random.randint(0, 100) for _ in range(100)]
    n1000 = [random.randint(0, 100) for _ in range(1000)]
    n10000 = [random.randint(0, 100) for _ in range(10000)]

    for n, arr in [(10, n10), (100, n100), (1000, n1000), (10000, n10000)]:
        bc, ba = bubble_sort(arr[:])
        sc, sa = selection_sort(arr[:])
        ic, ia = insertion_sort(arr[:])
        shc, sha = shell_sort(arr[:])
        mc, ma = merge_sort(arr[:])
        qc, qa = quick_sort(arr[:])

        output = f"{n:>5} "
        output += f"({bc:>8}, {ba:>8})".ljust(18)
        output += f"({sc:>8}, {sa:>8})".ljust(20)
        output += f"({ic:>8}, {ia:>8})".ljust(20)
        output += f"({shc:>8}, {sha:>8})".ljust(20)
        output += f"({mc:>8}, {ma:>8})".ljust(20)
        output += f"({qc:>8}, {qa:>8})".ljust(20)

    print(output)

if __name__ == "__main__":
    main()