# criar sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas;
    # alunos: nome, matricula, data de nascimento, sexo, endereço, telefone, email.
    # professores: nome, matricula, data de nascimento, sexo, endereço, telefone, email, disciplina.
    # disciplinas: nome, codigo(A1234), carga horaria, professor. 
    # turmas: nome, codigo (A1234), disciplina, professor, aluno (lista-matricula).

    # O sistema deve permitir a filtragem de professores por disciplina

# o sistema deve permitir a matricula de alunos em turmas
# O sistema deve permitir a alocação de professores em disciplinas
# o sistema deve permitir a alocação de disciplinas em turmas
# o sistema deve permitir a consulta de alunos matriculados em turmas
# o sistema deve permitir a consulta de professores alocados em disciplinas
# o sistema deve permitir a consulta de disciplinas alocadas em turmas
# CHATGPT : Refatorar o codigo para que ele fique mais organizado

#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------

alunos = []
professores = []
disciplinas = []
turmas = []

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno: ")
    sexo = input("Digite o sexo do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o numero do aluno: ")
    email = input("Digite o email do aluno: ")
    return {'nome': nome, 'matricula': matricula, 'data_nascimento': data_nascimento, 
            'sexo': sexo, 'endereco': endereco, 'telefone': telefone, 'email': email}

def cadastro_professor():
    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matricula do professor: ")
    data_nascimento = input("Digite a data de nascimento do professor: ")
    sexo = input("Digite o sexo do professor: ")
    endereco = input("Digite o endereço do professor: ")
    telefone = input("Digite o numero do professor: ")
    email = input("Digite o email do professor: ")
    disciplina = input("Digite a disciplina que o professor leciona: ")
    return {'nome': nome, 'matricula': matricula, 'data_nascimento': data_nascimento, 
            'sexo': sexo, 'endereco': endereco, 'telefone': telefone, 'email': email, 'disciplina': disciplina}

def cadastro_disciplina():
    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o codigo da disciplina: ")
    carga_horaria = input("Digite a carga horaria da disciplina: ")
    professor = input("Digite o nome do professor responsável pela disciplina: ")
    return {'nome': nome, 'codigo': codigo, 'carga_horaria': carga_horaria, 'professor': professor}

def cadastro_turma():
    nome = input("Digite o nome da turma: ")
    codigo = input("Digite o codigo da turma: ")
    disciplina = input("Digite a disciplina da turma: ")
    professor = input("Digite o nome do professor: ")
    alunos_matriculados = input("Digite as matriculas dos alunos separados por vírgula: ").split(",")
    return {'nome': nome, 'codigo': codigo, 'disciplina': disciplina, 'professor': professor, 'alunos': alunos_matriculados}

def matricular_aluno_em_turma():
    matricula_aluno = input("Digite a matrícula do aluno: ")
    codigo_turma = input("Digite o código da turma: ")
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            turma['alunos'].append(matricula_aluno)
            print(f"Aluno {matricula_aluno} matriculado na turma {codigo_turma}.")
            return
    print("Turma não encontrada")

def alocar_professor_em_disciplina():
    matricula_professor = input("Digite a matrícula do professor: ")
    codigo_disciplina = input("Digite o código da disciplina: ")
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo_disciplina:
            disciplina['professor'] = matricula_professor
            print(f"Professor {matricula_professor} alocado à disciplina {codigo_disciplina}.")
            return
    print("Disciplina não encontrada")

def alocar_disciplina_em_turma():
    codigo_turma = input("Digite o código da turma: ")
    codigo_disciplina = input("Digite o código da disciplina: ")
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            turma['disciplina'] = codigo_disciplina
            print(f"Disciplina {codigo_disciplina} alocada à turma {codigo_turma}.")
            return
    print("Turma não encontrada")

def consultar_alunos_matriculados():
    codigo_turma = input("Digite o código da turma para consultar alunos matriculados: ")
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            print(f"Alunos matriculados na turma {codigo_turma}: {', '.join(turma['alunos'])}")
            return
    print("Turma não encontrada")

def consultar_professores_alocados():
    codigo_disciplina = input("Digite o código da disciplina para consultar o professor alocado: ")
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo_disciplina:
            print(f"Professor alocado à disciplina {codigo_disciplina}: {disciplina['professor']}")
            return
    print("Disciplina não encontrada")

def consultar_disciplinas_alocadas():
    codigo_turma = input("Digite o código da turma para consultar disciplinas alocadas: ")
    for turma in turmas:
        if turma['codigo'] == codigo_turma:
            print(f"Disciplina alocada à turma {codigo_turma}: {turma['disciplina']}")
            return
    print("Turma não encontrada")

#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------

# Menu 
def exibir_menu():
    while True:
        print("\nMenu de opções:")
        print("0 - Sair")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar professor")
        print("3 - Cadastrar disciplina")
        print("4 - Cadastrar turma")
        print("5 - Matricular aluno em uma turma")
        print("6 - Alocar professor em disciplina")
        print("7 - Alocar disciplina em turma")
        print("8 - Consultar alunos matriculados em turma")
        print("9 - Consultar professores alocados em disciplina")
        print("10 - Consultar disciplinas alocadas em turma")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 0:
            print("Saindo do sistema...")
            break
        elif opcao == 1:
            alunos.append(cadastro_aluno())
        elif opcao == 2:
            professores.append(cadastro_professor())
        elif opcao == 3:
            disciplinas.append(cadastro_disciplina())
        elif opcao == 4:
            turmas.append(cadastro_turma())
        elif opcao == 5:
            matricular_aluno_em_turma()
        elif opcao == 6:
            alocar_professor_em_disciplina()
        elif opcao == 7:
            alocar_disciplina_em_turma()
        elif opcao == 8:
            consultar_alunos_matriculados()
        elif opcao == 9:
            consultar_professores_alocados()
        elif opcao == 10:
            consultar_disciplinas_alocadas()
        


exibir_menu()
