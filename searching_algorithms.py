import math

#linear search
def linear_search(lst, val):
    for i in range(len(lst)): #theta(n)
        if lst[i] == val:
            return i
    return None # theta(1)

def linear_search_test():
    lst = [5, 8, 12, 7, 8, 10]
    print(linear_search(lst, 10))



#binary-search 
def binary_search(srt_lst, val):
    left = 0
    right = len(srt_lst) - 1
    index = None # everything above while loop: theta(1)
    found = False
    while not found and left <= right: # theta(logbase2(n))
        mid = (left + right) // 2
        if srt_lst[mid] == val:
            index = mid
            found = True # everything in while loop: theta(1)
        elif val < srt_lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return index # theta(1)


def bin_search_test():
    lst = [5, 7, 8, 8, 10, 12]
    print(binary_search(lst, 10))

#bin_search()
#search()



