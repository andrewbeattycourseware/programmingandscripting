N = float(input("Enter positive number you are looking for approximate sqrt for  "))
if N <= 0:
    print("Please run program again and select positive number")

def new_raph(N):
    print(N)
    x0 = N/2
    while 0 < x0 == N:
        print ("in while")
        fxn = (x0**2) - N
        fpxn = (2*x0)
        x1 = x0 - (fxn) / (fpxn)
        if fxn <= 0.1:
            print(format(x1,'.2f'))
            break
        else:
            x0 = x1

new_raph(N)