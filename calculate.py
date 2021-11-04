from __future__ import annotations
from rich.text import Text
from aussage import Aussage
from listHelper import split_list, delete_range, getClosingBraceIndex
from console import console
from tokenizer import Tokenizer


def evaluateTokenList(tokenList: list[str | Aussage]) -> Aussage:
    """
    evaluates the given list of tokens
    :parameter tokenList: a list of tokens from the tokenizer to evaluate
    :returns: the value the token list evaluates to
    """

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
            del tokenList[i - 1]
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


def evaluate(expression: str, shouldPrint: bool = False, tafel: bool = False,
             numberOfVariables: int = 0, aussagenObjects: list[str | Aussage] = []) -> Aussage:
    """
    takes an expression and evaluates the result
    :parameter expression: the expression to evaluate
    :parameter shouldPrint: whether or not to print the value to the console
    :parameter tafel: whether or not to use the values of numberOfVariables and aussagenObjects
    :parameter numberOfVariables: the number of variables to create
    :parameter aussagenObjects: TODO whats that?!
    :returns: the evaluated result
    """

    if tafel:
        result = evaluateTokenList(Tokenizer(expression, True, numberOfVariables, aussagenObjects).tokenize())
    else:
        result = evaluateTokenList(Tokenizer(expression).tokenize())
    if shouldPrint:
        console.print(Text(result.stringValue(), "bold green"))
    return result
