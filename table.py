from __future__ import annotations
from typing import Any
from termcolor import colored
from colorama import init
from expression import Expression
from globals import console
from interpreter import Interpreter


class Table:

    @staticmethod
    def to_string_list(dimensions: int, input_list: list[Any | list[Any]]) -> list[str | list[str]]:
        """
        converts list to a list of string
        :param dimensions: number of dimensions of list
        :param input_list: the list to convert to a list of strings
        :returns: the converted list of strings
        """

        result_list = []
        if dimensions == 1:
            for element in input_list:
                result_list.append(str(element))
        elif dimensions == 2:
            for row in input_list:
                rowList = []
                for element in row:
                    rowList.append(str(element))
                result_list.append(rowList)
        return result_list

    @staticmethod
    def binary_number_converted(binary_string: str, number_of_variables: int) -> list[Expression]:
        """
        converts the binary number to a sequence of true / false values to create a list of expressions
        :param binary_string: the binary string representation of a sequence of true / false values
        :param number_of_variables: the total number of expressions to generate (missing leading zeros will be filled
               autom.)
        :returns: a list of expressions generated from the binary string
        """

        binary_string = binary_string.split("b")[1]
        length = len(binary_string)
        if length < number_of_variables:
            binary_string = (number_of_variables - length) * "0" + binary_string
        resultList = []
        for element in binary_string:
            resultList.append(Expression(element))
        return resultList

    @staticmethod
    def print_table():
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
        table_elements = []
        for j in range(2 ** numberOfVariables):
            table_elements.append(Table.__row(j, numberOfVariables, expressions))
        columns = []
        for i in range(numberOfVariables):
            columns.append(chr(65 + i))
        for expression in expressions:
            columns.append(expression)
        Table.__print_table(table_elements, columns, "green", ["white"], "white")

    @staticmethod
    def __row(index: int, number_of_variables: int, expressions: list[str]) -> list[str | Expression]:
        """
        evaluates the expressions for the given row
        :param index: the index of the row to evaluate the entries for
        :param number_of_variables: the total number of variables used
        :param expressions: the expressions to evaluate
        :returns: the resulting row as a list of strings
        """

        value_list = Table.binary_number_converted(str(bin(index)), number_of_variables)
        variableValueList = value_list
        for expression in expressions:
            value_list.append(Interpreter.evaluate(expression, False, True, number_of_variables, variableValueList))
        for i, element in enumerate(value_list):
            # noinspection PyTypeChecker
            value_list[i] = element.to_str()
        return value_list

    @staticmethod
    def __print_table(table: list[list[str]], column_names: list[str], column_names_color: str,
                      entry_colors: list[str],
                      surrounding_color: str, show_indices: bool = False):
        """
        prints table to the console using the given options
        :param table: the table to print to the console
        :param column_names: the names for the columns of table (for the header row)
        :param column_names_color: color for the column names
        :param entry_colors: color for entry values of the table
        :param surrounding_color: color of the table grid
        :param show_indices: adds indices to the table
        """

        if len(entry_colors) == 1:
            for i in range(len(table) - 1):
                entry_colors.append(entry_colors[0])
        # table = toStringList(2, table)
        if show_indices:
            column_names.reverse()
            column_names.append("")
            column_names.reverse()
            i = 1
            for row in table:
                row.reverse()
                row.append(str(i))
                row.reverse()
                i = i + 1
        init()
        # calculate max Lengths:
        max_lengths = []
        for i in range(len(column_names)):
            maxLength = len(column_names[i])
            for j in range(len(table)):
                if len(table[j][i]) > maxLength:
                    maxLength = len(table[j][i])
            max_lengths.append(maxLength + 1)

        # print table
        # print top Bar
        top_bar = "+"
        for length in max_lengths:
            top_bar = top_bar + length * "-" + "-+"
        print(colored(top_bar, surrounding_color))

        # print column names
        s = colored("| ", surrounding_color)
        i = 0
        for element in column_names:
            s = s + (f"{colored(element, column_names_color)}" +
                     (max_lengths[i] - len(element)) * " " + colored("| ", surrounding_color))
            i = i + 1
        print(s)

        # print bottomBar
        print(colored(top_bar, surrounding_color))

        # print entries
        for i in range(len(table)):
            entry = colored("| ", surrounding_color)
            for j in range(len(column_names)):
                entry = entry + colored(table[i][j], entry_colors[i]) + (
                        max_lengths[j] - len(table[i][j])) * " " + colored("| ", surrounding_color)
            print(entry)

        # print end bar
        print(colored(top_bar, surrounding_color))
