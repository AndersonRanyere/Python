import os
import pandas as pd

diretorio = r'\\2023'

arquivos_xlsm = []

# Lista todos os arquivos no diretório
for root, dirs, files in os.walk(diretorio):
    for file in files:
        if file.endswith('.xlsm'):
            arquivos_xlsm.append(os.path.join(root, file))

if not arquivos_xlsm:
    print("Nenhum arquivo .xlsm encontrado na pasta.")
else:
    # Encontre o arquivo .xlsm mais recente com base na data de modificação
    arquivo_mais_recente = max(arquivos_xlsm, key=lambda x: os.path.getmtime(x))

    # Mensagem de depuração para verificar o caminho do arquivo
    print(f"Caminho do arquivo .xlsm mais recente: {arquivo_mais_recente}")

    # Nome da planilha que você deseja abrir (substitua pelo nome correto)
    nome_da_planilha = 'Linhas Rejeitadas'

    # Abra a segunda aba do arquivo Excel
    try:
        df = pd.read_excel(arquivo_mais_recente, sheet_name=nome_da_planilha)

        # Seleciona apenas as colunas desejadas
        colunas_desejadas = ['geo', 'cdd', 'nomes', 'Titulo', 'NP', 'Unb', 'Cliente', 'Nosso_Numero', 'Vl_Movto']
        df = df[colunas_desejadas]

        # Agora você tem um DataFrame com apenas as colunas desejadas
        print(df.head())  # Exemplo: Imprime as primeiras linhas do DataFrame resultante

        # Ordena o DataFrame pelo valor da coluna 'geo' em ordem crescente
        df = df.sort_values(by='geo', ascending=True)

        # Agora você tem o DataFrame ordenado por 'geo'
        print(df.head())  # Exemplo: Imprime as primeiras linhas do DataFrame ordenado
    except FileNotFoundError:
        print(f'O arquivo {arquivo_mais_recente} não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao abrir o arquivo Excel: {e}')

df.to_excel('dados_processados.xlsx', index=False)

pd.read_excel('dados_processados.xlsx').head()

# Carregue o arquivo Excel com os dados processados
df = pd.read_excel('dados_processados.xlsx')

# Obtenha os valores únicos da coluna 'geo'
geos = df['geo'].unique()

# Crie um escritor Excel (ExcelWriter) para gravar em um único arquivo Excel
writer = pd.ExcelWriter('dados_separados_por_geo.xlsx', engine='xlsxwriter')

# Para cada valor único em 'geo', crie uma aba e salve os dados nessa aba
for geo in geos:
    # Filtrar o DataFrame para o valor específico de 'geo'
    df_filtrado = df[df['geo'] == geo]
    
    # Salvar os dados na aba correspondente
    df_filtrado.to_excel(writer, sheet_name=geo, index=False)

# Feche o escritor Excel
writer.save()

# Mensagem de conclusão
print("Dados separados por GEO foram salvos em 'dados_separados_por_geo.xlsx'.")

