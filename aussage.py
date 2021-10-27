class Aussage:
    wertDarstellung = "binär"
    def __init__(self, value):
        match value:
            case True: self.value = value      
            case False: self.value = value
            case "0": self.value = False
            case "1": self.value = True
            case "f": self.value = False
            case "w": self.value = True
            case "false": self.value = False
            case "true": self.value = True
            case _: print(f"ERROR: DER WERT {value} ist für eine Aussage nicht zulässig! Zulässig sind: 0, f, false, 1, w, true")
        
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
