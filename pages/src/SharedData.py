class SharedData:
    prpListCase1 = []
    tpListCase1 = []
    
    # Get
    def getprpListCase1(self):
        return self.prpListCase1
    
    def getTpListCase1(self):
        return self.tpListCase1
    
    # Set
    def setprpListCase1(self, prpList):
        self.prpListCase1 = prpList.copy()
    
    def setTpListCase1(self, tpList):
        self.tpListCase1 = tpList.copy()
        