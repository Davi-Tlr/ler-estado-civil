nome = input("Digite seu nome: ")

# Loop até o usuário digitar uma entrada válida para o estado civil
while True:
    estC = input('Digite seu estado civil: "S": Solteiro, "C": Casado, "V": Viúvo, "D": Divorciado: ').upper()
    if estC == "S":
        estC = "Solteiro"
        break
    elif estC == "C":
        estC = "Casado"
        break
    elif estC == "V":
        estC = "Viúvo"
        break
    elif estC == "D":
        estC = "Divorciado"
        break
    else:
        print('Entrada inválida. Por favor, digite "S", "C", "V" ou "D".')

print(f"Nome: {nome}, Estado Civil: {estC}")
