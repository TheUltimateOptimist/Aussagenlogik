from variables import Variables
from tafel import printTafel
from calculate import evaluate
from aussage import Aussage
from rich.text import Text
from console import console
from language import erklaerung, befehle


def interpret(text: str):
    """
    interprets the given text
    :parameter text: text to interpret
    """

    # TODO: If we'd use Python 3.10+ we could use switch case statements here

    if text == "erkläre":
        console.print(Text("\n".join(erklaerung.split("-n-")), "bold cyan"))
    elif text == "befehle":
        console.print(Text("\n".join(befehle.split("-n-")), "bold magenta"))
    elif text == "tafel":
        printTafel()
    elif text == "binär":
        Aussage.wertDarstellung = text
    elif text == "wf":
        Aussage.wertDarstellung = text
    elif text == "truefalse":
        Aussage.wertDarstellung = text
    elif "=" in text:
        Variables.add(text.split("=")[0].strip(), evaluate(text.split("=")[1].strip()))
    else:
        evaluate(text, True)


def mainLoop():
    """
    program main loop:
        - asks for input and evaluates it in a loop
        - exits when KeyboardInterrupt occurred (ctrl+c) or input was like "exit"
    """

    canceled = False
    operation = ""
    while not canceled:
        try:
            operation = input(">: ").strip()
            if operation.lower() == "exit":
                canceled = True
            else:
                interpret(operation)
        except KeyboardInterrupt:
            canceled = True
        except Exception as exception:
            console.print(Text("Ungültige Eingabe ('" + operation + "') -> '" + str(exception) + "'", "bold red"))


def welcomeUser():
    """
    prints the welcome message and some basic usage information
    """
    console.print("Version 1.0.2")
    console.print("created by Jonathan Dück")
    console.print("contributers: Leon Gierschner")  # :D
    link = Text("https://github.com/TheUltimateOptimist/Aussagenlogik", "underline")
    console.print(Text("Source Code: ").append(link))
    console.print(Text("Willkommen!", "bold green"))
    console.print(Text("Um zu erfahren wie dieses Tool funktioniert, gib 'erkläre' ein, und drücke Enter!", "bold green"))
    console.print(Text("Um alle Befehle anzeigen zu lassen, gib 'befehle' ein, und drücke Enter!", "bold green"))


if __name__ == '__main__':
    welcomeUser()
    mainLoop()
