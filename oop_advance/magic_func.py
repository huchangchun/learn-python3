#encoding=utf-8
class  Magic:
    _myInfo = []
    def __init__(self,age=None,name=None,sex=None,uuid=None):
        self.age = age
        self.sex = sex
        self.name = name
        self.uuid = uuid
        if self.age is not None and self.name is not None and self.sex is not None and self.uuid is not None:
            self.setMyinfo()
   
    def setMyinfo(self):
            if self.uuid not in Magic._myInfo:
                Magic._myInfo.append({self.uuid:{"age":self.age,"name":self.name,"sex":self.sex}})
                
    def __getitem__(self,key):
        try:
            if key in Magic._myInfo:
                return Magic._myInfo[key]
        except KeyError:
            return "Hello"
    def __setitem__(self,key,value):
        if key not in Magic._myInfo:     
            Magic._myInfo.append({value["uuid"]:{"age":value["age"],"name":value["name"],"sex":value["sex"]}})
        
    def __delitem__(self,key):
        for item in Magic._myInfo:
            if key in item:
                Magic._myInfo.remove(item)        
    @staticmethod
    def printInfo():
        for item in Magic._myInfo:
            for k,subitem in item.items():
                print("------------------")
                print("id:",k)
                for k,v in subitem.items():
                    print("{0}={1}".format(k,v))
                print("------------------")
a=Magic(18,"Jack","Man","1123")
b=Magic(19,"Tom","Man","1235")
dic = {"uuid":"1236","age":29,"name":"John","sex":"Female"}
b['1236'] = dic
b.printInfo()
del b['1236']
b.printInfo()
