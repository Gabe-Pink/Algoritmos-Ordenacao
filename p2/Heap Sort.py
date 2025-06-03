import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Vantagens:
# - Complexidade O(n log n).
# - Usa uma estrutura de dados de heap eficiente.

# Desvantagens:
# - Não é estável.
# - Mais complexo de implementar.