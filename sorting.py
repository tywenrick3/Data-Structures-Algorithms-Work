def merge(srt_lst1, srt_lst2, lst):
    i = j = 0
    while i + j < len(lst):
        if (j == len(srt_lst2)) or (i < len(srt_lst1) and srt_lst1[i] < srt_lst2[j]):
            lst[i+j] = srt_lst1[i]
            i += 1
        else:
            lst[i+j] = srt_lst2[j]
            j += 1
    
def merge_sort(lst):
    n = len(lst)

    if n < 2:
        return
    
    mid = n // 2
    lst_first_half = lst[0:mid] #theta(n)
    lst_2nd_half = lst[mid:n] #theta(n)

    merge_sort(lst_first_half)
    merge_sort(lst_2nd_half)

    merge(lst_first_half, lst_2nd_half, lst)



def selection_sort(lst):
    # Traverse through all array elements
    for i in range(len(lst)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        
    return lst



def insertion_sort(lst):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(lst)):
  
        key = lst[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    
    return lst



def main():
    lst1 = [18, 34, 2, 6, 10, 9, 43, 22, 1, 90]
    merge_sort(lst1)
    print(lst1)

main()