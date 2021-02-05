
def intervalIntersection(firstList, secondList):
    if firstList ==[] or secondList == []:
        return []


    returnThis = []
    for list1,list2 in zip(firstList, secondList):
        if list1[1] != list2[0]:
            temp =  [max(list1[0],list2[0]),min(list1[1],list2[1])]
            returnThis.append(temp)
        if list1[1] == list2[0]:
            temp = [list1[0],list2[1]]
            returnThis.append(temp)
    return returnThis
    

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]] 
output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


print(intervalIntersection(firstList,secondList))
print(output)