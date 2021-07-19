while(True):
    count = int(input())

    for i in range(1, count):
        s = ""
        for j in range(i, 0, -1):
            s += str(j)
        print('\t'*(count - 1), s)
    for i in range(count, 1, -1):
        s = ""
        for j in range(1, i):
            s += str(j)
        print('\t'*(count-i), s)
