print("Ingresa los lados de un triángulo, números enteros mayores a cero, por favor")

X= abs(int(input("Lado X: ")))
Y= abs(int(input("Lado Y: ")))
Z= abs(int(input("Lado Z: ")))

if(X*Y*Z==0):
    print("Qué parte de triángulo no entendiste (pusiste un cero)?")
else:
    #validamos que sea tríangulo y lo clasificamos
    if( (X+Y)>Z and (X+Z)>Y and (Y+Z)>X ):

        if(X==Y and X==Z):
            print("Equilátero")
        elif(X==Y or X==Z or Y==Z):
            print("Isósceles")
        else:
            print("Escaleno")

    else:
        print("Qué parte de lados de un triángulo no entendiste?")

'''
Pruebas:
1: X=8, Y=8, Z=8, R= Equilátero
2.1: X=8, Y=8, Z=1, R= Isósceles
2.2: X=8, Y=1, Z=8, R= Isósceles
2.3: X=1, Y=8, Z=8, R= Isósceles
3: X=3, Y=4, Z=5, R= Ecaleno
4: X=-8, Y=-8, Z=-8, R= Equilátero, no afecta el - por el valor absoluto (abs)
5: X=0, Y=1, Z=1, R= Uno es cero, no es triángulo
6: X=1, Y=2, Z=3, R= No es triángulo
'''