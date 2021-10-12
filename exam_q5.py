def remove_numbers(list1):
    i = 0
    while i < len(list1):
        if list1[i].isdigit(): 
            del list1[i]
            i -= 1 # because using del eveything shifts left
        i += 1

    return list1
        
    #runtime complexity of theta(n) becuase we are iterating through each element of list1



def main():
    list1= ['2', 'a', '5', '5', 'b', 'y', '1' , 'g']
    remove_numbers(list1)
    print(list1)
    [ 'g', 'a', 'y', 'b']   # [ 'a', 'b', 'y', 'g'] is also fine, as order does not matter

main()