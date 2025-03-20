
#for count in range(1, 100, 25):
#    print(count)

lst_numb = [12, 45,78,96,72,102,101,145,785]
for index, value in enumerate(lst_numb):
    print(f"Rang: {index}, Valeur: {value}")


d = { 1:"red", 2:"green", 3:"blue", 4:"yellow"}
for key, value in d.items(): 
    print(key)
    print(value)

print("les clés")
for k in d.keys():
    print(k)

print("Les valeurs\n")
for v in d.values():
    print(v)

print("Les clés - valeurs\n")
for k, v in d.items():      
    print(k, v)

tpl = ("red", "green", "blue", "yellow")
for i in tpl:
    print(i)


tple = (12, 18, 20, 22, 45, 78)
for i in range(len(tple)):
    #print( i, " ", tple[i])
    print(f"{i} {tple[i]}")