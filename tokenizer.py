from aussage import Aussage
from language import operations, values
from variables import Variables
from listHelper import getClosingBraceIndex
class Tokenizer:
    def __init__(self, expression, tafel = False, numberOfVariables = 0, aussagenObjects = []):
        self.numberOfVariables = numberOfVariables
        self.aussagenObjects = aussagenObjects
        self.expression = expression
        self.tafel = tafel
        if not tafel:
            self.words = operations + values + Variables.names
        else:
            self.words = []
            for operation in operations:
                self.words.append(operation)
            for i in range(numberOfVariables):
                self.words.append(chr(65 + i))
    def __isWord(self, textString):
        for word in self.words:
            if word == textString:
                return True
        return False 
    def __isContainedInWord(self, textString):
        for word in self.words:
            if word.__contains__(textString):
                return True
        return False
 
    def __nextSymbolNotALetter(self, currentIndex, text):
        if len(text) == currentIndex + 1:
            return True
        code = ord(text[currentIndex + 1])
        if (code < 65 or code > 90) and (code < 97 or code > 122):
            return True
        else:
            return False

    def __isValue(self, element):
        for value in values:
            if str(element.__class__) == "<class 'str'>" and value == element:
                return True
        return False
    def __dissolveVariables(self, list):
        if not self.tafel:
            for i,token in enumerate(list):
                if Variables.contains(token):
                    list[i] = Variables.getValue(token) 
            for i, token in enumerate(list):
                if self.__isValue(token):
                    list[i] = Aussage(token)
            return list         
        else:
            for i, token in enumerate(list):
                if len(token) == 1:
                    code = ord(token)
                    if code >= 65 and code <= 64 + self.numberOfVariables:
                        list[i] = self.aussagenObjects[code - 65]
            return list
    def __braceNichtTokens(self, list):
        for i,element in enumerate(list):
            if element == "nicht" and list[i + 1] == "nicht":
                del list[i + 1]
                del list[i]
            elif (element == "nicht" and i == 0) or (element == "nicht" and list[i - 1] != "("):
                closingBraceIndex = i + 2
                if list[i + 1] == "(":
                    closingBraceIndex = getClosingBraceIndex(i + 1,list) + 1
                if closingBraceIndex < len(list) - 1:
                    list.insert(closingBraceIndex, ")")
                else:
                    list.append(")")
                list.insert(i, "(")
        return list

    def tokenize(self):
        resultList = []
        word = ""
        for i in range(len(self.expression)):
            if self.__isContainedInWord(word + self.expression[i]):
                if self.__isWord(word + self.expression[i]) and self.__nextSymbolNotALetter(i, self.expression):
                    resultList.append(word + self.expression[i])
                    word = ""
                else:
                    word = word + self.expression[i]
            elif self.expression[i] == "(" or self.expression[i] == ")":
                    resultList.append(self.expression[i])
                    word = ""
            else:
                word = ""
        resultList = self.__braceNichtTokens(resultList)
        return self.__dissolveVariables(resultList)
    