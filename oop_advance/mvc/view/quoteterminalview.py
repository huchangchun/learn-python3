# -*- coding:utf-8 -*-
class QuoteTerminalView(object):
    '''视图层'''
    def show(self,quote):
        '''显示查询结果
        @parameter quote 接收数据'''
        print("您查询到的名人名言是：%s" %(quote))
    def error(self,msg):
        print("error:%s" %(msg))
    def select_quote(self):
        return input("请您输入编号进行查询：")