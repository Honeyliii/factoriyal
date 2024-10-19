number=int(input("ples you number:"))
factorial = 1
if  number<=0:
    print('no factorial')
else:
    for i in range(1, number+1):
        factorial = factorial* i
        
    
    print('fact number :', number, ':', factorial)        