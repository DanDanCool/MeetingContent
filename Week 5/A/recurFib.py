def f(n):
    if(n == 0): # base case 1 (f(0) = 1)
        return 1
    if(n == 1): # base case 2 (f(1) = 1)
        return 1
    return f(n-1) + f(n-2) # recurrence (nth term is equal to the sum of two previous terms)
# this goes to 11
