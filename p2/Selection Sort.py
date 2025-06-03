def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Vantagens:
# - Simples de entender e implementar.
# - Funciona bem para listas pequenas.

# Desvantagens:
# - Ineficiente para listas grandes (complexidade O(n^2)).
# - Muitos swaps desnecessários.