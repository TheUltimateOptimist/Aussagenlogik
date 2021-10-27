class Aussage:
    wertDarstellung = "binär"
    def __init__(self, value):
        if value == True:
            self.value = value
        elif value == False:
            self.value = False
        elif value == "true":
            self.value = True
        elif value == "false":
            self.value = False
        elif value == "1":
            self.value = True
        elif value == "0":
            self.value = False
        elif value == "w":
            self.value = True
        elif value == "f":
            self.value = False
        else:
            print(f"ERROR: DER WERT {value} ist für eine Aussage nicht zulässig! Zulässig sind: 0, f, false, 1, w, true")
    
    def nicht(self):
        if self.value:
            return Aussage(False)
        else:
            return Aussage(True)

    def und(self, aussageB):
        if  self.value and aussageB.value:
            return Aussage(True)
        else:
            return Aussage(False)    

    def oder(self, aussageB):
        if self.value or aussageB.value:
            return Aussage(True)
        else:
            return Aussage(False)

    def xor(self, aussageB):
        if (self.value and not aussageB.value) or (aussageB.value and not self.value):  
            return Aussage(True)    
        else:
            return Aussage(False)

    def folgt(self, aussageB):
        if self.value and not aussageB.value:
            return Aussage(False)
        else:
            return Aussage(True)
   
    def stringValue(self):
        if self.value and self.wertDarstellung == "binär":
            return "1"
        elif not self.value and self.wertDarstellung == "binär":
            return "0"
        elif self.value and self.wertDarstellung == "wf":
            return "w"
        elif not self.value and self.wertDarstellung == "wf":
            return "f"
        elif self.value and self.wertDarstellung == "truefalse":
            return "true"    
        elif not self.value and self.wertDarstellung == "truefalse":
            return "false"   
        else: raise ValueError      
