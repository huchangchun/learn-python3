# -*- coding:utf-8 -*-
from controller.quoteterminalcontroller import QuoteterminalController
def mains():
    while True:
        controller = QuoteterminalController()
        controller.run()
if __name__ == '__main__':
    mains()