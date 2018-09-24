#-*- coding:utf-8
#Tree-Node Type
class Node:
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
       
    def isLeft(self):
        return self.father.left == self
#create nodes创建叶子节点
def createNodes(freqs):
    return [Node(freq) for freq in freqs]
#create Huffman-Tree创建Huffman树
def createHuffmanTree(nodes):
    """
    创建Huffman树的思想是:每次都pop排序(这里采用从小到大)后的两个节点生成父节点，然后append父节点
    直到只有一个节点;
    
    获取所有节点存放在queue中
    while循环直到queue长度为1
    {
        对queue进行从小到大排序:排序能保证每次更新后的queue都是从小到大排序，
        pop两个节点出来作为左右孩子节点l,r
        创建父节点f
        l,r的父节点指向父节点f
        父节点f的左右孩子分别指向l,r
        queue增加父节点
    }
    循环结束后queue中只剩一个节点，该节点的权重是最大的一个，即根节点，根节点的父节点置空
    """
    queue = nodes[:] #切片赋值后生成新的对象，如果queue=nodes直接赋值，修改queue会改动原有的nodes
    while(len(queue))> 1:
        queue.sort(key=lambda item :item.freq)
        left_node = queue.pop(0)
        right_node = queue.pop(0)
        father_node = Node(left_node.freq + right_node.freq)
        father_node.left = left_node
        father_node.right = right_node
        left_node.father = father_node
        right_node.father = father_node
        queue.append(father_node)
    queue[0].father = None
    return queue[0]
  
#Huffman编码
def huffmanEncoding(nodes,root):
    """
    生成一个list用于存放节点的编码
    遍历nodes，对每个node进行向上编码，直到父节点为根节点，如果父节点不是根节点：
    若为左孩子节点则编码为1，若为右孩子节点则编码为0
    编码表
    """
    
    codes = [""] * len(nodes)
    for i,item in enumerate(nodes):
        while item != root:
            if item.isLeft():
                codes[i] = '1' + codes[i]
            else:
                codes[i] = "0" + codes[i]
            item = item.father
    return codes

if __name__ == '__main__':
     
    chars_freqs = [('我', 15),('喜欢', 8),('观看', 6),('巴西', 5),('足球', 3),('世界杯',1)]    
    nodes = createNodes([item[1] for item in chars_freqs])
    root = createHuffmanTree(nodes)
    codes = huffmanEncoding(nodes,root)
    for item in zip(chars_freqs,codes):
        print('%s  freq:%-2d    encoding: %s' % (item[0][0],item[0][1],item[1]))

 