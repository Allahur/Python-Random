a = float(input("Digite o valor de A: "))
b = input("Operador: ")
c = float(input("Digite o valor de C: "))

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("Erro \nUse os operadores; \n*\n+\n/\n-")
