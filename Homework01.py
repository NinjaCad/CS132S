"""
    Deliverable: Homework01.py
    

    References:

        https://runestone.academy/runestone/books/published/pythonds3/Introduction/toctree.htmlLinks to an external site.
        https://runestone.academy/runestone/books/published/pythonds3/AlgorithmAnalysis/toctree.htmlLinks to an external site.


    Sample Input/Output:

        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework01.py 

        This program finds the smallest difference between any two elements in a
        randomly generated list of integers, using two different algorithms with 
        different Big-O efficiency.

        Enter random min range: 1
        Enter random max range: 1000000
        Enter length of list: 10

        Smallest difference: 7505
        List: [91074, 722243, 691463, 162983, 152492, 83569, 391027, 870040, 215036, 23326]
        List length: 10
        Algorithm 1 Time: 2.098083e-05
        Algorithm 2 Time: 5.960464e-06
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework01.py 

        This program finds the smallest difference between any two elements in a
        randomly generated list of integers, using two different algorithms with 
        different Big-O efficiency.

        Enter random min range: 1
        Enter random max range: 1000000
        Enter length of list: 100

        Smallest difference: 144
        List: [908290, 670214, 908817, 897559, 668697, 647719, 899112, 829998, 429621, 220217, 326714, 959549, 693310, 975424, 973376, 701504, 887363, 406603, 264269, 130135, 154715, 815707, 793189, 919654, 807032, 901761, 638601, 815244, 612497, 823443, 566940, 771229, 683677, 960159, 429216, 387256, 160952, 971453, 176323, 983238, 166602, 103120, 663249, 192725, 136408, 61658, 422140, 958717, 626948, 879881, 42249, 891667, 928023, 99613, 739623, 725804, 151860, 965434, 453947, 902460, 424253, 481601, 128834, 897871, 323414, 621917, 489824, 331105, 324960, 203117, 376691, 784245, 310137, 769916, 803201, 420231, 766343, 653194, 870286, 716693, 594839, 696731, 63906, 891811, 24997, 389542, 48047, 691125, 904118, 318901, 455096, 696255, 945092, 257998, 414170, 535009, 890356, 317429, 732662, 332791]
        List length: 100
        Algorithm 1 Time: 1.234055e-03
        Algorithm 2 Time: 2.932549e-05
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework01.py 

        This program finds the smallest difference between any two elements in a
        randomly generated list of integers, using two different algorithms with 
        different Big-O efficiency.

        Enter random min range: 1
        Enter random max range: 1000000
        Enter length of list: 1000

        Smallest difference: 1
        Squeezed text (87 lines). 
        List length: 1000 
        Algorithm 1 Time: 9.741092e-02 
        Algorithm 2 Time: 2.269745e-04 
        >>> RESTART: /Users/jeickemeyer/TMU/Courses/CIS112/_key/Homework01.py 
        This program finds the smallest difference between any two elements in a 
        randomly generated list of integers, using two different algorithms with 
        different Big-O efficiency. 

        Enter random min range: 1 
        Enter random max range: 1000000 E
        nter length of list: 10000 
        Smallest difference: 1 
        Squeezed text (868 lines). 
        List length: 10000 
        Algorithm 1 Time: 8.537766e+00 
        Algorithm 2 Time: 2.315998e-03 
        >>>


    100	CS132S Rubric HW01:
        5	Initial I/O
        15	Algorithm 1 Implementation
        15	Algorithm 2 Implementation
        15	Different Big-O Efficiencies
        15	Time Two Algorithms
        5	Final Output
        10	Readability
        20	Quality of Solution
"""

import time
import random

def randomListGenerator(min, max, length):
    rlist = []
    for i in range(length):
        rlist.append(random.randint(min, max))
    return rlist

# Big O (n^2)
def algorithm1(rlist):
    difference = float('inf')
    for i in range(len(rlist)):
        for j in range(len(rlist)):
            if i != j and abs(rlist[i] - rlist[j]) < difference:
                difference = abs(rlist[i] - rlist[j])
    return difference

# Big O (n log n) for sort
# Big O (n) for alg
def algorithm2(rlist):
    difference = float('inf')
    rlist.sort()
    for i in range(len(rlist) - 1):
        if abs(rlist[i] - rlist[i + 1]) < difference:
            difference = abs(rlist[i] - rlist[i + 1])
    return difference

def main():
    print("\nThis program finds the smallest difference between any two elements in a")
    print("randomly generated list of integers, using two different algorithms with")
    print("different Big-O efficiency.\n")

    minRange = int(input("Enter random min range: "))
    maxRange = int(input("Enter random max range: "))
    length = int(input("Enter length of list: "))

    ranList = randomListGenerator(minRange, maxRange, length)

    start = time.time()
    result1 = algorithm1(ranList)
    end = time.time()
    time1 = end - start

    start = time.time()
    result2 = algorithm2(ranList)
    end = time.time()
    time2 = end - start

    print("\nSmallest difference:", result1)
    print("List:", ranList)
    print("List length:", len(ranList))

    print(f"Algorithm 1 Time {time1:e}")
    print(f"Algorithm 2 Time {time2:e}")

if __name__ == "__main__":
    main()