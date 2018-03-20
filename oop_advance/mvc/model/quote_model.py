# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from database.quote import Quotes
class QuotesModel(object):
    '''模型层
    只有模型层才能直接访问数据
    '''
    def get_quotes(self,index):
        ''''''
        try:
            value = Quotes[index]
        except IndexError as err:
            value = 'Not Found'
        return value