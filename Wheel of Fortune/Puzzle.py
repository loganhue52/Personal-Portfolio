class Puzzle:
    def __init__(self,currentpuzzle):
        self.p=currentpuzzle
        self.listy=[]
        self.output=""

    #from logans hangman code
    #replaces letters with a _ then adds space in between
    def makePuzzle(self):
        for i in range(len(self.p)):
            if self.p[i]!=" ":
                self.listy.append("_")
            else:
                self.listy.append(" ")
        for i in self.listy:
            self.output += i
            self.output += " "
        return self.output

    #for printing the puzzle to the console
    def __str__(self):
        self.output=""
        for i in self.listy:
            self.output += i
            self.output += " "
        return self.output  

    #replaces _ with the letter put into it
    def replace(self,uI):
        self.output = ""
        if uI.lower() in self.p.lower():
            for i in range(len(self.p)):
                if self.p[i].lower() == uI.lower():
                    self.listy[i] = self.p[i]
            for i in self.listy:
                self.output += i
                self.output += " "
            return self.output
        else:
            return None

    #for checking if the puzzle is completed
    def iscomplete(self):
        if "_" not in self.output:
            return True
        else: 
            return False