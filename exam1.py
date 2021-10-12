def ranged_sorted(lissy, low, high):
    if low >= high:
        return True #basecase
    if lissy[low] >= lissy[low+1]:
        return ranged_sorted(lissy, low+1, high)

    return False
    #runtime is theta(n) becuase the amount of recursive calls depend on the length of lissy and the area of intrest (low and high)

def main():
    print(ranged_sorted([100,-50,8, 2], 0, 3))

    print(ranged_sorted([500,650,100,80,350], 1, 3))

main()
