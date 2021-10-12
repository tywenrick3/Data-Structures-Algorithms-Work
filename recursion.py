#recursion examples
def count(index):
    print(index)
    if index < 2:
        count(index + 1) #recursion occurs here
    return 

def upAndDown(n):
    print("level:", n)
    if n < 4:
        upAndDown(n+1) #recursion occurs here
    print("LEVEL:", n)
    return 

def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1

    return n * fact(n-1) #recursion occurs here

def count_up(start, end):
    if(start == end):
        print(end)
    else:
        count_up(start, end - 1) #recursion occurs here
        print(end)

def count_up3(start, end):
    if (start == end):
        print(end)
    else:
        mid = (start + end) // 2
        count_up3(start, mid) #recursion occurs here
        count_up3(mid+1, end) #recursion occurs here



def reverse_list(lst):
    """
    : lst type: list[]
    : return type: None
    """
    return [i for i in lst[::-1]]

#print(reverse_list([1,2,3,4,5]))

def sum_to(n):
    """
    : n type: int
    : return type: int
    """
    if n < 0:
        return 0
    else:
        return n + sum_to(n-1)

#print(sum_to(3))


def func1(n): #for tracing: n = 16
    if (n <= 1):
        return 0
    else:
        return 10 + func1(n-2)



def func2(n): #for tracing: n = 16
    if (n <= 1):
        return 1
    else:
        return 1 + func2(n//2)

    

def main():
    #count(0)
    #upAndDown(1)
    #print(fact(3))
    #count_up(1, 5)
    count_up3(1, 5)
    
main()