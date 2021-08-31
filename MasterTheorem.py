import math

print("\nMaster Theorem for Divide and Conquer methods\n")
print("\nRunning Time Complexity Equation: T(n) = a.T(n/b)+O((n^k).(log(n)))^p\n")
print("\nGiven a >= 1, b > 1, k >= 0 and p is a real number\n")

a = int(input("\nEnter your value for a: "))
b = int(input("\nEnter your value for b: "))
k = int(input("\nEnter your value for k: "))
p = int(input("\nEnter your value for p: "))

nPow = 0
logPow = 0

print("\nRunning Time Complexity:\n")

if a > pow(int(b),int(k)):
    nPow = round(math.log(a,b))
    print("O(n^"+str(nPow)+")")
elif a == pow(b,k):
    if int(p) > -1:
        nPow = round(math.log(a,b))
        logPow = round(p + 1)
        print("O(n^"+str(nPow)+"*(log(n))^"+str(logPow)+")")
        # nPow = pow(n,math.log(a,b))*pow(math.log(n),(p+1))
    elif p == -1:
        nPow = round(math.log(a,b))
        print("O(n^"+str(nPow)+"*log(log(n)))")
        #logPow = math.log(math.log(n))
        #nPow = pow(n,math.log(a,b))*math.log(math.log(n)))
    elif p < -1:
        #nPow = pow(n,math.log(a,b)
        nPow = round(math.log(a,b))
        print("O(n^"+str(nPow)+")")
elif a < pow(b,k):
    #print("\n3a\n")
    if p >= 0:
        nPow = round(k)
        logPow = round(p)
        if logPow == 0:
            print("O(n^"+str(k)+")")
        else:
            print("O(n^"+str(k)+"*(log(n))^"+str(p)+")")
    else:
        nPow = k
        print("O(n^"+str(k)+")")

#print(output)
