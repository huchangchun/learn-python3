class Agent(object):
    _agent = dict()
    def __new__(cls, *p):
        number =p[0]
        if not number in cls._agent:
            cls._agent[number]  = object.__new__(cls)
        return cls._agent[number]
    def __init__(self, number):
        self.number = number
        
    def __eq__(self, rhs):
        return self.number == rhs.number
    
Agent("a") is Agent("a") == True