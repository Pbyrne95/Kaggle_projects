def minimumSwap(s1,s2):
    if len(s1) != len(s2): return -1

    countyx = 0
    countxy = 0
    for c1,c2 in zip(s1,s2):
        if c1 == "x" and c2 == "y": countyx+=1
        elif c1 == "y" and c2 == "x": countxy+=1

    if (countxy + countyx ) % 2 == 1: return -1
    return countxy // 2 + countyx // 2 + countxy % 2 + countyx % 2