def statement():
    print('''
A Universidade HackerLand tem a seguinte política de notas:

Cada aluno recebe uma nota entre 0 e 100.
Notas abaixo de 40 são reprovadas.

Sam, o professor, arredonda as notas da seguinte forma:

1. Se a diferença para o próximo múltiplo de 5 for menor que 3, arredonda
   para esse múltiplo.
2. Se a nota for abaixo de 38, não arredonda, pois ainda é reprovado.

Exemplos:
- Nota = 84 arredonda para 85 (85 - 84 < 3)
- Nota = 29 não arredonda (é < 40)
- Nota = 57 não arredonda (60 - 57 >= 3)

Dado o valor inicial das notas dos n alunos, escreva um código para
automatizar o arredondamento.

Descrição da Função
Complete a função `gradingStudents` no editor abaixo.
`gradingStudents` tem o(s) seguinte(s) parâmetro(s):
- `int grades[n]`: notas antes do arredondamento

Retorna
- `int[n]`: notas após o arredondamento

Formato de Entrada
A primeira linha contém um inteiro, n, o número de alunos.
Cada uma das n linhas seguintes contém um inteiro, `grade[i]`.

Restrições
- 1 <= n <= 60
- 0 <= grades[i] <= 100

Entrada de Exemplo 0:
4
73
67
38
33

Saída de Exemplo 0:
75
67
40
33

Explicação 0:
- Nota 73 arredonda para 75 (75 - 73 < 3)
- Nota 67 não arredonda (70 - 67 = 3)
- Nota 38 arredonda para 40 (40 - 38 < 3)
- Nota 33 não arredonda (abaixo de 40)
''')


def gradingStudents(grades):
    return 0


if __name__ == '__main__':

    statement()

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
