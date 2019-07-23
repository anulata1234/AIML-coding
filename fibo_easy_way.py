
def fibo():  
    num1 =0
    num2 = 1

    for i in range(0,10):
       num = num2+num1
       num1=num2
       num2 = num 
       print (num)

fibo()
