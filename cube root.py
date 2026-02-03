import math
n=int(input("enter a number: "))
if 0<n<10:
    print(n**2)

elif 10<=n<100:
        print(math.sqrt(n))
elif 100<=n<1000:
            print(math.cbrt(n))
else:
                print("invalid")
