def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Vantagens:
# - Simples de implementar.
# - Pode detectar se a lista já está ordenada (versão otimizada).

# Desvantagens:
# - Muito ineficiente para listas grandes (complexidade O(n^2)).
# - Realiza muitas comparações desnecessárias.