def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Vantagens:
# - Bom para listas pequenas ou parcialmente ordenadas.
# - Funciona bem para inserção de elementos em listas ordenadas.

# Desvantagens:
# - Ineficiente para listas grandes (complexidade O(n^2)).
# - Não é adequado para grandes conjuntos de dados.