def lsearch(l, v):
    c = 0

    while c < len(l):
        if l[c] == v:
            return c
        c += 1
    else:
        return -1


l = [10, 20, 30, 40, 50, 75]
v = 40


def main():
    print(lsearch(l, v))
    print("--------------------")


if __name__ == '__main__':
    main()
