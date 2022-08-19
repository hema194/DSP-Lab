n=int(input("Enter base value:"))
x=int(input("Power value:"))
def power(n,x):
          if(n==0):
                    return 1
          else:
                    return(x*power(x,n-1))
print(power(n,x))
