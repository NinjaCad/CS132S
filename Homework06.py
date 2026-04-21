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