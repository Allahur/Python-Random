print("\nO que é, o que é, come raízes é nojento e fica embaixo da terra ?")
palavra_secreta = "Minhoca"
palpite = ""
contador = 0
limite = 3
sair = False

while palpite != palavra_secreta and not (sair):
    if contador < limite:
        palpite = input("\n\nDigite seu palpite: ")
        contador += 1
    else: 
        sair = True
if sair == True:
        print('\nVocê perdeu!')
else:
        print("\nGanhou!")
