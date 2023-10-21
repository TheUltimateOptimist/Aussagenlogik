from rich.text import Text
from globals import console


class UserInterface:

    @classmethod
    def main_loop(cls):
        """
        program main loop:
            - asks for input and evaluates it in a loop
            - exits when KeyboardInterrupt occurred (ctrl+c) or input was like "exit"
        """

        canceled = False
        while not canceled:
            try:
                operation = input(">: ").strip()
                if operation.lower() == "exit":
                    canceled = True
                else:
                    UserInterface.interpret(operation)
            except KeyboardInterrupt:
                canceled = True
            except Exception as exception:
               console.print(Text("Ungültige Eingabe '" + operation + "'" , "bold red"))

    @classmethod
    def welcome_user(cls):
        """
        prints the welcome message and some basic usage information
        """
        console.print("Version 1.0.3")
        console.print("created by Jonathan Dück")
        console.print("contributors: Leon Gierschner")  # :D
        link = Text("https://github.com/TheUltimateOptimist/Aussagenlogik", "underline")
        console.print(Text("Source Code: ").append(link))
        console.print(Text("Willkommen!", "bold green"))
        console.print(
            Text("Um zu erfahren wie dieses Tool funktioniert, gib 'erkläre' ein, und drücke Enter!", "bold green"))
        console.print(Text("Um alle Befehle anzeigen zu lassen, gib 'befehle' ein, und drücke Enter!", "bold green"))

    @classmethod
    def interpret(cls, text: str):
        """
        interprets the given text
        :parameter text: text to interpret
        """

        from table import Table
        from variables import Variables
        from interpreter import Interpreter
        from expression import Expression
        from language import descriptions, commands
        from view_type import ViewType

        # TODO: If we'd use Python 3.10+ we could use switch case statements here

        if text == "erkläre":
            console.print(Text("\n".join(descriptions.split("-n-")), "bold cyan"))
        elif text == "befehle":
            console.print(Text("\n".join(commands.split("-n-")), "bold magenta"))
        elif text == "tafel":
            Table.print_table()
        elif text in ["binär", "wf", "truefalse"]:
            Expression.view_type = ViewType.from_str(text)
        elif "=" in text:
            name = text.split("=")[0].strip()
            Variables.get_instance().add(name, Interpreter.evaluate(text.split("=")[1].strip()))
            console.print(Text(Variables.get_instance().get_value(name).to_str(), "bold green"))
        else:
            Interpreter.evaluate(text, True)
