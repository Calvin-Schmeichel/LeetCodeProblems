# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToString(NumberList, index):
    if index == 0:
        return str(NumberList[index])
    
    return str(NumberList[index])+ListToString(NumberList, index-1)
    


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #print(ListToString(l1, len(l1)-1))
        #print(ListToString(l2, len(l2)-1))

        sum = str(int(ListToString(l1, len(l1)-1))+int(ListToString(l2, len(l2)-1)))
        #print(sum)

        SumList = []

        for n in range(len(sum)-1, -1, -1):
            SumList.append(int(sum[n]))

        return SumList


        



print(Solution.addTwoNumbers(Solution, [2,4,3], [5,6,4]))