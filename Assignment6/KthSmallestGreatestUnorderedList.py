def heapify (array, n, k):
    greatest = k 
    left = 2*k + 1
    right = 2*k + 2

    if left < n and array[k] < array[left]:
        greatest = left
 
    if right < n and array[greatest] < array[right]:
        greatest = right

    if greatest != k :
        array[greatest],array[k] = array[k],array[greatest]

def max_heap(array,n): 
    
    for i in range(n, -1, -1): 
        heapify(array, n, i) 
  
    for num in range(n-1, -1, -1): 
        #swap between two element 
        array[num], array[0] = array[0], array[num] 
        heapify(array,num, 0) 
        
li = [ 12, 11, 13, 5, 6, 7] 
max_heap(li, len(li)) 
k = int(input("k:- "))
choice = input("1 : Kth Smallest\n2 : Kth Largest\n")
if choice == '1':
    print(li[k-1]) 
elif choice == '2':
    print(li[-k])
else:
    print("Wrong Input")