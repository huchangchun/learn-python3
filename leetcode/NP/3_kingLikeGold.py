#encoding=utf-8
import os
import sys
root_path = os.path.abspath("../../")
if root_path not in sys.path:
    sys.path.append(root_path)
from timeopt.Timing import Timing
"""
有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。
参与挖矿工人的总数是10人。
每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。
要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？
A. 500金/5人
B. 200金/3人
C. 300金/4人
D. 350金/3人
E. 400金/5人

"""
class King:
    pass