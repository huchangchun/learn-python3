"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Input: (2 -> 4 -> 6 ->2) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 2 ->3
Explanation: 3462 + 465 = 7023.
"""
#encoding=utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
     
    #124 ms 
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        tempNode = None
        carry = 0
        val = 0
           
        while l1  and l2  :
            val =  l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next 
            carry = val // 10 
            if root is None:
                root = tempNode = ListNode(val % 10)
            else:
                tempNode.next = ListNode(val % 10)
                tempNode =  tempNode.next
        l3 = l1 or l2
        while l3 :
            val = l3.val + carry
            l3 = l3.next
            carry = val // 10
            tempNode.next = ListNode(val % 10)
            tempNode = tempNode.next
        if carry != 0:
            tempNode.next = ListNode(carry)
                   
        return root
              
    #shoter version 108ms
    def addTwoNumbers(self, l1: ListNode, l2 : ListNode) -> ListNode:
        p = dummy = ListNode(-1)
        carry = 0 
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry  = val // 10
            p.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next
    def printPreNode(self,  l1: ListNode) -> ListNode:
        if l1.next:
            print(l1.val,"-> ",end="")  
        else:
            print(l1.val)  
            return
        l1 = l1.next
        self.printPreNode(l1)        
    def printPostNode(self, l1: ListNode) -> ListNode:
        if l1.next:
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