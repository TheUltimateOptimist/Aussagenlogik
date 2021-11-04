from __future__ import annotations
from typing import Any
from termcolor import colored
from colorama import init


def toStringList(dimensions: int, inputList: list[Any | list[Any]]) -> list[str | list[str]]:
    """
    converts list to a list of string
    :param dimensions: number of dimensions of list
    :param inputList: the list to convert to a list of strings
    :returns: the converted list of strings
    """

    resultList = []
    if dimensions == 1:
        for l in inputList:
            resultList.append(str(l))
    elif dimensions == 2:
        for row in inputList:
            rowList = []
            for element in row:
                rowList.append(str(element))
            resultList.append(rowList)
    return resultList


def printTable(table: list[list[str]], columnNames: list[str], columnNamesColor: str, entryColors: list[str], surroundingColor: str, showIndexes: bool = False):
    """
    prints table to the console using the given options
    :param table: the table to print to the console
    :param columnNames: the names for the columns of table (for the header row)
    :param columnNamesColor: color for the column names
    :param entryColors: color for entry values of the table
    :param surroundingColor: color of the table grid
    :param showIndexes: adds indices to the table
    """

    if len(entryColors) == 1:
        for i in range(len(table) - 1):
            entryColors.append(entryColors[0])
    #table = toStringList(2, table)
    if showIndexes == True:
        columnNames.reverse()
        columnNames.append("")
        columnNames.reverse()
        i = 1
        for row in table:
            row.reverse()
            row.append(str(i))
            row.reverse()
            i = i + 1
    init()
    # calculate max Lengths:
    maxLengths = []
    for i in range(len(columnNames)):
        maxLength = len(columnNames[i])
        for j in range(len(table)):
            if len(table[j][i]) > maxLength:
                maxLength = len(table[j][i])
        maxLengths.append(maxLength + 1)

    # print table
    # print top Bar
    topBar = "+"
    for l in maxLengths:
        topBar = topBar + l*"-" + "-+"
    print(colored(topBar, surroundingColor))

    # print column names
    s = colored("| ", surroundingColor)
    i = 0
    for element in columnNames:
        s = s + (f"{colored(element, columnNamesColor)}" +
                 (maxLengths[i] - len(element))*" " + colored("| ", surroundingColor))
        i = i + 1
    print(s)

    # print bottomBar
    print(colored(topBar, surroundingColor))

    # print entries
    for i in range(len(table)):
        entry = colored("| ", surroundingColor)
        for j in range(len(columnNames)):
            entry = entry + colored(table[i][j], entryColors[i]) + (
                maxLengths[j] - len(table[i][j]))*" " + colored("| ", surroundingColor)
        print(entry)

    # print end bar
    print(colored(topBar, surroundingColor))

