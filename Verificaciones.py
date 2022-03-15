print('Por favor ingrese 3 números en forma de lista:')
print()
num1=input()
num2=input()
num3=input()
if (num1.isnumeric() & num2.isnumeric()) & num3.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    print()
else:
    print('Por favor ingrese solo números para poder continuar')
    exit()


if (num2<num1>num3):
    num_mayor=num1
elif (num1<num2>num3):
    num_mayor=num2
else:
    num_mayor=num3

print('Respuesta: ')
print('Entre los 3 números, el número mayor es: ')
print(num_mayor)