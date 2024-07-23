from PredefSets import PredefSets
from IntermediatePolicy import IntermediatePolicy
predSet = PredefSets()
ip = IntermediatePolicy()

newPrp, newRet, newTP = ip.computeIntermediatePolicy(1)

print(newPrp)
print(newRet)
print(newTP)
