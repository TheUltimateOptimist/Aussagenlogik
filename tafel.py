from aussage import Aussage
from calculate import calculate
from my_console import console
from print_table import printTable

def binaryNumberconverted(binaryString, numberOfVariables):
    binaryString = binaryString.split("b")[1]
    length = len(binaryString)
    if length < numberOfVariables:
        binaryString = (numberOfVariables - length)*"0" + binaryString
    resultList = []
    for element in binaryString:
        resultList.append(Aussage(element))
    return resultList

def row(index, numberOfVariables, expressions):
    valueList = binaryNumberconverted(str(bin(index)), numberOfVariables)
    variableValueList = valueList
    for expression in expressions:
        valueList.append(calculate(expression, False, True, numberOfVariables, variableValueList))
    for i, element in enumerate(valueList):
        valueList[i] = element.stringValue()
    return valueList

def printTafel():
    numberOfVariables = int(input(">Gib die Anzahl der vorkommenden Variablen ein: "))
    outputString = ">Variablen: "
    for i  in range(numberOfVariables):
        if i < numberOfVariables - 1:
            outputString+=f"{chr(65 + i)}, "
        else:
            outputString+=f"{chr(65 + i)}"
    console.print(outputString)
    expressions = []
    console.print(">Gib beliebig viele Ausdrücke mit den oben genannten Variablen ein")
    console.print(">Gib s ein, wenn du keine Ausdrücke mehr eingeben möchtest")
    text = ""
    i = 0
    while text != "s":
        text = input(f">{i+1}. Ausdruck: ")
        if text != "s":
            expressions.append(text)
        i += 1
    list = []
    # import time
    # start = time.time()
    for j in range(2**numberOfVariables):
        list.append(row(j, numberOfVariables, expressions))
    columns = []
    for i in range(numberOfVariables):
        columns.append(chr(65 + i))
    for expression in expressions:
        columns.append(expression)
    # print(time.time() - start)
    # time.sleep(20)
    printTable(list, columns, "green", ["white"], "white")