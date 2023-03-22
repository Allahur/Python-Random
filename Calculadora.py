# Cálculo básico

a = float(input("Digite o valor de A: ")) # Valor primário 
b = input("Operador: ") # símbolo ao qual quer fazer o cálculo 
c = float(input("Digite o valor de C: ")) # Valor secundário para fazer o cálculo 

# Simbolos para cálculos básicos.
if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("Erro \nUse os operadores; \n*\n+\n/\n-") # Caso der erro ou usou algo não correspondente ao enunciado
