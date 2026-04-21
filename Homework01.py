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

main()