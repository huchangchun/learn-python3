#encoding=utf-8
"""
如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？
我们从最小的i开始，当i = 0，由于1,3,5都大于0，既没有比0小的币值，因此凑够0元需要0个硬币
我们用d[i] =j表示凑够i元最少需要j个硬币，于是我们已经得到d[0] =0 ,表示凑够0元需要最少0个硬币
当i=1, min(d[1]) = d[1-1] + 1 = d[0] + 1 = 1
当i=2, min(d[2]) = d[2-1] + 1 = d[1] + 1 = 2
当i=3, min(d[3]) = d[3-1] + 1 = d[2] + 1 = 2 + 1 = 3 < d[3-3] = 1
当i=4, min(d[4]) = d[4-1] + 1 = d[3] + 1 = 1 + 1 or d[4-3] + 1= d[1] + 1 = 1 + 1 = 2
当i=5, min(d[5]) = d[5-1] + 1 = d[4] + 1 = 2 + 1 = 3 < d[5-5] + 1 = d[0] + 1 = 1
min(d[i]) = min{d(i-vj) + 1}

"""
class Solution:
    """
    d(i) = min{d(i-vj)  + 1},i-vj>=0 ,vj表示第j个硬币的面值
    """
    def coins(self, M):
        n = [0]
        for i in range(1, M + 1):
            l = []
            for vj in [1,3,5]:
                if i - vj >=0:
                    l.append(n[i-vj] + 1)
            n.append(min(l))
        return n[-1]
 
            
if __name__=="__main__":

    Test = Solution()
    print(Test.coins(11))
  