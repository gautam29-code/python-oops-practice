def outer(arg):
    def inner(val1,val2):
        if val1<0:
            val1=val1*(-1)
        if val2<0:
            val2=val2 *(-1)  
        arg(val1,val2)
            
        
        
    return inner
   
@outer 
def add(num1,num2):
    print(num1+num2)
add(2,-4)
add(-5,2)
add(-5,-2)