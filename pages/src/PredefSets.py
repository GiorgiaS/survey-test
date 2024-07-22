from itertools import chain, combinations
import random

class PredefSets:
    ################
    # Purpose Field
    ################
    spacePrpCase1 = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    customer1PrpCase1 = ['Basic service', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    customer2PrpCase1 = ['Basic service', 'Service operation and security', 'Additional service/feature']
    managerPrpCase1 = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    peer1PrpCase1 = ['Basic service', 'Legal requirement', 'Service operation and security', 'Additional service/feature']
    peer2PrpCase1 = ['Basic service', 'Analytics/Research', 'Marketing', 'Legal requirement']
    peer3PrpCase1 = ['Basic service', 'Service operation and security', 'Additional service/feature']
    
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
    
    
    
    def getPowersetPrp(self):
        s = list(self.allPrp)  # Convert the input iterable to a list.
        result = list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
        return list(filter(None, result))


    # Choice di pymoo non estrae una tupla, ma un valore numerico. Quindi, al posto di passare il powerset, gli passo un range di valori. 
    # Ad ogni valore, però, deve corrispondere una tupla del powerset. Per questo motivo, costruisco un dizionario a cui associo una chiave numerica ad una tupla.
    def getPrpDict(self):
        prpDict = {}
        powerset = self.getPowersetPrp()
        powerset = filter(None, powerset)
        i = 0
        for prp in powerset:
            prpDict[i] = set(prp)
            i += 1
            
        return prpDict    
    
