''''
Linha de comando pra pedir nome, idade e email do usuário em uma pilha.
'''''

pilha = []

def nome():
    name = input("Digite seu nome: ")
    return name

def age():
    idade = int(input("\nDigite a sua idade: "))
    return idade

def mail():
    email = input("\nDigite o seu e-mail: ")
    return email

def empilhar():
    name = nome()
    idade = age()
    email = mail()
    registro = (name, idade, email)
    pilha.append(registro)

def desempilhar():
    if pilha:
        pilha.pop()
        print("Registro desempilhado com sucesso.")
    else:
        print("A pilha está vazia. Não é possível desempilhar.")

def exibir_registros():
    if pilha:
        print("\n--- Registros ---")
        for registro in pilha:
            print("Nome:", registro[0])
            print("Idade:", registro[1])
            print("Email:", registro[2])
            print("----------------")
    else:
        print("A pilha está vazia. Não há registros para exibir.")

def menu():
    print("\n1 - Empilhar registro")
    print("2 - Desempilhar registro")
    print("3 - Exibir registros")
    print("4 - Sair")
    option = int(input("\nSelecione a opção: "))
    return option

def controle():
    while True:
        option = menu()
        
        if option == 1:
            empilhar()
        elif option == 2:
            desempilhar()
        elif option == 3:
            exibir_registros()
        elif option == 4:
            break
        else:
            print("\nOpção inválida.")

def main():
    print("Controle de LIFO com arranjo não dinâmico\n")
    controle()

main()
