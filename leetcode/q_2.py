# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# stringifying the solution into a linked list 
def addTwoNumbers1(l1, l2):
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


# Solution 2 -> using a linked list 

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2


        currentCarry = 0 

        head = cur = ListNode(0)

        while p1 or p2 or currentCarry:

            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0 
            
            cur.next = ListNode(currentVal)
            cur = cur.next

            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next 
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next 
                p2 = p2.next
        return head.next    




