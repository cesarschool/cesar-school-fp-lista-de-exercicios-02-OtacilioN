## QUESTÃO 2 ##
# Uma forma de avaliar se uma pessoa está acima do peso é através do calculo do índice IMC.
# Se o valor do IMC estiver acima de 25, significa que a pessoa está acima do peso.
# A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m)). Com base na altura e peso fornecido no
# console exiba uma mensagem determinando se uma pessoa está acima do peso.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

# BMI = IMC (In English)

def _get_IMC(weight, stature):
    return weight/(stature*stature)


def main():
    weight = float(input("Type the weight in kg: "))
    stature = float(input("Type the stature in m: "))
    BMI = _get_IMC(weight, stature)
    if(BMI > 25):
        print("You are over the weight")
    else:
        print("You are NOT over the weight")


if __name__ == '__main__':
    main()
