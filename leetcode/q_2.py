# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
    joined_l1 = ''
    joined_l2 = ''
    for i in range(len(l1)):
        joined_l1 += str(l1[i]) 
        joined_l2 += str(l2[i])  
    temp = str(int(joined_l1)+int(joined_l2))  
    
    final_j = []
    for i in temp:
        i = str(i)
        for j in i:
            final_j.append(int(j))
    return final_j[::-1]

l1 = [2,4,3]
l2 = [5,6,4]
print(addTwoNumbers(l1,l2))
