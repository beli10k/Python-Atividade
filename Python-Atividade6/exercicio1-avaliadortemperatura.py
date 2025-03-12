def validar_numero(numero):
    try:
        return float(numero)
    except ValueError:
        return None

def soma_digitos(numero):
    if not numero.isdigit():
        return "O valor informado não é um número inteiro válido."
    return sum(int(digito) for digito in numero)


temp_max = input("Informe a temperatura mais alta do dia: ")
temp_min = input("Informe a temperatura mais baixa do dia: ")

temp_max = validar_numero(temp_max)
temp_min = validar_numero(temp_min)

if temp_max is None or temp_min is None:
    print("Erro: Você deve falar números válidos (inteiros ou decimais).")
else:
    # Cálculos
    media = (temp_max + temp_min) / 2
    variacao = abs(temp_max - temp_min)
    
    print(f"Média da temperatura: {media:.2f}")
    print(f"Variação de temperatura: {variacao:.2f}")
    
    # Solicitação do número para soma de dígitos
    numero = input("Informe um número inteiro para calcular a soma dos dígitos: ")
    resultado = soma_digitos(numero)
    print(resultado)
