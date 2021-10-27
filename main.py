from variables import Variables
from tafel import printTafel
from calculate import calculate
from aussage import Aussage
from rich.text import Text
from my_console import console
from language import erklaerung
def erklaere():
    console.print(Text("\n".join(erklaerung.split("-n-")), "bold cyan"))

def evaluateInput(text):
    if text == "erkläre":
        erklaere()
    elif text == "tafel":
        printTafel()
    elif text == "binär":
        Aussage.wertDarstellung = text
    elif text == "wf":
        Aussage.wertDarstellung = text
    elif text == "truefalse":
        Aussage.wertDarstellung = text    
    elif text.__contains__("="):
        Variables.add(text.split("=")[0].strip(), calculate(text.split("=")[1].strip())) 
    else:
        calculate(text, True)    

def main():
    operation = input(">: ")
    try:
        evaluateInput(operation.strip())
    except:
        console.print(Text("Ungültige Eingabe", "bold red"))
    main()

def welcomeUser():
    console.print("created by Jonthan Dück")
    link = Text("https://github.com/TheUltimateOptimist/Aussagenlogik", "underline")
    console.print(Text("Source Code: ").append(link))
    console.print(Text("Wilkommen!", "bold green"))
    console.print(Text("Um zu erfahren wie dieses Tool funktioniert, gib 'erkläre' ein, und drücke Enter!", "bold green"))

if __name__ == '__main__':
    welcomeUser()
    main()