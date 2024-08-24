
name:str=input("Enter your name: ")
num1:int=int(input("Enter your first favorite number: ")) 
num2:int=int(input("Enter your second favorite number: ")) 
num3:int=int(input("Enter your third favorite number: ")) 
numbers:list[int]=[num1, num2, num3]
numbertype:list=[]

print(f"Hello, {name}! Let's explore your favorite numbers:")

for number in numbers:
    if (number % 2 == 0):
        numbertype.append((number,"even"))
        print(f"The number {number} is even")
    else:
        numbertype.append((number,"odd"))
        print(f"The number {number} is odd")


for number in numbers:
    print(f"The number {number} and its square: ({number}, {number*number})")

for number in numbers:
    sum=number+number

print(f"Amazing! The sum of your favorite numbers is: {sum}")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if is_prime(sum):
    print(f"Wow, {sum}  is a prime number!")



