from __future__ import annotations


class Aussage:
    """
    representation for an expression with support for various operators
    """

    wertDarstellung: str = "binär"

    def __init__(self, value: str | bool):
        """
        creates an object of type Aussage
        :parameter value: the value this expression evaluates to (either "w" / "f" or "1" / "0" or
                          "true" / "false" or true / false
        """

        if value == True:
            self.value = value
        elif value == False:
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

    def nicht(self) -> Aussage:
        """
        evaluates the 'nicht Aussage' operation
        :returns: the result of 'nicht Aussage'
        """

        if self.value:
            return Aussage(False)
        else:
            return Aussage(True)

    def und(self, aussageB: Aussage) -> Aussage:
        if self.value and aussageB.value:
            return Aussage(True)
        else:
            return Aussage(False)

    def oder(self, aussageB: Aussage) -> Aussage:
        """
        evaluates the 'Aussage oder Aussage' operation
        :returns: the result of 'Aussage oder Aussage'
        """

        if self.value or aussageB.value:
            return Aussage(True)
        else:
            return Aussage(False)

    def xor(self, aussageB: Aussage) -> Aussage:
        """
        evaluates the 'Aussage xor Aussage' operation
        :returns: the result of 'Aussage xor Aussage'
        """

        if (self.value and not aussageB.value) or (aussageB.value and not self.value):
            return Aussage(True)
        else:
            return Aussage(False)

    def folgt(self, aussageB: Aussage) -> Aussage:
        """
        evaluates the 'Aussage folgt Aussage' operation
        :returns: the result of 'Aussage folgt Aussage'
        """

        if self.value and not aussageB.value:
            return Aussage(False)
        else:
            return Aussage(True)

    def stringValue(self) -> str:
        """
        creates a string representation:
            -> uses the value of wertDarstellung to create the string
        :returns: the corresponding string representation
        :raises ValueError: if wertDarstellung is neither "binär" nor "wf" nor "truefalse"
        """

        if self.value and self.wertDarstellung == "binär":
            return "1"
        elif not self.value and self.wertDarstellung == "binär":
            return "0"
        elif self.value and self.wertDarstellung == "wf":
            return "w"
        elif not self.value and self.wertDarstellung == "wf":
            return "f"
        elif self.value and self.wertDarstellung == "truefalse":
            return "true"
        elif not self.value and self.wertDarstellung == "truefalse":
            return "false"
        else:
            raise ValueError
