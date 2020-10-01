#fizzbuzz interview que
n = int(input("enter the number :"))
def fizzbuzz(n):
    if n<0 or n>(2*10**5):
        return None
    else:
        for i in range (1, n+1):
            if i%3==0 and i%5==0:
                print("FizzBuzz")
            elif i%3==0:
                print("Fizz")
            elif i%5==0:
                print("Buzz")
            else:
                print(i)
fizzbuzz(65)   
