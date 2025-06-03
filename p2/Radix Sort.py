def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

# Vantagens:
# - Muito rápido para números inteiros.
# - Complexidade O(n).

# Desvantagens:
# - Funciona melhor para números inteiros.
# - Requer múltiplas passagens pelos dados.