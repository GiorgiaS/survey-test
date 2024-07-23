from pages.src.PredefSets import PredefSets
from pages.src.IntermediatePolicy import IntermediatePolicy


predSet = PredefSets()
ip = IntermediatePolicy()

newPrp, newRet, newTP = ip.computeIntermediatePolicy(1)

print(newPrp)
print(newRet)
print(newTP)
