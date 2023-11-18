from typing import Any
from expression import Expression
from language import operations, values
from variables import Variables
from extended_list import ExtendedList


class Tokenizer:
    """
    generates a sequence of tokens using an input string
    """

    def __init__(self, expression: str, table: bool = False, number_of_variables: int = 0, expressions: list = None):
        """
        creates an object of type Tokenizer
        :param expression: the expression to parse
        :param table: TODO ?!
        :param number_of_variables: the number of variables that could exist in the expression
        :param expressions: TODO ?!
        """

        if expressions is None:
            expressions = []

        self.number_of_variables = number_of_variables
        self.expression_objects = expressions
        self.expression = expression
        self.table = table
        if not table:
            self.words = operations + values + Variables.get_instance().names
        else:
            self.words = operations + values + [chr(65 + i) for i in range(number_of_variables)]

    def tokenize(self):
        """
        tokenizes the input string
        :returns: the corresponding list of tokens
        """
        result = []
        word = ""
        for i in range(len(self.expression)):
            if self.__is_contained_in_word(word + self.expression[i]):
                if self.__is_word(word + self.expression[i]) and self.__next_symbol_not_a_letter(i, self.expression):
                    result.append(word + self.expression[i])
                    word = ""
                else:
                    word = word + self.expression[i]
            elif self.expression[i] == "(" or self.expression[i] == ")":
                result.append(self.expression[i])
                word = ""
            else:
                word = ""
        result = self.__embrace_not_tokens(result)
        return self.__dissolve_variables(result)

    def __is_word(self, text_string: str) -> bool:
        """
        whether or not textString is an existing word-symbol in this language
        :param text_string: the text to check for symbolness :D
        :returns: true if the text represents an existing word-symbol in this language, false otherwise
        """

        for word in self.words:
            if word == text_string:
                return True
        return False

    def __is_contained_in_word(self, text_string: str) -> bool:
        """
        whether or not textString could be any predefined word-symbol
        :param text_string: the text to check for 'could-be-predefinedness' xD
        :returns: true if the text could be a predefined word-symbol, false otherwise
        """

        for word in self.words:
            if text_string in word:
                return True
        return False

    @staticmethod
    def __next_symbol_not_a_letter(current_index: int, text: str) -> bool:
        """
        whether or not the next symbol doesn't exist or would not be a letter
        :param current_index: the current index to deduce the next index from
        :param text: the text where to look for the next symbol
        :returns: true if the text is not long enough or next symbol is not a letter, false otherwise
        """

        if len(text) == current_index + 1:
            return True

        code = ord(text[current_index + 1])
        if (code < 65 or code > 90) and (code < 97 or code > 122):
            return True
        else:
            return False

    @staticmethod
    def __is_value(element: Any) -> bool:
        """
        whether or not the element represents a valid value-symbol in this language
        :param element: any element to check
        :returns: True if elements class is str and represents a valid value-symbol in this language, false otherwise
        """

        for value in values:
            if type(element) is str and value == element:
                return True
        return False

    def __dissolve_variables(self, tokens: list) -> list:
        """
        replaces all variables with its values
        :param tokens: where to replace all variables with its values
        :returns: the list with all variables replaced
        """
        for i, token in enumerate(tokens):
            if self.__is_value(token):
                tokens[i] = Expression(token)
        if not self.table:
            for i, token in enumerate(tokens):
                if type(token) is not Expression and Variables.get_instance().contains(token):
                    tokens[i] = Variables.get_instance().get_value(token)
            return tokens
        else:
            for i, token in enumerate(tokens):
                if type(token) is not Expression and len(token) == 1:
                    code = ord(token)
                    if 65 <= code <= 64 + self.number_of_variables:
                        tokens[i] = self.expression_objects[code - 65]
            return tokens

    @staticmethod
    def __embrace_not_tokens(tokens: list) -> list:
        """
        embraces all tokens that corresponds to a 'Nicht'-token
        :param tokens: the list of tokens where to work on
        :returns: the modified list
        """
        for i, element in enumerate(tokens):
            if element == "nicht" and tokens[i + 1] == "nicht":
                del tokens[i + 1]
                del tokens[i]
        for i, element in enumerate(tokens):
            if (element == "nicht" and i == 0) or (element == "nicht" and tokens[i - 1] != "("):
                closing_brace_index = i + 2
                if tokens[i + 1] == "(":
                    closing_brace_index = ExtendedList(tokens).get_closing_brace_index(i + 1) + 1
                if closing_brace_index < len(tokens) - 1:
                    tokens.insert(closing_brace_index, ")")
                else:
                    tokens.append(")")
                tokens.insert(i, "(")
        return tokens
