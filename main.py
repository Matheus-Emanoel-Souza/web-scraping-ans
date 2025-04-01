import os

def main():
    arquivos = []
    while True:
        opcao = input("Digite 1 para inserir arquivo, 0 para cancelar, 2 para transformar: ")
        if opcao == "1":
            caminho = input("Digite o caminho do arquivo: ")
            if os.path.exists(caminho):
                arquivos.append(caminho)
            else:
                print("Arquivo não encontrado.")
        elif opcao == "0":
            print("Operação cancelada.")
            break
        elif opcao == "2":
            if arquivos:
                print("Transformação realizada para os arquivos:")
                for arquivo in arquivos:
                    print(arquivo)
            else:
                print("Nenhum arquivo foi informado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
