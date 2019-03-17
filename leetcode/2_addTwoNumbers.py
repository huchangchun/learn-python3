"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
#encoding=utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
     
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        tempNode = None
        nextplus = 0
        val = 0
        def createNewNode(value):
            plus = 0
            if value < 10:
                value = value
            else:
                plus = value // 10
                value = value % 10
            return ListNode(value),plus               
        while l1 is not None and l2 is not None:
            val =  l1.val + l2.val + nextplus
            l1 = l1.next
            l2 = l2.next 
            newNode,nextplus = createNewNode(val)
            if root is None:
                root = tempNode = newNode
            else:
                tempNode.next = newNode
                tempNode = newNode
        l3 = l1 if l1 is not None else l2 if l2 is not None else None
        while l3 is not None:
            val = l3.val + nextplus
            l3 = l3.next
            newNode,nextplus = createNewNode(val)
            tempNode.next = newNode
            tempNode = newNode
        if nextplus != 0:
            tempNode.next = ListNode(nextplus)
            tempNode = newNode            
        return root
              
 
    def printPreNode(self,  l1: ListNode) -> ListNode:
        if l1.next is not None:
            print(l1.val,"-> ",end="")  
        else:
            print(l1.val)  
            return
        l1 = l1.next
        self.printPreNode(l1)        
    def printPostNode(self, l1: ListNode) -> ListNode:
        if l1.next is  None:
            print(l1.val,end=" ")
            return 
        else:
            self.printPostNode(l1.next)
            print("->",end=" ")
        print(l1.val,end=" ")
        
        
             
 
if __name__ == "__main__":
    Test = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    #l1.next.next.next = ListNode(9)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    Test.printPreNode(l1)
    Test.printPreNode(l2)
 
    retNode = Test.addTwoNumbers(l1, l2)
    Test.printPreNode(retNode)