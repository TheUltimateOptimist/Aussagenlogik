from __future__ import annotations
from view_type import ViewType


class Expression:
    """
    representation for an expression with support for various operators
    """

    view_type: ViewType = ViewType.from_str("binary")
    value: bool = False

    def __init__(self, value: str | bool):
        """
        creates an object of type Expression
        :parameter value: the value this expression evaluates to (either "w" / "f" or "1" / "0" or
                          "true" / "false" or true / false
        """

        if type(value) is bool and value:
            self.value = value
        elif type(value) is bool and not value:
            self.value = False
        elif value == "true":
            self.value = True
        elif value == "false":
            self.value = False
        elif value == "1":
            self.value = True
        elif value == "0":
            self.value = False
        elif value == "w":
            self.value = True
        elif value == "f":
            self.value = False
        else:
            print(f"ERROR: DER WERT {value} ist für eine Aussage nicht zulässig! "
                  f"Zulässig sind: 0, f, false, 1, w, true")

    def not_(self) -> Expression:
        """
        evaluates the 'nicht Expression' operation
        :returns: the result of 'nicht Expression'
        """

        return Expression(not self.value)

    def and_(self, other: Expression) -> Expression:
        """
        evaluates the 'Expression und Expression' operation
        :returns: the result of 'Expression und Expression'
        """

        return Expression(self.value and other.value)

    def or_(self, other: Expression) -> Expression:
        """
        evaluates the 'Expression oder Expression' operation
        :returns: the result of 'Expression oder Expression'
        """

        return Expression(self.value or other.value)

    def xor_(self, other: Expression) -> Expression:
        """
        evaluates the 'Expression xor Expression' operation
        :returns: the result of 'Expression xor Expression'
        """
        return Expression(self.value != other.value)

    def implies_(self, other: Expression) -> Expression:
        """
        evaluates the 'Expression folgt Expression' operation
        :returns: the result of 'Expression folgt Expression'
        """

        return Expression(not self.value or other.value)

    def to_str(self) -> str:
        """
        creates a string representation:
            -> uses the value of view_type to create the string
        :returns: the corresponding string representation
        :raises ValueError: if view_type is neither BINARY nor WAHR_FALSCH nor TRUE_FALSE
        """

        if self.value and self.view_type == ViewType.BINARY:
            return "1"
        elif not self.value and self.view_type == ViewType.BINARY:
            return "0"
        elif self.value and self.view_type == ViewType.WAHR_FALSCH:
            return "w"
        elif not self.value and self.view_type == ViewType.WAHR_FALSCH:
            return "f"
        elif self.value and self.view_type == ViewType.TRUE_FALSE:
            return "true"
        elif not self.value and self.view_type == ViewType.TRUE_FALSE:
            return "false"
        else:
            raise ValueError
