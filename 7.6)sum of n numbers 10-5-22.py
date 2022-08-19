
#sum of natural numbers
n=int(input("Enter number :"))
sum=0
fact=1
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum)


#factorial
for j in range(1,n+1):
    fact=fact*j
print("factorial is=",fact)

#functions
def fname():
    return("Hello world")
print(fname())

#factorial by function
def factorial(num):
    fact=1
    for j in range(1,num+1):
        fact=fact*j
    return(fact)
print(factorial(3))

#power function by recurrsion
def power(x,n):
    if(n==0):
        return 1
    else :
        return x*power(x,n-1)
print(power(2,3))

#fibnocci by recurrsion
def fibnocci(number):
    if(number<=1):
        return number
    else:
        return(fibnocci(number-1)+fibnocci(number-2))
nterms=int(input("How many terms :"))
for i in range(nterms):
    print(i)
print(fibnocci(nterms))
