def divider():
    while True:
        nums=input('Enter 2 digits (format: x y):')
        (x,y)=nums.split()
        try:
            print(float(x)/float(y))
        except ZeroDivisionError:
            print('Division by zero')
        except ValueError:
            print('Don not use letters')


divider()