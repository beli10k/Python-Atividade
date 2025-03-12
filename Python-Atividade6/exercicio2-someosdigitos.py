def soma_digitos(numero):
    if not numero.isdigit():
        return "O valor informado não é um número inteiro."
    return sum(int(digito) for digito in numero)

numero = input("Informe um número inteiro: ")


resultado = soma_digitos(numero)
print(resultado)
