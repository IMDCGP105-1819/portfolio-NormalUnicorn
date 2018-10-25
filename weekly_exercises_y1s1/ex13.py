def remove_dups(L1, L2):
    for x in range(len(L1)+1):
        if x in L2:
            L1.remove(x)
        print(L1)

L1 = [1,2,3,4]
L2 = [1,2,3,4]
remove_dups(L1, L2)
