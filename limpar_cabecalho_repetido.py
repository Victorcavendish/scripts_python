#FUNCIONALIDADE = remover cabecalhos repetidos de fontes de arquivos csv

import csv

def limpar_csv(entrada, saida1):
    with open(entrada, newline='', encoding='utf-8-sig') as csv_in:
        leitor = csv.reader(csv_in, delimiter=';')
        linhas = list(leitor)

    if not linhas:
        print("Arquivo está vazio.")
        return

    cabecalho = linhas[0]
    linhas_filtradas = [cabecalho]

    for linha in linhas[1:]:
        # Remove espaços e compara com o cabeçalho
        if [campo.strip() for campo in linha] != [campo.strip() for campo in cabecalho]:
            linhas_filtradas.append(linha)

    with open(saida1, 'w', newline='', encoding='utf-8') as csv_out:
        escritor = csv.writer(csv_out, delimiter=';')
        escritor.writerows(linhas_filtradas)

    print(f"Arquivo limpo salvo como: {saida1}")

# Exemplo de uso
limpar_csv('entrada.csv', 'saida1.csv')
