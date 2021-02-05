## first solution 59/85

def intervalIntersection(firstList, secondList):

    returnThis = []
    firstpoint,secondpoint = 0,0
    while firstpoint < len(firstList) and secondpoint < len(secondList):
        f_1,f_2 = firstList[firstpoint]
        s_1,s_2 = secondList[secondpoint]
        first_and_first = max(f_1,s_1)
        second_and_second = min(f_2,s_2)
        if second_and_second - first_and_first >= 0:
            returnThis.append([first_and_first,second_and_second])
        if f_2 < s_2:
            firstpoint += 1
        else:
            secondpoint +=1
    return returnThis

    # return (sorted(returnThis, key = lambda x: x[0]))
    

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]] 
output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


print(intervalIntersection([[14,16]],[[7,13],[16,20]]))


