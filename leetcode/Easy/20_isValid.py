#encoding=utf-8
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
#pairs = {"()":"","[]":"","{}":""}
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        i = 0
        pairs = ["()","[]","{}"]
        while i <len(s):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] + stack[-1] in pairs:
                stack.pop()
                stack.pop()
            i += 1
        return False if stack else True
        

if __name__=="__main__":
    Test=Solution()
    print(Test.isValid("()[]{}") == True)
    print(Test.isValid("()") == True)
    print(Test.isValid("(]") == False)
    print(Test.isValid("(])]") == False)
    print(Test.isValid("{[]}") == False)
    