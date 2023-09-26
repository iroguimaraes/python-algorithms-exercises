weight = float(input("Peso: "))
converter = str(input("(K)g ou (L)bs: "))

if converter == "L" or converter == "l":
    converted_weight = weight / 2.2
    print("Peso em Kg: " + str(converted_weight))

elif converter == "K" or converter == "k":
    converted_weight = weight * 2.2
    print("Peso em Lbs: " + str(converted_weight))
else: 
    print("favor digitar K ou L para conversão")