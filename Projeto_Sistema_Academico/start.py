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

def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    data_nascimento = input("Digite a data de nascimento do aluno: ")
    sexo = input("Digite o sexo do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o numero do aluno: ")
    email = input("Digite o email do aluno: ")
    return{'nome ': nome, 'matricula':matricula, 'data_nascimento':data_nascimento, 'sexo': sexo, 'endereço': endereco, 'telefone:': telefone, 'email':email}

def cadastro_professor():
    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matricula do professor: ")
    data_nascimento = input("Digite a data de nascimento do professor: ")
    sexo = input("Digite o sexo do professor: ")
    endereco = input("Digite o endereço do professor: ")
    telefone = input("Digite o numero do professor: ")
    email = input("Digite o email do professor: ")
    disciplina = input("Digite a disciplina que o professor leciona")
    return {'nome ': nome, 'matricula':matricula, 'data_nascimento':data_nascimento, 'sexo': sexo, 'endereço': endereco, 'telefone': telefone, 'email':email, 'disciplina':disciplina}

def cadastro_disciplina():
    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o codigo da disciplna: ")
    carga_horaria = input("Digite a carga horaria da disciplina: ")
    professor = input("Digite o nome do professor: ")
    return {'nome':nome, 'codigo':codigo, 'carga horaria':carga_horaria, 'professor':professor}

def cadastro_turma():
    nome = input("Digite o nome da turma: ")
    codigo = input("Digite o codigo da turma: ")
    disciplina = input("Digite as disciplinas da turma: ")
    professor = input("Digite o nome dos professores")
    aluno = input("Digite o nome dos alunos: ")    
    return {'nome': nome, 'codigo':codigo, 'disciplina':disciplina, 'professor':professor, 'aluno': aluno}