from variables import Variables
from tafel import printTafel
from calculate import calculate
from aussage import Aussage
from rich.text import Text
from my_console import console
def erklaere():
    with open("erklaerung.txt", mode="r", encoding="utf8") as file:
        console.print(Text("".join(file.readlines()), "bold rgb(255,253,208)"))

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
    evaluateInput(operation.strip())
    main()

def welcomeUser():
    console.print("created by Jonthan Dück")
    link = Text("https://github.com/TheUltimateOptimist/Matrizen", "underline")
    console.print(Text("Source Code: ").append(link))
    console.print(Text("Wilkommen!", "bold green"))
    console.print(Text("Um zu erfahren wie dieses Tool funktioniert, gib 'erkläre' ein, und drücke Enter!", "bold green"))

if __name__ == '__main__':
    welcomeUser()
    main()