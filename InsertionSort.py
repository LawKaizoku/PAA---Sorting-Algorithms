class InsertionSort:
    def insertionSort(alist):
        n = len(alist)
        for i in range(1,n):
            chave = alist[i]
            j = i -1
            while j >= 0 and alist[j] > chave:
                alist[j+1] = alist[j]
                j = j -1
            alist[j+1] = chave


        pass