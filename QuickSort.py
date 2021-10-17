class QuickSort:

    @staticmethod
    def troca(array,i,j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp


    @staticmethod
    def quicksort(array,p,r):
        if p<r:
            q = QuickSort.partition(array,p,r)
            QuickSort.quicksort(array,p,q-1)
            QuickSort.quicksort(array,q+1,r)

    @staticmethod
    def partition(array, start,end):
        x = array[end]
        i = start -1
        for j in range(start, end):
            if (array[j] <= x):
                i = i+1
                QuickSort.troca (array,i,j)
        QuickSort.troca(array,i+1, end)
        return i+1