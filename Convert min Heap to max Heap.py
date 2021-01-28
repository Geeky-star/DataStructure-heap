
def maxHeapify(arr,i,n):

    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left]>arr[i]:
        largest = left

    if right<n and arr[right]>arr[largest]:
        largest = right

    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        maxHeapify(arr,largest,n)


def convertMaxHeap(arr,n):

    for i in range(int((n-2)/2),-1,-1):
        maxHeapify(arr,i,n)

def printArray(arr,size):
    for i in range(size):
        print(arr[i],end = " ")
    print()


arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]  
n = len(arr) 
  
print("Min Heap array : ")  
printArray(arr, n)  
  
convertMaxHeap(arr, n)  
  
print("Max Heap array : ")  
printArray(arr, n) 

