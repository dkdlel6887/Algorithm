N = int(input())
arr = list(map(int, input().split()))
Mid_num = int(N/2)
def bubbleSort(arr):
    for i in range(N-1, 0, -1): # 198, 197, 196, ..., 2, 1
        for j in range(i):  # 0, 1, ..., 198
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(v):
    for i in range(1, N):
        j, key = i-1, v[i]
        while v[j] > key and j >= 0:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = key
    return v

# insertionSort(arr)
bubbleSort(arr)
print(arr)
print(arr[Mid_num])