from typing import Any
from aussage import Aussage
from language import operations, values
from variables import Variables
from listHelper import getClosingBraceIndex


class Tokenizer:
    """
    generates a sequence of tokens using an input string
    """

    def __init__(self, expression: str, tafel: bool = False, numberOfVariables: int = 0, aussagenObjects: list = []):
        """
        creates an object of type Tokenizer
        :param expression: the expression to parse
        :param tafel: TODO ?!
        :param numberOfVariables: the number of variables that could exist in the expression
        :param aussagenObjects: TODO ?!
        """

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

    def __isWord(self, textString: str) -> bool:
        """
        whether or not textString is an existing word-symbol in this language
        :param textString: the text to check for symbolness :D
        :returns: true if the text represents an existing word-symbol in this language, false otherwise
        """

        for word in self.words:
            if word == textString:
                return True
        return False

    def __isContainedInWord(self, textString: str) -> bool:
        """
        whether or not textString could be any predefined word-symbol
        :param textString: the text to check for 'could-be-predefinedness' xD
        :returns: true if the text could be a predefined word-symbol, false otherwise
        """

        for word in self.words:
            if textString in word:
                return True
        return False

    def __nextSymbolNotALetter(self, currentIndex: int, text: str) -> bool:
        """
        whether or not the next symbol doesn't exist or would not be a letter
        :param currentIndex: the current index to deduce the next index from
        :param text: the text where to look for the next symbol
        :returns: true if the text is not long enough or next symbol is not a letter, false otherwise
        """

        if len(text) == currentIndex + 1:
            return True

        code = ord(text[currentIndex + 1])
        if (code < 65 or code > 90) and (code < 97 or code > 122):
            return True
        else:
            return False

    def __isValue(self, element: Any) -> bool:
        """
        whether or not the element represents a valid value-symbol in this language
        :param element: any element to check
        :returns: True if elements class is str and represents a valid value-symbol in this language, fals otherwise
        """

        for value in values:
            if str(element.__class__) == "<class 'str'>" and value == element:
                return True
        return False

    def __dissolveVariables(self, list: list) -> list:
        """
        replaces all variables with its values
        :param list: where to replace all variables with its values
        :returns: the list with all variables replaced
        """

        if not self.tafel:
            for i, token in enumerate(list):
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
        """
        embraces all tokens that corresponds to a 'Nicht'-token
        :param list: the list of tokens where to work on
        :returns: the modified list
        """

        for i, element in enumerate(list):
            if element == "nicht" and list[i + 1] == "nicht":
                del list[i + 1]
                del list[i]
            elif (element == "nicht" and i == 0) or (element == "nicht" and list[i - 1] != "("):
                closingBraceIndex = i + 2
                if list[i + 1] == "(":
                    closingBraceIndex = getClosingBraceIndex(i + 1, list) + 1
                if closingBraceIndex < len(list) - 1:
                    list.insert(closingBraceIndex, ")")
                else:
                    list.append(")")
                list.insert(i, "(")
        return list

    def tokenize(self):
        """
        tokenizes the input string
        :returns: the corresponding list of tokens
        """
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
