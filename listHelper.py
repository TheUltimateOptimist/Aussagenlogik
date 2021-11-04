# index 1 and index 2 identify the part of the list that will be split of of the main list and returned
from __future__ import annotations

from aussage import Aussage


def split_list(index1: int, index2: int, list: list) -> list:
    """
    gives everything from list between index1 and index2
    :param index1: index of first item to take
    :param index2: index of last item to take
    :param list: the list for this operation
    :returns: everything from list between (and including) index1 and index2
    """
    finalList = []
    for i in range(index1, index2 + 1):
        finalList.append(list[i])
    return finalList


def delete_range(index1, index2, list):
    """
    deletes everything from list between index1 and index2
    :param index1: index of first item to delete
    :param index2: index of last item to delete
    :param list: the list for this operation
    :returns: everything from list except all elements between index1 and index2
    """
    n = index2 - index1 + 1
    for _ in range(n):
        list.pop(index1)
    return list


def getClosingBraceIndex(openingBraceIndex: int, list: list[str | Aussage]) -> int:
    """
    searches for the corresponding closing brace
    :raises SyntaxError: if closing brace could not be found in list
    :param openingBraceIndex: the index of the open brace to search the closing one for
    :param list: the list of tokens to search through
    :returns: the index for the corresponding closing brace
    """

    state = 0
    i = openingBraceIndex + 1
    while i < len(list):
        element = list[i]
        if element == "(":
            state += 1
        elif element == ")" and state != 0:
            state -= 1
        elif element == ")" and state == 0:
            return i
        i += 1
    raise SyntaxError("schließende Klammer nicht gefunden!")
