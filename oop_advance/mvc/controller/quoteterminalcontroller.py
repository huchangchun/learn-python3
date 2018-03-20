# -*- coding:utf-8 -*-
import sys
sys.path.append('../')
from model.quote_model import QuotesModel
from view.quoteterminalview import QuoteTerminalView

class QuoteterminalController(object):
    '''控制层'''
    def __init__(self):
        self.model = QuotesModel()
        self.view = QuoteTerminalView()
    def run(self):
        n = self.view.select_quote()
        try:
            index = int(n)
            quote = self.model.get_quotes(index)
            self.view.show(quote)
        except ValueError as err:
            self.view.error('不合法的索引值')