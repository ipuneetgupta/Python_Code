# QuickSort.py
def Quicksort(arr,low,high):

    if(low>=high):
         return
    parition_idx=Pivot(arr,low,high)
    Quicksort(arr,low,parition_idx-1)
    Quicksort(arr,parition_idx+1,high)

    return

def Pivot(arr,low,high):
    se=low-1
    pivot_idx=arr[high]
    for i in range(low,high):
        if arr[i]<=pivot_idx:
            se+=1
            arr[i],arr[se]=arr[se],arr[i]

    arr[se+1],arr[high]=arr[high],arr[se+1]
    se+=1
    return se

arr=[int(n) for n in input().split()]
Quicksort(arr,0,len(arr)-1)
print(arr)