#encoding=utf-8
"""

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = tmp = ListNode(-1)
        if not l1 or not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        
        res =  l1 or l2
        while res:
            tmp.next =ListNode(res.val)
            res = res.next
            tmp = tmp.next
 
        return root.next
        
    def prePrint(self, l1: ListNode):
        if l1:
            print(l1.val,end="")
        if l1.next:
            print(" -> ",end="")
        else:
            print()
            return
        self.prePrint(l1.next)
        
        
if __name__=="__main__":
    import copy
    Test = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)
    l2= ListNode(3)
    l2.next = ListNode(5)
    l2.next.next = ListNode(7)
    l2.next.next.next = ListNode(8)    
    
    Test.prePrint(l1)
    Test.prePrint(l2)
    m1=Test.mergeTwoLists(l1, l2)
    m2 = copy.deepcopy(m1)
    Test.prePrint(m1)
    """
       
    while 部分不能替换为
            #if l1: 
                #tmp.next = l1
            #if l2:
                #tmp.next = l2
            
    """ 
  
    l2.next.next.next.val = 9
    print("change l2:")
    Test.prePrint(l2)
    print("mergelst is changed")
    Test.prePrint(m1)
    Test.prePrint(m2)

    
    print("ok")
    """
    1 -> 2 -> 4 -> 5
    3 -> 5 -> 7 -> 8
    1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 7 -> 8
    3 -> 5 -> 7 -> 9
    1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 7 -> 9
    ok
    """