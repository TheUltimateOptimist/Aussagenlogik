from tokenizer import Tokenizer
from listHelper import split_list, delete_range, getClosingBraceIndex
from my_console import console

def evaluateTokenList(tokenList):
        i = 0
        while i < len(tokenList):
            token = tokenList[i]
            if token == "(":
                closingBraceIndex = getClosingBraceIndex(
                    i, tokenList)
                tokenList[i] = evaluateTokenList(split_list(
                    i + 1, closingBraceIndex - 1, tokenList))
                tokenList = delete_range(i + 1, closingBraceIndex, tokenList)
            i += 1
        i = 0
        while i < len(tokenList):
            token = tokenList[i]
            if str(token.__class__) == "<class 'str'>" and token == "nicht":
                tokenList[i] = tokenList[i + 1].nicht()  
                del tokenList[i + 1]
            elif str(token.__class__) == "<class 'str'>" and token == "und":
                tokenList[i] = tokenList[i - 1].und(tokenList[i + 1])
                del tokenList[i + 1]
                del tokenList[i - 1]
            elif str(token.__class__) == "<class 'str'>" and token == "oder":
                tokenList[i] = tokenList[i - 1].oder(tokenList[i + 1])
                del tokenList[i + 1]
                del tokenList[i -1]    
            elif str(token.__class__) == "<class 'str'>" and token == "xor":
                tokenList[i] = tokenList[i - 1].xor(tokenList[i + 1])   
                del tokenList[i + 1] 
                del tokenList[i - 1]
            elif str(token.__class__) == "<class 'str'>" and token == "folgt":
                tokenList[i] = tokenList[i - 1].folgt(tokenList[i + 1])   
                del tokenList[i + 1] 
                del tokenList[i - 1]
            else:
                i += 1
        return tokenList[0]

def calculate(expression, shouldPrint = False, tafel = False, numberOfVariables = 0, aussagenObjects = []):
    if tafel:
        result = evaluateTokenList(Tokenizer(expression, True, numberOfVariables, aussagenObjects).tokenize())
    else:
        result = evaluateTokenList(Tokenizer(expression).tokenize())
    if shouldPrint:
        console.print(result.stringValue())
    return result
