from enum import Enum


class ViewType(Enum):
    BINARY = 0
    WAHR_FALSCH = 1
    TRUE_FALSE = 2

    @classmethod
    def from_str(cls, text: str):
        if text == "binär" or text == "binary":
            return ViewType.BINARY
        elif text == "wf" or text == "wahrfalsch":
            return ViewType.WAHR_FALSCH
        else:
            return ViewType.TRUE_FALSE
