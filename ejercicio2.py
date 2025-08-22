numero=int(input("Dame un numero: "))

if(numero>=0 and numero%2==0):
    print("Par Positivo")
elif(numero>=0):
    print("Impar Positivo")
elif(numero%2==0):
    print("Par Negativo")
else:
    print("Impar Negativo")
    