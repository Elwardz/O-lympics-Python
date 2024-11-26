import pandas as pd

#-> El, Vamos criar as listas de Perguntas

questions = [
    # O(1) - Complexidade constante
    [
        """def caixeiro_viajante(cidades):
    if len(cidades) == 1:
        return cidades
    resultado = []
    for i in range(len(cidades)):
        rest = cidades[:i] + cidades[i+1:]
        for x in caixeiro_viajante(rest):
            resultado.append([cidades[i]] + x)
    return resultado """,
        "O(n!) - Fatorial",
        "O(n) - Linear",
        "O(log n) - Logarítmica",
        "O(n^2) - Quadrática",
        1  
    ],
    [
        """def busca_solucoes(n):
    if n == 0:
        return 1
    return busca_solucoes(n-1) + busca_solucoes(n-1) """,
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        "O(2^n) - Exponencial",
        4 
    ],
    [
        """def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in range(n):
        for v in graph[u]:
            dist[u][v] = graph[u][v]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist """,
        "O(n) - Linear",
        "O(n^3) - Cúbica",
        "O(n^2) - Quadrática",
        "O(log n) - Logarítmica",
        2  
    ],

   
    [
        """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr """,
        "O(log n) - Logarítmica",
        "O(1) - Constante",
        "O(n) - Linear",
        "O(n^2) - Quadrática",
        4  
    ],
    [
        """def ordenar_tuplas(lista):
    return sorted(lista, key=lambda x: x[1])""",
        "O(n^2) - Quadrática",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n log n) - Linear-Logarítmica",
        4  
    ],
    [
        """def e_primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True""",
        "O(n) - Linear",
        "O(n^2) - Quadrática",
        "O(log n) - Logarítmica",
        "O(1) - Constante",
        3  
    ],

  
    [
        """def verifica_par(valor):
    return valor % 2 == 0""",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        "O(log n) - Logarítmica",
        2 
    ],
    [
        """def acessar_elemento(lista, index):
    return lista[index]""",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        "O(log n) - Logarítmica",
        2  
    ],
    [
        """def busca_binaria(arr, x):
    esquerda, direita = 0, len(arr) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1 """,
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        "O(log n) - Logarítmica",
        4  
    ],

 
    [
        """def soma_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma""",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        "O(n log n) - Linear-logarítmica",
        1  

    ],
    [
        """def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado """,
        "O(n log n) - Linear-logarítmica",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        
        1  
    ],
    [
        """def multiplicar_matrizes(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result""",
        "O(1) - Constante",
        "O(n log n) - Linear-logarítmica",
        "O(n) - Linear",
        "O(n^2) - Quadrática",
        4  
    ], 

    
    [
        """def multiplicar_matrizes_3D(A, B, C):
    result = [[[0 for _ in range(len(C[0][0]))] for _ in range(len(C[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(C[0][0])):
                result[i][j][k] = A[i][j][k] * B[i][j][k] * C[i][j][k]
    return result""",
        "O(n^3) - Cúbica",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(log n) - Logarítmica",
        1  
    ],
    [
        """def gerar_subconjuntos(s):
    if len(s) == 0:
        return [[]]
    else:
        subconjuntos = gerar_subconjuntos(s[1:])
        return subconjuntos + [[s[0]] + x for x in subconjuntos]""",
        "O(n^2) - Quadrática",
        "O(2^n) - Exponencial",
        "O(1) - Constante",
        "O(log n) - Logarítmica",
        2  
    ],
    [
        """
import itertools
def permutacoes_lista(lista):
    return list(itertools.permutations(lista))""",
        "O(n^2) - Quadrática",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n!) - Fatorial",
        4  
    ],

    [
        """
def buscar_tripletos(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            for k in range(j + 1, len(lista)):
                print(lista[i], lista[j], lista[k])
""",
        "O(n^3) - Cúbica",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        1  
    ],
    [
        """
def gerar_permutacoes(lista):
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        rest = lista[:i] + lista[i+1:]
        for x in gerar_permutacoes(rest):
            resultado.append([lista[i]] + x)
    return resultado""",
        "O(n^3) - Cúbica",
        "O(n^2) - Quadrática",
        "O(1) - Constante",
        "O(n!) - Fatorial",
        4  
    ],

    [
        """
def atribuir_variavel(valor):
    a = valor
    return a""",
        "O(2^n) - Exponencial",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        3  
    ],
    [
        """
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivot]
    meio = [x for x in arr if x == pivot]
    direita = [x for x in arr if x > pivot]	
    return quick_sort(esquerda) + meio + quick_sort(direita)""",
        "O(2^n) - Exponencial",
        "O(1) - Constante",
        "O(n log n) - Linear-logarítmica",
        "O(n) - Linear",
        3  
    ],
    [
        """
def contar_pares(lista):
    contagem = 0
    for num in lista:
        if num % 2 == 0:
            contagem += 1
    return contagem """,
        "O(n!) - Fatorial",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        2  
    ],
    [
        """
def divisao_recursiva(n):
    if n <= 1:
        return n
    return divisao_recursiva(n // 2) + 1""",
        "O(log n) - logarítmica",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        1  
    ],

    [
        """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)""",
        "O(2^n) - Exponencial",
        "O(n!) - Fatorial",
        "O(n^2) - Quadrática",
        "O(n^3) - Cúbica",
        1  
    ],
    [
        """
def pares_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            print(lista[i], lista[j]) """,
        "O(n^n) - Superexponencial",
        "O(n) - Linear",
        "O(1) - Constante",
        "O(n^2) - Quadrática",
        4  
    ]
]

# 2parte - criar dataframe do pandas

df = pd.DataFrame(questions, columns=["Perguntas", "Opcao 1", "Opcao 2","Opcao 3","Opcao 4","Resposta Correta"])

#3 - Salva no Arquivo Excel

df.to_excel("questions.xlsx", index=False)

print("perguntas inseridas com sucesso")