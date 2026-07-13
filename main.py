meme_dict = {
    "LOL": "Risada na internet.",
    "AFK": "Longe do teclado.",
    "NOOB": "Pessoa iniciante em um jogo.",
    "BUG": "Erro em um programa ou jogo.",
    "NERF": "Quando algo fica mais fraco em um jogo."
}

print("Bem-vindo ao dicionário!")
print("--------------------")
print("Palavras disponíveis:")
for palavra in meme_dict:
    print("-", palavra)
print("--------------------")
print("Digite uma palavra em letras maiúsculas.")

for i in range(5):
    palavra = input("Digite uma palavra que você não entende: ")

    if palavra in meme_dict:
        print("Significado:", meme_dict[palavra])
    else:
        print("Essa palavra não foi encontrada.")
        resposta = input("Deseja adicionar essa palavra? S ou N: ")

        if resposta == "S":
            significado = input("Digite o significado: ")
            meme_dict[palavra] = significado
            print("Palavra adicionada!")

    print("--------------------")

print("Dicionário atualizado:")

for palavra in meme_dict:
    print(palavra, "-", meme_dict[palavra])
