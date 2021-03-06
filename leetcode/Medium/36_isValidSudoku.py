#encoding=utf-8
"""
 Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:
"""
class Solution:
    def isValidSudoku1(self, board: [[str]]) -> bool:
        """
        判断行数字是否为1-9
        判断列数字是否为1-9
        判断3x3九宫格数字是否为1-9
        """
        rowset = set()
        colset = set()        
        for row in range(9):
            rowset.clear()
            colset.clear()
            bestset = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] not in rowset:
                        rowset.add(board[row][col])
                    else:
                        return False
             
                if board[col][row] != '.':
                    if board[col][row] not in colset:
                        colset.add(board[col][row])
                    else:   
                        return False
        
        bestset = set()
        for i in range(3):
            for j in range(3):
                bestset.clear()
                for k in range(3):
                    for n in range(3):
                        row = 3 * i + k
                        col = 3 * j + n
                        if board[row][col] != '.':
                            if board[row][col] not in bestset:
                                bestset.add(board[row][col])
                            else:
                                return False                            
                             
        return True
   
   
if __name__=="__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Test = Solution()
    print(Test.isValidSudoku(board) == True)
    print(Test.isValidSudoku(board) == False)
  
