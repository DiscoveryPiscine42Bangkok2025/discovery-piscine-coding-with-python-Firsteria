start = int(input("Enter a number less than 25: "))

if start < 25:
    for i in range(start, 26, 1):
        print("Inside the loop, my variable is " +str(i))
else:
    print("Error")