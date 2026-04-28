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