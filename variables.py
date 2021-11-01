from __future__ import annotations
from typing import Any


# TODO: singleton pattern or static storage -> there are pretty nice annotation implementations out there

class Variables:
    """
    designated class for storing variables:
        - holds variable names
        - and variable values
    """

    names: list[str] = []
    values: list[Any] = []

    @classmethod
    def add(cls, name: str, value: Any) -> None:
        """
        adds a variable to the storage
        :param name: the variable name
        :param value: the variable value
        """

        if cls.contains(name):
            for i, variable in enumerate(cls.names):
                if variable == name:
                    cls.values[i] = value
        else:
            cls.names.append(name)
            cls.values.append(value)

    @classmethod
    def remove(cls, name: str) -> None:
        """
        removes a variable by its name
        :param name: the name of the variable to remove
        """

        for i, variable in enumerate(cls.names):
            if variable == name:
                del cls.names[i]
                del cls.values[i]
                break

    @classmethod
    def contains(cls, name: str) -> bool:
        """
        whether or not there is a variable with given name
        :param name: the name of the variable to check for existence
        """

        for variable in cls.names:
            if variable == name:
                return True
        return False

    @classmethod
    def getValue(cls, name: str) -> Any | None:
        """
        get the value of the variable with the given name
        :param name: the name of the variable to get the value from
        :returns: the value of the variable
        """

        for i, variable in enumerate(cls.names):
            if variable == name:
                return cls.values[i]
        return None
