#encoding=utf-8
import os
import sys
root_path = os.path.abspath("../../")
if root_path not in sys.path:
    sys.path.append(root_path)
from timeopt.Timing import Timing
"""
有一座高度是10级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶。要求用程序来求出一共有多少种走法。

"""
class ClimbingWays:
    getClimbingWaysTiming = Timing()
    @getClimbingWaysTiming.timeit(level=1, prefix="[API] ")
    def getClimbingWays_recurve(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.getClimbingWays_recurve(n-1) + self.getClimbingWays_recurve(n-2)
    
    @getClimbingWaysTiming.timeit(level=1, prefix="[API] ")
    def getClimbingWays_note(self, n: int, d: dict) -> int:
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in d:
            return d[n]
        else:
            val = self.getClimbingWays_note(n - 1, d) + self.getClimbingWays_note(n - 2, d)
            d[n] = val
            return val
        
    @getClimbingWaysTiming.timeit(level=1, prefix="[API] ")
    def getClimbingWays_np(self, n: int) -> int:  
        if n < 1:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        tmp = 0
        for i in range(3, n+1):
            tmp = a + b
            a = b
            b = tmp
        return tmp
 
if __name__ == "__main__":
    Test = ClimbingWays()
    dc = {}
    #print(Test.getClimbingWays_recurve(50))
    print(Test.getClimbingWays_note(50,dc))
    print(Test.getClimbingWays_np(50))
    Test.getClimbingWaysTiming.show_timing_log()