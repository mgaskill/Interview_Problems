'''
Fibonacci - each number equals the sum of the two preceding numbers.

Fn = Fn-1 + Fn-2

Given a number, provide the fibonacci result in the sequence starting with 0

Challenge: account for negative or fraction numbers 

'''

#recursive solution - assumes no negatives or fractions entered and starting at 0
def fib_iteration(num): #create a list and then sum at the end
    alist = []
    first = 0
    second = 1
    while num >= 0:
        alist.append(first)
        num -= 1
        first, second = second, (first + second)
    return alist[num]

def fib_recursive(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    else:
        return fib_recursive(num-1) + fib_recursive(num-2)  


#test 
implementations = [fib_iteration, fib_recursive]

for impl in implementations:
    print "trying %s" % impl
    print "  f(0) == 0: %s" % (impl(0) == 0)
    print "  f(1) == 1: %s" % (impl(1) == 1)
    print "  f(2) == 1: %s" % (impl(2) == 1)
    print "  f(3) == 2: %s" % (impl(3) == 2)
    print "  f(6) == 8: %s" % (impl(6) == 8)
    print "  f(13) == 233: %s" % (impl(13) == 233)

