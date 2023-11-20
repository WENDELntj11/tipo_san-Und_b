nome_do_arquivo = "lista_tipos_sanguineos.txt"

def adicionar_nome_e_tipo_sanguineo():
    nome = input("Insira o nome do paciente Por favor: ")
    tipo_sanguineo = input("Digite o tipo sanguíneo: ")
    pessoa = {
        "Nome": nome,
        "Tipo Sanguíneo": tipo_sanguineo
    }
    lista_de_pessoas.append(pessoa)
    print(f"Dados de {pessoa} armazenados com sucesso!")


def visualizar_lista():
    if not lista_de_pessoas:
        print("A lista está completamente vazia")
    else:
        print("Lista dos Nomes e Tipagem Sanguínea:")
        for pessoa in lista_de_pessoas:
            print(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}"
            )

def salvar_dados():
    with open(nome_do_arquivo, "w") as arquivo:
        for pessoa in lista_de_pessoas:
            arquivo.write(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}"
            )
        print("Arquivo gerado com sucesso!")
def carregar_dados():
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(", ")
                nome = dados[0].split(": ")[1]
                tipo_sanguineo = dados[1].split(": ")[1]
                pessoa = {
                    "Nome": nome,
                    "Tipo Sanguíneo": tipo_sanguineo
                }
                lista_de_pessoas.append(pessoa)
            print(" Seus dados foram carregados com sucesso!")
    except FileNotFoundError:
        print(f"ERRO! \n O arquivo {nome_do_arquivo} não foi encontrado. Procure alguem ou administrador do sistema.")
carregar_dados()

while True:
    print("\n Opções")
    print(
        "1. ADICIONAR PACIENTE E TIPO SANGUÍNEO \n2. VISUALIZAR PACIENTES \n3. SALVAR DADOS EM ARQUIVO \n4. ENCERRAR O SISTEMA"
    )
    opcao = input("ESCOLHA  APENAS UMA OPÇÃO: ")
    if opcao == "1":
        adicionar_nome_e_tipo_sanguineo()
    elif opcao == "2":
        visualizar_lista()
    elif opcao == "3":
        salvar_dados()
    elif opcao == "4":
        print(" O Sistema  foiencerrado com sucesso!")
        break
    else:
        print("Infelizmente essa opção esta inválida, tente novamente!")
