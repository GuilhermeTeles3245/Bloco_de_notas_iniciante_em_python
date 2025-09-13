# Variáveis globais
resultado = False
escolha = 0
blocos = {}  # Dicionário que vai armazenar os blocos de notas (título -> lista de linhas)
Contas_do_usuario = {"admin": "admin123"} # Dicionário para armazenar usuários e senhas


def criar_usuario():
    usuario = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    Contas_do_usuario[usuario] = senha
    print(f"Usuário {usuario} criado com sucesso!\n")


def login():
    global resultado  # precisa pra alterar a variável global
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in Contas_do_usuario and Contas_do_usuario[usuario] == senha:
        print(f"Bem-vindo, {usuario}!\n")
        resultado = True
    else:
        print("Usuário ou senha incorretos. Tente novamente.\n")
        resultado = False
    return resultado


def interface():
    print("Seja Bem Vindo!\n")
    print("1. Criar Usuário")
    print("2. Login")
    print("3. Visitante\n")
    interface = input("Digite a opção desejada: ")
    return interface


def mostrar_lista_atual():
    print("Blocos atuais:")
    if len(blocos) == 0:
        print(" - Nenhum bloco criado ainda")
    else:
        for titulo in blocos:
            print(f" - {titulo}")
    print("\n")


def menu_adm():
    print("Selecione o que deseja fazer:")
    print("1. Criar         4. Atualizar")
    print("2. Editar        5. Deletar")
    print("3. Ler           6. Voltar pra Interface")
    print("7. Sair\n")
    escolha = input("Opção: ")
    return escolha


def menu_visitante():
    print("Selecione o que deseja fazer:")
    print("1. Ler")
    print("2. Voltar pra Interface")
    print("3. Sair\n")
    escolha = input("Opção: ")
    print("\n")
    return escolha


def criar():
    titulo = input("Título do bloco: ")
    blocos[titulo] = []  
    print(f"Bloco '{titulo}' criado com sucesso!\n")
    resposta = input("Deseja criar mais um bloco? (s/n): ")
    if resposta.lower() in ['s', 'sim']:
        criar()
    input("Pressione Enter para continuar...\n")


def editar():
    mostrar_lista_atual()
    titulo = input("Escolha o bloco que deseja editar o conteúdo: ")
    if titulo in blocos:
        print(f"Conteúdo atual do bloco '{titulo}':")
        for linha in blocos[titulo]:
            print(f" - {linha}")
        print("\n")
        nova_linha = input("Digite a nova linha de texto: ")
        blocos[titulo].append(nova_linha)
        print(f"Bloco '{titulo}' atualizado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.\n")
    resposta = input("Deseja adicionar mais linhas? (s/n): ")
    if resposta.lower() in ['s', 'sim']:
        editar()
    else:
        input("Pressione Enter para continuar...\n")


def ler():
    mostrar_lista_atual()
    titulo = input("Título do bloco a ser lido: ")
    if titulo in blocos:
        print(f"Conteúdo do bloco '{titulo}':")
        for linha in blocos[titulo]:
            print(f" - {linha}")
        print("\n")
    else:
        print(f"Bloco '{titulo}' não encontrado.\n")
    input("Pressione Enter para continuar...\n")


def atualizar():
    mostrar_lista_atual()
    titulo = input("Título do bloco a ser atualizado: ")
    if titulo in blocos:
        print(f"Conteúdo atual do bloco '{titulo}':")
        for linha in blocos[titulo]:
            print(f" - {linha}")
        print("\n")
        novo_titulo = input("Digite o novo título do bloco: ")
        blocos[novo_titulo] = blocos.pop(titulo)
        print(f"Bloco '{titulo}' atualizado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.")
    resposta = input("Deseja atualizar mais algum bloco? (s/n): ")
    if resposta.lower() in ['s', 'sim']:
        atualizar()
    input("Pressione Enter para continuar...\n")


def deletar():
    mostrar_lista_atual()
    titulo = input("Título do bloco a ser deletado: ")
    if titulo in blocos:
        del blocos[titulo]
        print(f"Bloco '{titulo}' deletado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.\n")
    resposta = input("Deseja deletar mais algum bloco? (s/n): ")
    if resposta.lower() in ['s', 'sim']:
        deletar()
    else:
        input("Pressione Enter para continuar...\n")


def sair():
    print("Saindo do Bloco de Notas. Até mais!\n")
    exit()


while True:
    interface_escolhida = interface()
    if interface_escolhida == '1':
        criar_usuario()
    elif interface_escolhida == '2':
        # Sempre pede login quando escolher a opção 2
        login()
        if resultado:
            # Entrou: menu admin
            while True:
                escolha = menu_adm()
                if escolha == '1':
                    criar()
                elif escolha == '2':
                    editar()
                elif escolha == '3':
                    ler()
                elif escolha == '4':
                    atualizar()
                elif escolha == '5':
                    deletar()
                elif escolha == '6':
                    # Voltar pra interface e exigir senha na próxima vez
                    resultado = False
                    break
                elif escolha == '7':
                    sair()
                else:
                    print("Opção inválida. Tente novamente.\n")
    elif interface_escolhida == '3':
        while True:
            escolha = menu_visitante()
            if escolha == '1':
                ler()
            elif escolha == '2':
                break
            elif escolha == '3':
                sair()
            else:
                print("Opção inválida. Tente novamente.\n")
    else:
        print("Opção inválida. Tente novamente.\n")
