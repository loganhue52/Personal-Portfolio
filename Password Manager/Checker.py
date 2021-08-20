class Checker:
    def __init__(self,password):
        self.cL=[False,False,False,False,False]
        self.password=password

    def check(self):
        #mostly pieces from the original strength checker assignment
        for i in self.password:
            if ord(i) in range(97,123):
                self.cL[0] = True
            if ord(i) in range(65,91):
                self.cL[1] = True
            if i.isdigit() == True:
                self.cL[2] = True
            if i == "!" \
            or i == "@" \
            or i == "#" \
            or i == "$" \
            or i == "%" \
            or i == "^" \
            or i == "&" \
            or i == "(" \
            or i == ")":
                self.cL[3] = True
            
        if (len(self.password) >= 8):
            self.cL[4] = True
        
        if False in self.cL:
            return False
        else:
            return True