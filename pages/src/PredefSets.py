from itertools import chain, combinations

class PredefSets:
    ################
    # Case 1
    ################
    spacePrpCase1 = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    customer1PrpCase1 = ['Basic service', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    customer2PrpCase1 = ['Basic service', 'Service operation and security', 'Additional service/feature']
    managerPrpCase1 = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    peer1PrpCase1 = ['Basic service', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    peer2PrpCase1 = ['Basic service', 'Analytics/Research', 'Legal requirement']
    peer3PrpCase1 = ['Basic service', 'Service operation and security']
    
    spaceTPCase1 = ['Newsletter/Marketing', 'Project/Task management', 'Web analytics', 'Virtual meetings/events', 'Cloud computing service']
    customer1TPCase1 = ['Newsletter/Marketing', 'Project/Task management', 'Cloud computing service']
    customer2TPCase1 = ['Newsletter/Marketing', 'Virtual meetings/events', 'Cloud computing service']
    managerTPCase1 = ['Project/Task management', 'Web analytics', 'Virtual meetings/events', 'Cloud computing service']
    peer1TPCase1 = ['Virtual meetings/events', 'Cloud computing service']
    peer2TPCase1 = ['Newsletter/Marketing', 'Project/Task management', 'Web analytics']
    peer3TPCase1 = ['Newsletter/Marketing', 'Virtual meetings/events', 'Cloud computing service']
    
    spaceRetCase1 = 90
    customer1RetCase1 = 80
    customer2RetCase1 = 70
    managerRetCase1 = 30
    peer1RetCase1 = 50
    peer2RetCase1 = 45
    peer3RetCase1 = 60
    
    # Getters 
    # Prp
    def getSpacePrpCase1(self):
        return self.spacePrpCase1
    
    def getCustomer1PrpCase1(self):
        return self.customer1PrpCase1
    
    def getCustomer2PrpCase1(self):
        return self.customer2PrpCase1
    
    def getManagerPrpCase1(self):
        return self.managerPrpCase1
    
    def getPeer1PrpCase1(self):
        return self.peer1PrpCase1
    
    def getPeer2PrpCase1(self):
        return self.peer2PrpCase1
    
    def getPeer3PrpCase1(self):
        return self.peer3PrpCase1
    
    def getPrpPolicy(self, case):
        pol = []
        if case == 1: 
            pol.append(self.getSpacePrpCase1())
            
        return pol
    
    # Returns all purposes    
    def getPrpPP(self, case, *args): # *args = utils =  0 or 1
        pp = []
        if case == 1:
            pp.append(self.customer1PrpCase1)
            pp.append(self.customer2PrpCase1)
            pp.append(self.peer1PrpCase1)
            pp.append(self.peer2PrpCase1)
            pp.append(self.peer3PrpCase1)
            pp.append(self.managerPrpCase1)
            for u in args:
                pp.append(u.getprpListCase1())
            
        return pp

    def getPowersetPrp(self, case):
        allPrpList = self.getPrpPolicy(case)  # Convert the input iterable to a list.
        prpList = []
        # print('PredefSets::getPowersetPrp - allPrpList: ', allPrpList)
        for prpL in allPrpList:
            for prp in prpL:
                if not prp in prpList:
                    prpList.append(prp)
        
        # print('PredefSets::getPowersetPrp - prpList: ', prpList)
        result = list(chain.from_iterable(combinations(prpList, r) for r in range(len(prpList) + 1)))
        # print('PredefSets::getPowersetPrp - prp powerset: ', result)
        return list(filter(None, result))


    # Choice di pymoo non estrae una tupla, ma un valore numerico. Quindi, al posto di passare il powerset, gli passo un range di valori. 
    # Ad ogni valore, però, deve corrispondere una tupla del powerset. Per questo motivo, costruisco un dizionario a cui associo una chiave numerica ad una tupla.
    def getPrpDict(self, case):
        prpDict = {}
        powerset = self.getPowersetPrp(case)
        powerset = filter(None, powerset)
        i = 0
        for prp in powerset:
            prpDict[i] = set(prp)
            i += 1
            
        # print('PredefSets::getPrpDict - prpDict: ', prpDict)
        return prpDict    
    
    
    # TP
    def getSpaceTPCase1(self):
        return self.spaceTPCase1
    
    def getCustomer1TPCase1(self):
        return self.customer1TPCase1
    
    def getCustomer2TPCase1(self):
        return self.customer2TPCase1
    
    def getManagerTPCase1(self):
        return self.managerTPCase1
    
    def getPeer1TPCase1(self):
        return self.peer1TPCase1
    
    def getPeer2TPCase1(self):
        return self.peer2TPCase1
    
    def getPeer3TPCase1(self):
        return self.peer3TPCase1
    
    
    def getTPPolicy(self, case):
        pol = []
        if case == 1: 
            pol.append(self.getSpaceTPCase1())
        
        return pol
        
    def getTPPP(self, case, *args):
        pp = []
        if case == 1:
            pp.append(self.customer1TPCase1)
            pp.append(self.customer2TPCase1)
            pp.append(self.peer1TPCase1)
            pp.append(self.peer2TPCase1)
            pp.append(self.peer3TPCase1)
            pp.append(self.managerTPCase1)
            for u in args:
                pp.append(u.getTpListCase1())
            
        return pp

    def getPowersetTP(self, case):
        allTPList = self.getTPPolicy(case)  # Convert the input iterable to a list.
        prpList = []
        # print('PredefSets::getPowersetTP - allTPList: ', allTPList)
        for prpL in allTPList:
            for prp in prpL:
                if not prp in prpList:
                    prpList.append(prp)
        
        # print('PredefSets::getPowersetTP - prpList: ', prpList)
        result = list(chain.from_iterable(combinations(prpList, r) for r in range(len(prpList) + 1)))
        # print('PredefSets::getPowersetTP - prp powerset: ', result)
        return list(filter(None, result))


    # Choice di pymoo non estrae una tupla, ma un valore numerico. Quindi, al posto di passare il powerset, gli passo un range di valori. 
    # Ad ogni valore, però, deve corrispondere una tupla del powerset. Per questo motivo, costruisco un dizionario a cui associo una chiave numerica ad una tupla.
    def getTPDict(self, case):
        prpDict = {}
        powerset = self.getPowersetTP(case)
        powerset = filter(None, powerset)
        i = 0
        for prp in powerset:
            prpDict[i] = set(prp)
            i += 1
            
        # print('PredefSets::getTPDict - prpDict: ', prpDict)
        return prpDict    
    

    
    # Ret
    def getSpaceRetCase1(self):
        return self.spaceRetCase1
    
    def getCustomer1RetCase1(self):
        return self.customer1RetCase1
    
    def getCustomer2RetCase1(self):
        return self.customer2RetCase1
    
    def getManagerRetCase1(self):
        return self.managerRetCase1
    
    def getPeer1RetCase1(self):
        return self.peer1RetCase1
    
    def getPeer2RetCase1(self):
        return self.peer2RetCase1
    
    def getPeer3RetCase1(self):
        return self.peer3RetCase1
    
    def getRetPolicy(self, case):
        pol = []
        if case == 1: 
            pol.append(self.getSpaceRetCase1())
        
        return pol
        
    def getRetPP(self, case, *args):
        pp = []
        if case == 1:
            pp.append(self.customer1RetCase1)
            pp.append(self.customer2RetCase1)
            pp.append(self.peer1RetCase1)
            pp.append(self.peer2RetCase1)
            pp.append(self.peer3RetCase1)
            pp.append(self.managerRetCase1)
            
            for u in args:
                pp.append(u.getRetListCase1())
            
        return pp
    
           

    def getPowersetRet(self, case):
        allRetList = self.getRetPolicy(case)  # Convert the input iterable to a list.
        prpList = []
        # print('PredefSets::getPowersetRet - allRetList: ', allRetList)
        for prpL in allRetList:
            for prp in prpL:
                if not prp in prpList:
                    prpList.append(prp)
        
        # print('PredefSets::getPowersetRet - prpList: ', prpList)
        result = list(chain.from_iterable(combinations(prpList, r) for r in range(len(prpList) + 1)))
        # print('PredefSets::getPowersetRet - prp powerset: ', result)
        return list(filter(None, result))


    # Choice di pymoo non estrae una tupla, ma un valore numerico. Quindi, al posto di passare il powerset, gli passo un range di valori. 
    # Ad ogni valore, però, deve corrispondere una tupla del powerset. Per questo motivo, costruisco un dizionario a cui associo una chiave numerica ad una tupla.
    def getRetDict(self, case):
        prpDict = {}
        powerset = self.getPowersetRet(case)
        powerset = filter(None, powerset)
        i = 0
        for prp in powerset:
            prpDict[i] = set(prp)
            i += 1
            
        # print('PredefSets::getRetDict - prpDict: ', prpDict)
        return prpDict    
    
