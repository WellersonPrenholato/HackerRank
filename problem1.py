# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem

linha_entrada = input()

entradas = linha_entrada.split()
rows = int(entradas[0])
columns = int(entradas[1])
# columns = rows * 3

# Imprime o padrão
for i in range(rows):
    if i < rows // 2:
        pattern = ".|." * (2 * i + 1)
    elif i == rows // 2:
        pattern = "WELCOME"
    else:
        pattern = ".|." * (2 * (rows - i - 1) + 1)
    linha = "-" * ((columns - len(pattern)) // 2)
    
    print(linha + pattern + linha)