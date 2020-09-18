# C posthuma , september 2019
# sep 2020: renamed functions, added doc strings, made it a class
# script to scrape GO terms

class getGoTerms():

    def __init__(self):
        super().__init__()

        self.fileName = "resultaten bestand.txt"
        self.big_dict = self.createDict()
        print(self.getGoTerms())


    def createDict(self):
        # opens file, creates a dictionary with all results
        # returns that dictionary
        file = open(self.fileName)
        big_dict = {}
        for line in file:
            if not line == "\n":
                line = line.split(":")
                big_dict[line[0]] = line[1]
        return big_dict


    def getGoTerms(self):
        # creates a list with all GO terms
        goTermsList = []
        for i in self.big_dict:
            self.big_dict[i] = self.big_dict[i].split(",")
            for function in self.big_dict[i]:
                if function not in goTermsList:
                    goTermsList.append(function)
        return goTermsList


main = getGoTerms()