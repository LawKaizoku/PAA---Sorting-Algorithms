class HeapSort:

# Para refazeer heap da subárvore enraizada no índice i.

    def heap(arr, n, i):
        maior = i  # Inicializar o maior como raiz
        l = 2 * i + 1     # esquerda = 2*i + 1
        r = 2 * i + 2     #  direita = 2*i + 2
        # Veja se o filho esquerdo do root existe e é
        # maior que a raiz
        if l < n and arr[i] < arr[l]:
            maior = l
        # Veja se o filho certo do root existe e é maior que a raiz
        if r < n and arr[maior] < arr[r]:
            maior = r
        # Mude a raiz
        if maior != i:
            arr[i],arr[maior] = arr[maior],arr[i]  # troca

            # refaz Heap  a raiz.
            HeapSort.heap(arr, n, maior)

    # função principal

    def heapSort(arr):
        n = len(arr)

        # Construa um maxheap.
        # Como o último pai estará em ((n // 2) -1).
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heap(arr, n, i)

        # Um por um extraia elementos
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # troca
            HeapSort.heap(arr, i, 0)