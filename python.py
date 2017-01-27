#27.01.17
#Magnús Dagur

listi=[]
skra=input("skýra skrá ")
skra=skra+".txt"
minskra = open(skra,'w+')
bleyta = input("Sláðu inn texta innihald")
minskra.write(bleyta+"\n")
minskra = exit
minskra = open(skra,'a')
val=int(input("Sláðu inn hversu marga texta þu vilt hafa "))
telj=0
while telj != val:
    texti = input("Sláðu inn texta :")
    listi.append(texti)
    minskra.write(texti+"\n")
    telj+=1
minskra = exit
minskra = open(skra,"r")
print(minskra.read())
minskra.close
