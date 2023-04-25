import json

# Dicionários para armazenar informações
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

def salvar_estudante():
    with open('estudantes.json', 'w') as arquivo:
        json.dump(estudantes, arquivo)

def salvar_professor():
    with open('professores.json', 'w') as arquivo:
        json.dump(professores, arquivo)
    
def salvar_disciplina():
    with open('disciplinas.json', 'w') as arquivo:
        json.dump(disciplinas, arquivo)

def salvar_turma():
    with open('turmas.json', 'w') as arquivo:
        json.dump(turmas, arquivo)

def salvar_matricula():
    with open('matriculas.json', 'w') as arquivo:
        json.dump(matriculas, arquivo)

def carregar_estudante():
    global estudantes
    try:
        with open('estudantes.json', 'r') as arquivo:
            estudantes = json.load(arquivo)
    except FileNotFoundError:
        estudantes = []

def carregar_disciplina():
    global disciplinas
    try:
        with open('disciplinas.json', 'r') as arquivo:
            disciplinas = json.load(arquivo)
    except FileNotFoundError:
        disciplinas = []

def carregar_professor():
    global professores
    try:
        with open('professores.json', 'r') as arquivo:
            estudantes = json.load(arquivo)
    except FileNotFoundError:
        professores = []

def carregar_turma():
    global turmas
    try:
        with open('turmas.json', 'r') as arquivo:
            turmas = json.load(arquivo)
    except FileNotFoundError:
        turmas = []

def carregar_matricula():
    global matriculas
    try:
        with open('matriculas.json', 'r') as arquivo:
            matriculas = json.load(arquivo)
    except FileNotFoundError:
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
            menu_disciplina()
        elif opcao == "3":
            menu_professor()
        elif opcao == "4":
            menu_turma()
        elif opcao == "5":
            menu_matricula()
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
    codigo = int(input("Informe o código do estudante: "))
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")
    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes.append(estudante)
    salvar_estudante()
    print("Estudante adicionado com sucesso!")

def listar_estudantes():
    print("===== LISTAGEM ======")
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        for estudante in estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")


def excluir_estudante():
        # Implementar a funcionalidade de excluir um estudante aqui
        codigo = input("Informe o código do estudante que deseja excluir: ")
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudantes.remove(estudante)
                salvar_estudante()
                print("Estudante removido com sucesso!")
                return
            print("Estudante não encontrado.")

def alterar_estudante():
    # Implementar a funcionalidade de editar um estudante aqui
    codigo = input("Informe o código do estudante que deseja editar: ")
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            nome = input(f"Informe o novo nome para o estudante {codigo}: ")
            cpf = input(f"Informe o novo CPF para o estudante {codigo}: ")
            estudante['nome'] = nome
            estudante['cpf'] = cpf
            salvar_estudante()
            print("Estudante alterado com sucesso!")
            return
    print("Estudante não encontrado.")

def menu_disciplina():
    while True:
        print("***** [DISCIPLINAS] MENU DE OPERAÇÕES *****")
        print("1 - Incluir.")
        print("2 - Listar.")
        print("3 - Excluir.")
        print("4 - Atualizar.")
        print("9 - Voltar ao menu principal.")

        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            excluir_disciplina()
            continue
        elif opcao == "4":
            alterar_disciplina()
            continue
        elif opcao == "9":
            menu()
            continue
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def incluir_disciplina():
    # Implementar a funcionalidade de incluir uma nova disciplina aqui
    codigo = int(input("Informe o código da disciplina: "))
    nome = input("Informe o nome da disciplina: ")
    disciplina = {"codigo": codigo, "nome": nome}
    disciplinas.append(disciplina)
    salvar_disciplina()
    print("Disciplina adicionada com sucesso!")

def listar_disciplinas():
    print("===== LISTAGEM ======")
    if not disciplinas:
        print("Não há disciplinas cadastradas.")
    else:
        for disciplina in disciplinas:
            print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")

def excluir_disciplina():
        # Implementar a funcionalidade de excluir uma disciplina aqui
        codigo = input("Informe o código da disciplina que deseja excluir: ")
        for disciplina in disciplinas:
            if disciplina['codigo'] == codigo:
                disciplinas.remove(disciplina)
                salvar_disciplina
                print("Disciplina removido com sucesso!")
                return
            print("Disciplina não encontrada.")

def alterar_disciplina():
    # Implementar a funcionalidade de editar uma disciplina aqui
    codigo = input("Informe o código da disciplina que deseja editar: ")
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            nome = input(f"Informe o novo nome para a disciplina {codigo}: ")
            disciplina['nome'] = nome
            salvar_disciplina()
            print("Disciplina alterada com sucesso!")
            return
    print("Disciplina não encontrada.")


def menu_professor():
     while True:
        print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")
        print("1 - Incluir.")
        print("2 - Listar.")
        print("3 - Excluir.")
        print("4 - Atualizar.")
        print("9 - Voltar ao menu principal.")

        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            excluir_professor()
            continue
        elif opcao == "4":
            alterar_professor()
            continue
        elif opcao == "9":
            menu()
            continue
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def incluir_professor():
    # Implementar a funcionalidade de incluir um novo professor aqui
    codigo = int(input("Informe o código do professor: "))
    nome = input("Informe o nome do professor: ")
    cpf = input("Informe o CPF do professor: ")
    professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
    professores.append(professor)
    salvar_professor()
    print("Professor adicionado com sucesso!")

def listar_professores():
    print("===== LISTAGEM ======")
    if not professores:
        print("Não há professores cadastrados.")
    else:
        for professor in professores:
            print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")
        
def excluir_professor():
        # Implementar a funcionalidade de excluir um professor aqui
        codigo = input("Informe o código do professor que deseja excluir: ")
        for professor in professores:
            if professor['codigo'] == codigo:
                professores.remove(professor)
                salvar_professor()
                print("Professor removido com sucesso!")
                return
            print("Professor não encontrado.")

def alterar_professor():
    # Implementar a funcionalidade de editar um professor aqui
    codigo = input("Informe o código do professor que deseja editar: ")
    for professor in professores:
        if professor['codigo'] == codigo:
            nome = input(f"Informe o novo nome para o professor {codigo}: ")
            cpf = input(f"Informe o novo CPF para o professor {codigo}: ")
            professor['nome'] = nome
            professor['cpf'] = cpf
            salvar_professor()
            print("Professor alterado com sucesso!")
            return
    print("Professor não encontrado.")



def menu_turma():
    while True:
        print("***** [TURMA] MENU DE OPERAÇÕES *****")
        print("1 - Incluir.")
        print("2 - Listar.")
        print("3 - Excluir.")
        print("4 - Atualizar.")
        print("9 - Voltar ao menu principal.")

        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_turma()
        elif opcao == "2":
            listar_turma()
        elif opcao == "3":
            excluir_turma()
            continue
        elif opcao == "9":
            menu()
            continue
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def incluir_turma():
# Implementar a funcionalidade de incluir uma nova turma aqui
    codigo = int(input("Informe o código da turma: "))
    codigoprof = int(input("Informe o código do professor: "))
    codigodisc = int(input("Informe o código da disciplina: "))

    # Verifica se o código do professor existe na lista de professores
    prof_existe = False
    for professor in professores:
        if professor["codigo"] == codigoprof:
            prof_existe = True
            break
    if not prof_existe:
        print("Código de professor inválido!")
        return

    # Verifica se o código da disciplina existe na lista de disciplinas
    disc_existe = False
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigodisc:
            disc_existe = True
            break
    if not disc_existe:
        print("Código de disciplina inválido!")
        return

    turma = {"codigo": codigo, "codigoprof": codigoprof, "codigodisc": codigodisc}
    turmas.append(turma)
    salvar_turma()
    print("Turma adicionada com sucesso!")

def listar_turma():
    print("===== LISTAGEM ======")
    if not turmas:
        print("Não há turmas cadastradas.")
    else:
        for turma in turmas:
            print(f"Código Turma: {turma['codigo']}, Codigo Professor: {turma['codigoprof']}, Codigo Disciplina: {turma['codigodisc']}")

def excluir_turma():
        # Implementar a funcionalidade de excluir uma turma aqui
        codigo = input("Informe o código da turma que deseja excluir: ")
        for turma in turmas:
            if turma['codigo'] == codigo:
                turmas.remove(turma)
                salvar_turma()
                print("Turma removida com sucesso!")
                return
            print("Turma não encontrada.")


def menu_matricula():
    while True:
        print("***** [MATRICULA] MENU DE OPERAÇÕES *****")
        print("1 - Incluir.")
        print("2 - Listar.")
        print("3 - Excluir.")
        print("4 - Atualizar.")
        print("9 - Voltar ao menu principal.")

        opcao = input("Informe a ação desejada: ")

        if opcao == "1":
            incluir_matricula()
        elif opcao == "2":
            listar_matricula()
        elif opcao == "3":
            excluir_matricula()
        elif opcao == "9":
            menu()
            continue
        else:
            print("Opção inválida. Digite novamente.")

        input("Pressione ENTER para continuar...")

def incluir_matricula():
# Implementar a funcionalidade de incluir uma nova matricula aqui
    codigo = int(input("Informe o código da turma: "))
    codigoestud = int(input("Informe o código do estudante: "))

    # Validação de código de turma
    turma_existe = False
    for turma in turmas:
        if turma["codigo"] == codigo:
            turma_existe = True
            break
    if not turma_existe:
        print("Código de turma inválido!")
        return

    # Validação de código de estudante
    estudante_existe = False
    for estudante in estudantes:
        if estudante["codigo"] == codigoestud:
            estudante_existe = True
            break
    if not estudante_existe:
        print("Código de estudante inválido!")
        return

    matricula = {"codigo": codigo, "codigoestud": codigoestud}
    matriculas.append(matricula)
    salvar_matricula()
    print("Matricula adicionada com sucesso!")

def listar_matricula():
    print("===== LISTAGEM ======")
    if not matriculas:
        print("Não há matriculas cadastradas.")
    else:
        for matricula in matriculas:
            print(f"Código Matricula: {matricula['codigo']}, Codigo Estudante: {matricula['codigoestud']}")

def excluir_matricula():
        # Implementar a funcionalidade de excluir uma matricula aqui
        codigo = input("Informe o código da matricula que deseja excluir: ")
        for matricula in matriculas:
            if matricula['codigo'] == codigo:
                matriculas.remove(matricula)
                salvar_matricula()
                print("Matricula removida com sucesso!")
                return
            print("Matricula não encontrada.")


carregar_disciplina()
carregar_professor()
carregar_estudante()
carregar_matricula()
carregar_turma()
menu()
