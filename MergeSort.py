import math
class MergeSort:

    @staticmethod
    def mergeSort(arr, l, r):

        if l < r:
            # find mid index of arr
            m = (l + r) // 2
            # sort da meade da esquerda do vetor
            MergeSort.mergeSort(arr, l, m)
            # sort da meade da direita do vetor
            MergeSort.mergeSort(arr, m + 1, r)
            # mergir dois vetores
            MergeSort.merge(arr, l, m, r)

    @staticmethod
    def merge(arr, l, m, r):
        # tamanho da metade do array da esquerda
        nL = m - l + 1
        # tamanho da metade do array direita
        nR = r - m
        # criar dois vetores vazios
        L = [0] * (nL + 1)
        R = [0] * (nR + 1)
        #copi metade da esquerda do array  no L[0..LR-1]
        for i in range(0, nL):
            L[i] = arr[l + i]
        # copia metade da direita do array  no R[0..nR-1]
        for j in range(0, nR):
            R[j] = arr[m + 1 + j]

        # COLOCAR INFINITOS VALORES PARA L e R
        L[nL] = math.inf
        R[nR] = math.inf

        # REINICIAR i e j
        i = 0
        j = 0
        for k in range(l, r + 1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1