
#Currency Value
COPtoUSD = 0.00026 
PVStoUSD = 0.27 
BRtoUSD = 0.20 

#User Input
pesos = float(input("What do you have left in pesos? ")) #Colombian Peso
soles = float(input("What do you have left in soles? ")) #Peruvian Sole
reais = float(input("What do you have left in reais? ")) #Brazilian Reais

#Convertion to USD
pesos = pesos * COPtoUSD
soles = soles * PVStoUSD
reais = reais * BRtoUSD

#USD total

totalUSD = pesos + soles + reais

print (totalUSD)