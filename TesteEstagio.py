# Exercício 1: Cálculo da soma de números de 1 a 13

def soma():
    indice = 13  # Valor até o qual a soma será calculada
    soma, k = 0, 0  # Inicializa a soma e o contador k

    # Enquanto k for menor que o índice, o loop continuará
    while k < indice:
        k += 1  # Incrementa k
        soma += k  # Soma o valor de k à variável soma
        print(soma)  # Exibe a soma parcial a cada iteração
    print(f"Valor final {soma}\n")  # Exibe o valor final da soma

    return

soma()  # Chama a função soma

# Exercício 2: Verificação de Pertencimento à Sequência de Fibonacci

valor = int(input("Digite um valor:"))  # Recebe um valor do usuário para verificar
v3, v1 = 0, 0  # Inicializa v3 e v1 com 0
v2 = 1  # Inicializa v2 com 1 (primeiros valores de Fibonacci)
lista = [0, 1]  # Cria uma lista para armazenar a sequência de Fibonacci
validacao = 0  # Variável para armazenar o resultado da validação

# Gera a sequência de Fibonacci até o valor desejado
while v3 < valor:
    v3 = v1 + v2  # Calcula o próximo valor de Fibonacci
    v1 = v2  # Atualiza v1
    v2 = v3  # Atualiza v2
    lista.append(v3)  # Adiciona o valor à lista

print(lista)  # Exibe a sequência gerada

# Verifica se o valor fornecido pertence à sequência de Fibonacci
for l in lista:
    if valor == l:
        validacao = 1  # Se o valor pertence à sequência, altera a validação


# Exibe o resultado da verificação
if validacao == 1:
    print(f"O Valor {valor} pertence à sequência de Fibonacci\n")
else:
    print(f"O Valor {valor} não pertence à sequência de Fibonacci\n")

# Exercício 3: Análise de Faturamento Diário

import json  # Importa o módulo JSON para manipular dados JSON

# Carrega os dados de faturamento diário de um arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamentos = []  # Lista para armazenar faturamentos diários válidos
soma_faturamento = 0  # Variável para acumular a soma dos faturamentos
dias_com_faturamento = 0  # Contador para dias com faturamento

# Itera sobre os dados para calcular soma e encontrar os valores válidos de faturamento
for dia in dados['faturamento_diario']:
    valor = dia['valor']
    if valor > 0:  # Ignora dias com faturamento zero
        faturamentos.append(valor)
        soma_faturamento += valor
        dias_com_faturamento += 1

# Calcula o menor e maior valor de faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcula a média mensal (ignorando dias com faturamento zero)
media_mensal = soma_faturamento / dias_com_faturamento

# Conta o número de dias com faturamento acima da média mensal
dias_acima_da_media = 0
for valor in faturamentos:
    if valor > media_mensal:
        dias_acima_da_media += 1

# Exibe os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}\n")

# Exercício 4: Cálculo do Percentual de Representação por Estado

# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcula o percentual de cada estado
percentuais = {}
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    percentuais[estado] = percentual

# Exibe os resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}% do faturamento total\n")
print(f'faturamento total = R$ {faturamento_total:.2f}\n')

# Exercício 5: Inversão de Caracteres de uma String

string = input("Digite uma string: ")  # Recebe uma string do usuário

# Inverte a string usando slicing
string_invertida = string[::-1]

# Exibe a string invertida
print("String invertida:", string_invertida)
