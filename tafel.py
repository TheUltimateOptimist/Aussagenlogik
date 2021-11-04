from aussage import Aussage
from calculate import evaluate
from console import console
from print_table import printTable


def binaryNumberconverted(binaryString: str, numberOfVariables: int) -> list[Aussage]:
    """
    converts the binary number to a sequence of true / false values to create a list of expressions
    :param binaryString: the binary string representation of a sequence of true / false values
    :param numberOfVariables: the total number of expressions to generate (missing leading zeros will be filled autom.)
    :returns: a list of expressions generated from the binary string
    """

    binaryString = binaryString.split("b")[1]
    length = len(binaryString)
    if length < numberOfVariables:
        binaryString = (numberOfVariables - length) * "0" + binaryString
    resultList = []
    for element in binaryString:
        resultList.append(Aussage(element))
    return resultList


def row(index: int, numberOfVariables: int, expressions: list[str]) -> list[str]:
    """
    evaluates the expressions for the given row
    :param index: the index of the row to evaluate the entries for
    :param numberOfVariables: the total number of variables used
    :param expressions: the expressions to evaluate
    :returns: the resulting row as a list of strings
    """

    valueList = binaryNumberconverted(str(bin(index)), numberOfVariables)
    variableValueList = valueList
    for expression in expressions:
        valueList.append(evaluate(expression, False, True, numberOfVariables, variableValueList))
    for i, element in enumerate(valueList):
        valueList[i] = element.stringValue()
    return valueList


def printTafel():
    """
    entry point to create a table for boolean expressions:
        - asks the user how many variables to use
        - asks the user for any expressions to evaluate for all possible combinations of the variables
        - prints the resulting table to the console
    """

    numberOfVariables = int(input(">Gib die Anzahl der vorkommenden Variablen ein: "))
    outputString = ">Variablen: "
    for i in range(numberOfVariables):
        if i < numberOfVariables - 1:
            outputString += f"{chr(65 + i)}, "
        else:
            outputString += f"{chr(65 + i)}"
    console.print(outputString)
    expressions = []
    console.print(">Gib beliebig viele Ausdrücke mit den oben genannten Variablen ein")
    console.print(">Gib s ein, wenn du keine Ausdrücke mehr eingeben möchtest")
    text = ""
    i = 0
    while text != "s":
        text = input(f">{i + 1}. Ausdruck: ")
        if text != "s":
            expressions.append(text)
        i += 1
    list = []
    for j in range(2 ** numberOfVariables):
        list.append(row(j, numberOfVariables, expressions))
    columns = []
    for i in range(numberOfVariables):
        columns.append(chr(65 + i))
    for expression in expressions:
        columns.append(expression)
    printTable(list, columns, "green", ["white"], "white")
