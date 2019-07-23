def pn(num):
    for i in range(2, (num-1)):
        if num%i==0:
            print("number is not proime as num {} is divisble by {}".format(num,i))

            break


pn(5)
