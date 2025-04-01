import os
#import Transformador

import os
import pdfplumber
import pandas as pd

def extrair_tabelas_pdf(caminho_pdf, inicio, fim):
    with pdfplumber.open(caminho_pdf) as pdf:
        tabelas = []
        for pagina_num in range(inicio-1, fim):
            pagina = pdf.pages[pagina_num]
            tabela = pagina.extract_table()
            if tabela:
                tabelas.append(tabela)
        return tabelas

def salvar_tabelas_excel(tabelas, caminho_excel):
    with pd.ExcelWriter(caminho_excel, engine='openpyxl') as writer:
        for i, tabela in enumerate(tabelas):
            df = pd.DataFrame(tabela[1:], columns=tabela[0])
            df.to_excel(writer, index=False, sheet_name=f'Tabela_{i+1}')

def main():
    arquivos = []
    while True:
        opcao = input("Digite 1 para inserir arquivo, 0 para cancelar, 2 para transformar: ")
        if opcao == "1":
            caminho = input("Digite o caminho do arquivo PDF: ")
            if os.path.exists(caminho):
                arquivos.append(caminho)
            else:
                print("Arquivo não encontrado.")
        elif opcao == "0":
            print("Operação cancelada.")
            break
        elif opcao == "2":
            if arquivos:
                for arquivo in arquivos:
                    print(f"Processando: {arquivo}")
                    inicio = int(input("Digite o número da página inicial para extrair: "))
                    fim = int(input("Digite o número da página final para extrair: "))
                    tabelas = extrair_tabelas_pdf(arquivo, inicio, fim)
                    if tabelas:
                        caminho_excel = arquivo.replace(".pdf", ".xlsx")
                        salvar_tabelas_excel(tabelas, caminho_excel)
                        print(f"Arquivo Excel gerado: {caminho_excel}")
                    else:
                        print(f"Nenhuma tabela encontrada no arquivo {arquivo}.")
            else:
                print("Nenhum arquivo foi informado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

#C:\Users\UCL\Downloads\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf