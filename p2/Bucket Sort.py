def bucket_sort(arr):
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    return [num for bucket in buckets for num in bucket]

# Vantagens:
# - Muito eficiente para dados uniformemente distribuídos.
# - Complexidade O(n) no melhor caso.

# Desvantagens:
# - Depende fortemente da distribuição dos dados.
# - Não é ideal para dados muito dispersos.