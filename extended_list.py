from __future__ import annotations


class ExtendedList(list):

    def get_closing_brace_index(self, opening_index: int) -> int:
        """
        searches for the corresponding closing brace
        :param self: the list to work on
        :raises SyntaxError: if closing brace could not be found in list
        :param opening_index: the index of the open brace to search the closing one for
        :returns: the index for the corresponding closing brace
        """

        state = 0
        i = opening_index + 1
        while i < len(self):
            element = self[i]
            if element == "(":
                state += 1
            elif element == ")" and state != 0:
                state -= 1
            elif element == ")" and state == 0:
                return i
            i += 1

        raise SyntaxError("schließende Klammer nicht gefunden!")
