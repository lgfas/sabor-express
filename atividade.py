def par_ou_impar():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"{numero} é par!")
    else:
        print(f"{numero} é ímpar!")


def categoria_idade():
    idade = int(input("Digite sua idade: "))

    if 0 <= idade <= 12:
        print("Criança")
    elif 13 <= idade <= 18:
        print("Adolescente")
    elif idade > 18:
        print("Adulto")
    else:
        print("Idade inválida")
        
def login():
    usuario_correto = "lgfas"
    senha_correta = "123123"

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado")
    else:
        print("Acesso negado")


def verifica_quadrante():
    x = int(input("Coordenada X: "))
    y = int(input("Coordenada Y: "))

    if x > 0 and y > 0:
        print("Primeiro Quadrante")
    elif x < 0 and y > 0:
        print("Segundo Quadrante")
    elif x < 0 and y < 0:
        print("Terceiro Quadrante")
    elif x > 0 and y < 0:
        print("Quarto Quadrante")
    else:
        print("O ponto está localizado no eixo ou na origem")

def main():
    verifica_quadrante()
    login()
    categoria_idade()
    par_ou_impar()
    numeros_quadrados = {x: x**2 for x in range(1, 6)}
    print(numeros_quadrados)


if __name__ == '__main__':
    main()