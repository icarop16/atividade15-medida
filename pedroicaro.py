# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 
# PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
med1 = int(input("Digite á medida: "))
med2 = int(input("Digite á medida: "))
med3 = int(input("Digite á medida: "))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2 :
    print("Com essas medidas, um triângulo pode sim ser formado.")
else : 
    print("Com essas medidas, não é possível formar um triângulo.")