from __future__ import annotations
from rich.text import Text
from expression import Expression
from extended_list import ExtendedList
from globals import console
from tokenizer import Tokenizer


class Interpreter:

    @staticmethod
    def evaluate_token_list(token_list: list[str | Expression]) -> Expression:
        """
        evaluates the given list of tokens
        :parameter token_list: a list of tokens from the tokenizer to evaluate
        :returns: the value the token list evaluates to
        """
        print(token_list)
        i = 0
        while i < len(token_list):
            token = token_list[i]
            if token == "(":
                closing_brace_index = ExtendedList(token_list).get_closing_brace_index(i)
                token_list[i] = Interpreter.evaluate_token_list(token_list[i + 1: closing_brace_index])
                for _ in range(closing_brace_index - i):
                    del token_list[i + 1]
            i += 1
        i = 0
        while i < len(token_list):
            token = token_list[i]
            if str(token.__class__) == "<class 'str'>" and token == "nicht":
                token_list[i] = token_list[i + 1].not_()
                del token_list[i + 1]
            elif str(token.__class__) == "<class 'str'>" and token == "und":
                token_list[i] = token_list[i - 1].and_(token_list[i + 1])
                del token_list[i + 1]
                del token_list[i - 1]
            elif str(token.__class__) == "<class 'str'>" and token == "oder":
                token_list[i] = token_list[i - 1].or_(token_list[i + 1])
                del token_list[i + 1]
                del token_list[i - 1]
            elif str(token.__class__) == "<class 'str'>" and token == "xor":
                token_list[i] = token_list[i - 1].xor_(token_list[i + 1])
                del token_list[i + 1]
                del token_list[i - 1]
            elif str(token.__class__) == "<class 'str'>" and token == "folgt":
                token_list[i] = token_list[i - 1].implies_(token_list[i + 1])
                del token_list[i + 1]
                del token_list[i - 1]
            else:
                i += 1
        return token_list[0]

    @staticmethod
    def evaluate(expression: str, should_print: bool = False, tafel: bool = False,
                 number_of_variables: int = 0, expressions: list = None) -> Expression:
        """
        takes an expression and evaluates the result
        :parameter expression: the expression to evaluate
        :parameter should_print: whether or not to print the value to the console
        :parameter tafel: whether or not to use the values of numberOfVariables and aussagenObjects
        :parameter number_of_variables: the number of variables to create
        :parameter expressions: pre-filled list of expression-objects
        :returns: the evaluated result
        """

        if expressions is None:
            expressions = []

        if tafel:
            result = Interpreter.evaluate_token_list(Tokenizer(expression, True, number_of_variables,
                                                               expressions).tokenize())
        else:
            result = Interpreter.evaluate_token_list(Tokenizer(expression).tokenize())
        if should_print:
            console.print(Text(result.to_str(), "bold green"))
        return result
