
def main():
    fileName = readFile()
    big_dict = createDict(fileName)
    getGoTerms(big_dict)


def readFile():
    fileName = "resultaten bestand.txt"
    return fileName


def createDict(fileName):
    file = open(fileName)
    big_dict = {}
    for line in file:
        if not line == "\n":
            line = line.split(":")
            big_dict[line[0]] = line[1]
    return big_dict


def getGoTerms(big_dict):
    goTermsList = []
    for i in big_dict:
        big_dict[i] = big_dict[i].split(",")
        for function in big_dict[i]:
            if function not in goTermsList:
                goTermsList.append(function)
    print(goTermsList)


main()