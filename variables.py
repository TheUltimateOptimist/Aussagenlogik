from __future__ import annotations
from typing import Any
from expression import Expression


class Variables:
    """
    designated singleton class for storing variables:
        - holds variable names
        - and variable values
    """

    __instance: Variables = None
    names: list[str] = []
    values: list[Any] = []

    def __init__(self):
        if Variables.__instance is not None:
            raise Exception("This class is a singleton!")
        self.names = []
        self.values = []

    @staticmethod
    def get_instance():
        if Variables.__instance is None:
            Variables.__instance = Variables()
        return Variables.__instance

    def add(self, name: str, value: Any) -> None:
        """
        adds a variable to the storage
        :param name: the variable name
        :param value: the variable value
        """

        if self.contains(name):
            for i, variable in enumerate(self.names):
                if variable == name:
                    self.values[i] = value
        else:
            self.names.append(name)
            self.values.append(value)

    def remove(self, name: str) -> None:
        """
        removes a variable by its name
        :param name: the name of the variable to remove
        """

        for i, variable in enumerate(self.names):
            if variable == name:
                del self.names[i]
                del self.values[i]
                break

    def contains(self, name: str) -> bool:
        """
        whether or not there is a variable with given name
        :param name: the name of the variable to check for existence
        """

        for variable in self.names:
            if variable == name:
                return True
        return False

    def get_value(self, name: str) -> Expression | None:
        """
        get the value of the variable with the given name
        :param name: the name of the variable to get the value from
        :returns: the value of the variable
        """

        for i, variable in enumerate(self.names):
            if variable == name:
                return self.values[i]
        return None
