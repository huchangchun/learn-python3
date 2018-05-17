#-*- coding: utf-8 -*-
"""
二叉查找树是满足以下条件的二叉树：
1、左子树上的所有节点值均小于根节点值
2、右子树上的所有节点值均大于根节点值
3、左右子树也满足上述两个条件

二叉查找树的插入过程如下：
1、若当前二叉查找树为空，则插入的元素位根节点
2、若插入的元素值小于根节点，则将元素插入到左子树中
3、若插入的元素值大于根节点之，则将元素插入到右子树中

二叉查找树的删除，分三种情况：
1、如果节点d没有孩子节点，只需直接删除该节点，修改父节点：将d用Null替换
2、如果节点d只有一个孩子，那么将这个孩子节点提升到d的位置，并修改d的父节点，用d替换z;
3、如果节点d有两个孩子，那么查找d的后继y，此后继一定在d的右子树中，且y是d右子树中最小的节点，然后用y替换z

参考https://segmentfault.com/a/1190000004271781
"""
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    # 中序遍历
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def spliceOut(self):
        ##最小值为右子树中中序遍历第一个节点,可能是左节点也可能是右节点：
        # 1、最小值为左叶子节点
        # 2、最小值没有左孩子，但是有右孩子
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():  # 一般不存在
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

                pass

class BinarySearchTree:
    def __init__(self,root=None,size=0):
        self.root = None
        self.size = size

    def length(self):
        return self.size

    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key <currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def __getitem__(self, key):
        return self.get(key)
    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size -1 
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError('Error,key not in tree')
    def __delitem__(self,key):
        self.delete(key)

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

    def put(self,key,val):
        if self.root: #root not None ,put item
            self._put(key,val,self.root)
        else: #init root
            self.root = TreeNode(key,val)
        self.size = self.size + 1
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
    def preOrder(self,tree):
        if tree == None:
            return
        self.preOrder(tree.leftChild)
        print(tree.key)
        self.preOrder(tree.rightChild)

if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3]="A"
    mytree[4]="B"
    mytree[6]="C"
    mytree[2]="D"
    mytree[5] = "E"
    mytree[2.5] = "F"
    mytree[1] = "G"
    mytree[10] = "H"
    print(mytree.root.payload)
    print("----中序遍历-------")
    mytree.preOrder(mytree.root)
    print("----中序遍历-------")
    for i in mytree.__iter__():
        print(i)
    print("删除6")
    mytree.__delitem__(6)
    print("----中序遍历-------")
    for i in mytree.__iter__():
        print(i)
