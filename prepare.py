def main():
    file = input("enter file name: ")
    with open(file, mode="r") as startFile:
        with open("solution.txt", mode="w") as solutionFile:
            text = "-n-".join("".join(startFile.readlines()).split("\n"))
            solutionFile.write(f"'{text}'")


if __name__ == '__main__':
    main()