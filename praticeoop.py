def outer(arg):
    def inner(val1,val2):
        if val1==0 and val2==0:
            return("not possible")
        if val2==0:
            # temp=val1
            # val1=val2
            # val2=temp 
            val1,val2=val2,val1
        return arg(val1,val2)       
    return inner
   
@outer 
def add(num1,num2):
    return num1/num2
print(add(2,4))
print(add(2,0))
print(add(0,2))
print(add(0,0))



# a=4
# b=3
# a,b=b,a
# print(a,b)