import math
import copy
def divisors(n):
    total = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                total += 1
            else:
                total += 2
        i += 1
    return total

#[ expression if conditional else other thing for this many times ] 

def pow1(a, n):
    if n == 1:
        return a
    return a ** pow1(a, n / 2)

def pow(a, n):
    if n == 1:
        return a
    if (n % 2 == 0):
        y1 = pow(a, n // 2)
        return y1 * y1
    else:
        y1 = pow(a, (n-1) // 2)
        return a * y1 * y1


def fizzbuzz(n):
    lst = []
    for num in range(1, n+1):
        if (num % 3 == 0) & (num % 5 != 0):
            lst.append("Fizz")
        elif (num % 5 == 0) & (num % 3 != 0):
            lst.append("Buzz")
        elif (num % 5 == 0) & (num % 3 == 0):
            lst.append("FizzBuzz")
        else:
            lst.append(num)
    return lst

def middle_me(N, X, Y): 
    mid = N // 2
    str = ''
    for i in range(N+1):
        if i == mid:
            str += X
        else:
            str += Y
    return str

def insurance(age, size, num_of_days): 
    total = 0
    if num_of_days < 0:
        return 0
    if age < 25:
        total += 10 * num_of_days
    if size == 'economy':
        total += 0
    elif size == 'medium':
        total += 10 * num_of_days
    else:
        total += 15 * num_of_days
    total += 50 * num_of_days
    
    return total 

def insurance2(age, size, num_of_days):
    return (50 + (10 if age < 25 else 0) + (10 if size == 'medium' else 0 if size == 'economy' else 15)) * (num_of_days if num_of_days > 0 else 0)


def correctness(bobs_decisions, expert_decisions): 
    total = 0
    for i in range(len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            total += 1
        elif bobs_decisions[i] == '?' or expert_decisions[i] == '?':
            total += 0.5
    return total
            

def descending_order(num):
    lst = [int(x) for x in str(num)]
    lst.sort()
    lst = lst[::-1]
    strlist = [str(i) for i in lst]
    numstr = ''.join(strlist)
    return int(numstr)

#print(descending_order(42145))

def sc(n): 
    lst = []
    for i in range(1, n+1):
        if n % i == 0 and bin(i)[2:] in bin(n)[2:]:
            lst.append(i)
    return lst

def sc2(n):
    return [i for i in range(1, n//2 + 1) if n % i == 0 and bin(i)[2:] in bin(n)[2:]] + [n]

#print(sc2(100))

def digital_sum(n):
    if n == 0:
        return 0
    return n % 10 + digital_sum(int(n / 10))
    

def example3(n):
    i = 1
    sum = 0
    while (i < n*n):
        print(i)
        i *= 2
        sum += i
    return sum 

def tickets(lst):
    total = 0
    ticketprice = 25
    for i in range(len(lst)):
        print(total)
        change = lst[i] - ticketprice
        total += ticketprice
        if total >= change:
            total -= change    
        else:
            return 'NO'
    return 'YES'

def sum_of_integers_in_string(s):
    lst = [int(i) for i in s if i.isdigit()]
    return sum(lst)

def reverse_digits(val):
    new_val = 0
    while val > 0:
        last_digit = val % 10
        new_val = (new_val * 10) + last_digit
        val = val // 10
    return new_val

def m_times_n(m, n):
    if n == 0:
        return 0
    
    return m + m_times_n(m, n-1)


def reverse1(lst):
        low = 0
        high = len(lst) - 1
        while low <= high:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1

def majority_number(lissy):
    dic = {}
    for i in lissy:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for key in dic:
        if dic.get(key) >= (0.5*len(lissy)):
            return key
    

def in_somewhere(lissy, value):
    if type() == int:
        return 0
    else:
        return in_somewhere(lissy[1:], value)

def pr():
    lst1 = [ 1, 2, [ 4, 5]]
    lst2 = lst1
    lst3 = copy.copy(lst1)
    lst4 = copy.deepcopy(lst1)
    lst5 = lst1[ : ]
    lst2[0] = 6
    lst3[1] = 7
    lst5[2][1] = 8
    lst4[2][0] = 9
    print(lst1)
    print(lst2)
    print(lst3)
    print(lst4)
    print(lst5)

def main():
    #print(tickets([25, 25, 25, 100]))
    #print(tickets([25, 25, 25, 25, 50, 100, 50]))
    lst = [1,2,1,[[[2]]],1,4,5,8]
    lst1 = [0,1,5,-1,1,1,-99,1,2,1,1]
    lst2 = [0,1,5,-1,1,99,99,99,99,99,99]
    print(pr())
    #print(lst)

main()