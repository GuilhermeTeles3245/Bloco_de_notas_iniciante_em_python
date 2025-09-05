# Aplicação de Bloco de Notas com CRUD (Criar, Ler, Atualizar, Deletar)
# Autor: Guilherme Teles Pacheco :)
# Objetivo: Exemplo de aplicação simples para treinar conceitos de CRUD em Python, usando dicionários e listas.
# Observação: O código do Jogo da Velha Supremo foi feito em uma pasta separada e importado aqui para manter a organização.

# Variáveis globais
escolha = 0
blocos = {}  # Dicionário que vai armazenar os blocos de notas (título -> lista de linhas)

print("Bem-vindo ao Bloco de Notas!\n")

def mostrar_lista_atual():
    """
    Exibe a lista atual de blocos criados.
    """
    print("Blocos atuais:")
    for titulo in blocos:
        print(f" - {titulo}")
    print("\n")

def interface():
    """
    Exibe o menu inicial para escolher o tipo de usuário:
    - Administrador
    - Visitante
    Retorna a escolha feita pelo usuário.
    """
    print("Seja Bem Vindo!\n")
    print("1. Admin")
    print("2. Visitante")
    interface = input("Digite sua função atual: ")
    return interface

def menu_adm():
    """
    Exibe o menu do administrador com todas as opções CRUD.
    Retorna a escolha do usuário.
    """
    print("Selecione o que deseja fazer:")
    print("1. Criar         4. Atualizar")
    print("2. Editar        5. Deletar")
    print("3. Ler           6. Interface")
    print("7. Sair\n")
    escolha = input("Opção: ")
    return escolha

def menu_visitante():
    """
    Exibe o menu do visitante, que pode apenas ler blocos ou sair.
    Retorna a escolha do usuário.
    """
    print("Selecione o que deseja fazer:")
    print("1. Ler")
    print("2. Sair")
    print("3. Interface\n")
    escolha = input("Opção: ")
    print("\n")
    return escolha

def criar():
    """
    Cria um novo bloco de notas com um título fornecido pelo usuário.
    O bloco é armazenado no dicionário global 'blocos'.
    """
    titulo = input("Título do bloco: ")
    blocos[titulo] = []  # Cria um bloco vazio
    print(f"Bloco '{titulo}' criado com sucesso!\n")
    resposta = input("Deseja criar mais um bloco? (s/n): ")
    if resposta == 's' or resposta == 'sim' or resposta == 'S' or resposta == 'SIM':
        criar()  # Recursão para criar mais blocos
    input("Pressione Enter para continuar...\n")

def editar():
    """
    Permite editar (adicionar linhas de texto) em um bloco existente.
    """
    mostrar_lista_atual()
    titulo = input("Escolha o bloco que deseja editar o conteúdo: ")
    if titulo in blocos:
        print(f"Conteúdo atual do bloco '{titulo}':")
        for linha in blocos[titulo]:
            print(f" - {linha}")
        print("\n")
        nova_linha = input("Digite a nova linha de texto: ")
        blocos[titulo].append(nova_linha)  # Adiciona linha no bloco
        print(f"Bloco '{titulo}' atualizado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.\n")
    resposta = input("Deseja adicionar mais linhas? (s/n): ")
    if resposta == 's' or resposta == 'sim' or resposta == 'S' or resposta == 'SIM':
        editar()
    else:
        input("Pressione Enter para continuar...\n")

def ler():
    """
    Lê e exibe o conteúdo de um bloco escolhido pelo usuário.
    """
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
    """
    Atualiza o título de um bloco existente.
    """
    mostrar_lista_atual()
    titulo = input("Título do bloco a ser atualizado: ")
    if titulo in blocos:
        print(f"Conteúdo atual do bloco '{titulo}':")
        for linha in blocos[titulo]:
            print(f" - {linha}")
        print("\n")
        novo_titulo = input("Digite o novo título do bloco: ")
        blocos[novo_titulo] = blocos.pop(titulo)  # Renomeia o bloco
        print(f"Bloco '{titulo}' atualizado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.")
    resposta = input("Deseja atualizar mais algum bloco? (s/n): ")
    if resposta == 's' or resposta == 'sim' or resposta == 'S' or resposta == 'SIM':
        atualizar()
    input("Pressione Enter para continuar...\n")

def deletar():
    """
    Deleta um bloco existente do dicionário 'blocos'.
    """
    mostrar_lista_atual()
    titulo = input("Título do bloco a ser deletado: ")
    if titulo in blocos:
        del blocos[titulo]
        print(f"Bloco '{titulo}' deletado com sucesso!")
    else:
        print(f"Bloco '{titulo}' não encontrado.\n")
    resposta = input("Deseja deletar mais algum bloco? (s/n): ")
    if resposta == 's' or resposta == 'sim' or resposta == 'S' or resposta == 'SIM':
        deletar()
    else:
        input("Pressione Enter para continuar...\n")

def sair():
    """
    Sai da aplicação de bloco de notas.
    """
    print("Saindo do Bloco de Notas. Até mais!\n")
    exit()

# Loop principal da aplicação
while True:
    interface_escolhida = interface()
    if interface_escolhida == '1':  # Admin
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
            elif escolha == '6':  # Voltar para interface inicial
                break
            elif escolha == '7':
                sair()
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 7.")
    elif interface_escolhida == '2':  # Visitante
        escolha = menu_visitante()
        if escolha == '1':
            ler()
        elif escolha == '2':
            sair()
        elif escolha == '3':  # Voltar para interface inicial
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 3.")