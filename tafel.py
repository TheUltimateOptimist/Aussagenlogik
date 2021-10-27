from aussage import Aussage
from calculate import calculate
from my_console import console

def addRowStatement(index, numberOfVariables, expressions):
    valueList = []
    identifier = numberOfVariables - index
    if identifier > 0:
        for i in range(numberOfVariables):
            if i < identifier:
                valueList.append(Aussage(True))
            else:
                valueList.append(Aussage(False))  
    else:
        identifier += numberOfVariables   
        for i in range(numberOfVariables):
            if i < identifier:
                valueList.append(Aussage(False))  
            else: 
                valueList.append(Aussage(True))
    variableValueList = valueList
    for expression in expressions:
        valueList.append(calculate(expression, False, True, numberOfVariables, variableValueList))
    additionLine = "table.add_row("
    for element in valueList:
        additionLine+=f"'{element.stringValue()}', "
    additionLine+=")\n"       
    return additionLine

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
    with open("printTable.py", mode="w") as file:
        file.write("from rich.table import Table\nfrom my_console import console\n\ntable = Table(header_style='bold green')\n")
    with open("printTable.py", "a") as file:
        for i in range(numberOfVariables):
            file.write(f"table.add_column(chr({65 + i}))\n")
        for expression in expressions:
            file.write(f"table.add_column('{expression}')\n")
        for i in range(2*numberOfVariables):
            file.write(addRowStatement(i, numberOfVariables, expressions))
        file.write("console = Console()\n")
        file.write("console.print(table)\n")
    import printTable
    import importlib
    importlib.reload(printTable)