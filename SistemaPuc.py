# Dicionários para armazenar informações
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []


# Função para exibir o menu de opções
def menu():
    while True:
        print("\nSistema PUC")
        print("1 - Estudante")
        print("2 - Disciplina")
        print("3 - Professor")
        print("4 - Turma")
        print("5 - Matrícula")
        print("9 - Sair")

        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            menu_estudante()
        elif opcao == "2":
            print("EM DESENVOLVIMENTO")
            continue
        elif opcao == "3":
            print("EM DESENVOLVIMENTO")
            continue
        elif opcao == "4":
            print("EM DESENVOLVIMENTO")
            continue
        elif opcao == "5":
            print("EM DESENVOLVIMENTO")
            continue
        elif opcao == "9":
            exit()
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def menu_estudante():
    while True:
        print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
        print("1 - Incluir.")
        print("2 - Listar.")
        print("3 - Excluir.")
        print("4 - Atualizar.")
        print("9 - Voltar ao menu principal.")

        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            excluir_estudante()
            continue
        elif opcao == "4":
            alterar_estudante()
            continue
        elif opcao == "9":
            menu()
            continue
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def incluir_estudante():
    # Implementar a funcionalidade de incluir um novo estudante aqui
    codigo = input("Informe o código do estudante: ")
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes.append(estudante)
    print("Estudante adicionado com sucesso!")

def listar_estudantes():
    print("===== LISTAGEM ======")
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados")
    else:
        for nome in estudantes:
            print(nome)


def excluir_estudante():
        # Implementar a funcionalidade de excluir um estudante aqui
        codigo = input("Informe o código do estudante que deseja excluir: ")
        encontrado = False
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudantes.remove(estudante)
                encontrado = True
                break
        if encontrado:
            print("Estudante removido com sucesso!")
        else:
            print("Estudante não encontrado na lista.")

def alterar_estudante():
    # Implementar a funcionalidade de editar um estudante aqui
    codigo = input("Informe o código do estudante que deseja editar: ")
    encontrado = False
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            nome = input("Informe o novo nome do estudante: ")
            cpf = input("Informe o novo CPF do estudante: ")
            estudante['nome'] = nome
            estudante['cpf'] = cpf
            encontrado = True
            break
    if encontrado:
        print("Estudante editado com sucesso!")
    else:
        print("Estudante não encontrado na lista.")

def menu_disciplina():
    print("EM DESENVOLVIMENTO")
    # Implementar as opções do menu Disciplina


def menu_professor():
    print("EM DESENVOLVIMENTO")
    # Implementar as opções do menu Professor


def menu_turma():
    print("EM DESENVOLVIMENTO")
    # Implementar as opções do menu Turma


def menu_matricula():
    print("EM DESENVOLVIMENTO")
    # Implementar as opções do menu Matrícula


menu()
