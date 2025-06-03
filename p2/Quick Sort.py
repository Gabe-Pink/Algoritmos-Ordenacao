def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Vantagens:
# - Complexidade O(n log n) na maioria dos casos.
# - Rápido e eficiente na prática.

# Desvantagens:
# - Pode ter pior caso O(n^2) se o pivô for mal escolhido.
# - Não é estável por padrão.