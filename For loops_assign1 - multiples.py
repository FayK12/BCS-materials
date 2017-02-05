#this code prints multiples of 3, 5 or 3&5 for all numbers between 1-100

for i in range(1,101):
    if ((i%3 ==0) and (i%5 ==0)):
        print("FizzBuzz")
    elif (i%3 ==0):
        print("Fizz - I'm a multiple of 3")
    elif (i%5 ==0):
        print("Buzz - I'm a multiple of 5")
    else:
        print(i)
    
    
