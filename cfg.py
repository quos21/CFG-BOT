n = int(input("Enter the number of terms: "))
t1 = 0
t2 = 1
nextTerm = t1 + t2
print("Fibonacci Series: {}, {}".format(t1, t2))
for i in range(3, n+1):
    print("{}, ".format(nextTerm), end="")
    t1 = t2
    t2 = nextTerm
    nextTerm = t1 + t2