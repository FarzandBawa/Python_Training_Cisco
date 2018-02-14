# WAP to take a string of length k and a var n where n is a factor of k and print
# n lines taking a contiguous block of n values from k with distinct characters.


def splitStr(ss, n):
    i = 0
    while (i < len(ss)):
        s = ""
        for j in ss[i:i + n]:
            if j not in s:
                s += j
        print(s)
        i += n


ss = "ABCCAAADA"
n = 3
splitStr(ss, n)
