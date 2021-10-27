from aussage import Aussage
from calculate import calculate
from my_console import console
from print_table import printTable

def row(index, numberOfVariables, expressions):
    valueList = []
    identifier = numberOfVariables - index
    if identifier > 0:
        for i in range(numberOfVariables):
            if i < identifier:
                valueList.append(Aussage("true"))
            else:
                valueList.append(Aussage("false"))  
    else:
        identifier += numberOfVariables   
        for i in range(numberOfVariables):
            if i < identifier:
                valueList.append(Aussage("false"))  
            else: 
                valueList.append(Aussage("true"))
    variableValueList = valueList
    for expression in expressions:
        valueList.append(calculate(expression, False, True, numberOfVariables, variableValueList))
    for i,element in enumerate(valueList):
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
    for i in range(numberOfVariables*2):
        list.append(row(i, numberOfVariables, expressions))
    columns = []
    for i in range(numberOfVariables):
        columns.append(chr(65 + i))
    for expression in expressions:
        columns.append(expression)
    printTable(list, columns, "green", ["white"], "white")