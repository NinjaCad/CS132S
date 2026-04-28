"""
    Deliverable: Homework05.py


    References:

        https://runestone.academy/runestone/books/published/pythonds3/Recursion/DynamicProgramming.htmlLinks to an external site.
    

    Sample Input/Output:

        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework05.py 

        This program efficiently computes the minimum total number of character 
        insertion, deletion, and/or substitution operations required to transform 
        one string into another.

        The String Transformation Operations REquired (STORE) function can be 
        defined recursively via the following pseudocode:

        if len(string1) == 0:                      # base case: string1 empty
            store(string1, string2) = len(string2) # this many insertions to string 1 required
        elif len(string2) == 0:                    # base case: string2 empty
            store(string1, string2) = len(string1) # this many deletions from string 1 required
        elif string1[-1] == string2[-1]:           # last characters are the same
            store(string1, string2) = store(string1[0:-1], string2[0:-1]) # no operation needed
        else:                                      # last characters differ
            store(string1, string2) = 1+min(store(string1[0:-1], string2      ), # insertion
                                            store(string1      , string2[0:-1]), # deletion
                                            store(string1[0:-1], string2[0:-1])) # substitution

        Rather than computing overlapping subproblem answers repeatedly, this program 
        computes each of them once, storing them into a table (dynamic programming).

        Enter string1: dynamic
        Enter string2: programming

                p  r  o  g  r  a  m  m  i  n  g
            0  1  2  3  4  5  6  7  8  9 10 11
        d  1  1  2  3  4  5  6  7  8  9 10 11
        y  2  2  2  3  4  5  6  7  8  9 10 11
        n  3  3  3  3  4  5  6  7  8  9  9 10
        a  4  4  4  4  4  5  5  6  7  8  9 10
        m  5  5  5  5  5  5  6  5  6  7  8  9
        i  6  6  6  6  6  6  6  6  6  6  7  8
        c  7  7  7  7  7  7  7  7  7  7  7  8

        store("dynamic", "programming") = 8
        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework05.py 

        This program efficiently computes the minimum total number of character 
        insertion, deletion, and/or substitution operations required to transform 
        one string into another.

        The String Transformation Operations REquired (STORE) function can be 
        defined recursively via the following pseudocode:

        if len(string1) == 0:                      # base case: string1 empty
            store(string1, string2) = len(string2) # this many insertions to string 1 required
        elif len(string2) == 0:                    # base case: string2 empty
            store(string1, string2) = len(string1) # this many deletions from string 1 required
        elif string1[-1] == string2[-1]:           # last characters are the same
            store(string1, string2) = store(string1[0:-1], string2[0:-1]) # no operation needed
        else:                                      # last characters differ
            store(string1, string2) = 1+min(store(string1[0:-1], string2      ), # insertion
                                            store(string1      , string2[0:-1]), # deletion
                                            store(string1[0:-1], string2[0:-1])) # substitution

        Rather than computing overlapping subproblem answers repeatedly, this program 
        computes each of them once, storing them into a table (dynamic programming).

        Enter string1: recursion
        Enter string2: revision

                r  e  v  i  s  i  o  n
            0  1  2  3  4  5  6  7  8
        r  1  0  1  2  3  4  5  6  7
        e  2  1  0  1  2  3  4  5  6
        c  3  2  1  1  2  3  4  5  6
        u  4  3  2  2  2  3  4  5  6
        r  5  4  3  3  3  3  4  5  6
        s  6  5  4  4  4  3  4  5  6
        i  7  6  5  5  4  4  3  4  5
        o  8  7  6  6  5  5  4  3  4
        n  9  8  7  7  6  6  5  4  3

        store("recursion", "revision") = 3
        >>> 


    100	CS132S Rubric HW05:
        4	Initial I/O
        8	Base Case: string1 empty
        8	Base Case: string2 empty
        8	Recurrence Relation: last characters same
        16	Recurrence Relation: last characters differ
        16	Use Dynamic Programming Lookup Table, Not Recursion
        10	Output
        10	Readability
        20	Quality of Solution (100% for bottom up, 90% for memoization)
"""

def store(string1, string2, table):
    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if (i == 0):
                table[i][j] = j
            elif (j == 0):
                table[i][j] = i
            elif (string1[i - 1] == string2[j - 1]):
                table[i][j] = table[i - 1][j - 1]
            else:
                insertion = table[i - 1][j]
                deletion = table[i][j - 1]
                substitution = table[i - 1][j - 1]
                table[i][j] = 1 + min(insertion, deletion, substitution)

    print("\n   ", *list(string2))
    print(" ", *table[0])
    for i in range(1, len(string1) + 1):
        print(string1[i - 1], *table[i])

    return table[len(string1)][len(string2)]

def main():
    print("\nThis program efficiently computes the minimum total number of character")
    print("insertion, deletion, and/or substitution operations required to transform")
    print("one string into another.\n")

    print("The String Transformation Operations REquired (STORE) function can be")
    print("defined recursively via the following pseudocode:\n")
    print("if len(string1) == 0:                      # base case: string1 empty")
    print("    store(string1, string2) = len(string2) # this many insertions to string 1 required")
    print("elif len(string2) == 0:                    # base case: string2 empty")
    print("    store(string1, string2) = len(string1) # this many deletions from string 1 required")
    print("elif string1[-1] == string2[-1]:           # last characters are the same")
    print("    store(string1, string2) = store(string1[0:-1], string2[0:-1]) # no operation needed")
    print("else:                                      # last characters differ")
    print("    store(string1, string2) = 1+min(store(string1[0:-1], string2      ), # insertion")
    print("                                    store(string1      , string2[0:-1]), # deletion")
    print("                                    store(string1[0:-1], string2[0:-1])) # substitution\n")

    print("Rather than computing overlapping subproblem answers repeatedly, this program")
    print("computes each of them once, storing them into a table (dynamic programming).\n")

    s1 = input("Enter string1: ")
    s2 = input("Enter string2: ")
    minimum = store(s1, s2, [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)])
    print(f'\nstore("{s1}", "{s2}") = {minimum}\n')

if __name__ == "__main__":
    main()