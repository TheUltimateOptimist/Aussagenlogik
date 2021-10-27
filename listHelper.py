# index 1 and index 2 identify the part of the list that will be split of of the main list and returned
def split_list(index1, index2, list):
    finalList = []
    for i in range(index1, index2 + 1):
        finalList.append(list[i])
    return finalList


def delete_range(index1, index2, list):
    n = index2 - index1 + 1
    for _ in range(n):
        list.pop(index1)
    return list

def getClosingBraceIndex(openingBraceIndex, list):
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