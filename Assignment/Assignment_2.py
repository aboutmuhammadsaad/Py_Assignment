# # problem 1
# print('\nProblem 1')
# num1:int =int(input("Enter the First Number:"))
# num2:int =int(input("Enter the Second Number:"))

# print(f"Sum of two numbers {num1 + num2}")

# # problem 2
# print('\nProblem 2')
# animalname:str = input("What's your favorite animal?  ")
# print(f"My favorite animal is {animalname}!")

# # problem 3
# print('\nProblem 3')
# degrees_fahrenheit =float(input("Enter temperature in Fahrenheit: "))
# degrees_celsius:float = (degrees_fahrenheit - 32) * 5.0/9.0

# print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# # problem 4
# print('\nProblem 4')
# side1:int= int(input("What is the length of side 1?"))
# side2:int= int(input("What is the length of side 2?"))
# side3:int= int(input("What is the length of side 3?"))
# print(f"The perimeter of the triangle is {side1+side2+side3}")

# # problem 5
# print('\nProblem 5')
# num:float =float(input("Type a number to see its square: "))
# print(f"{num} squared is {num*num}") 

# problem 6
print('\nProblem 6')
lis:list[int]=[1, 2, 3, 4, 5]
del lis[3]
print(lis)

# problem 7
print('\nProblem 7')
list1:list[int]=[1,2,3]
list2:list[int]=[4,5,6]
list1.extend(list2)
print(list1)

# problem 8
print('\nProblem 8')
list3:list[int]=[10, 20, 30, 40]
val:int=list3.pop()
print(list3)
print(f"the value removed from the list is: {val}")

# problem 9
print('\nProblem 9')
fruits:list[str]=['red', 'blue', 'green', 'yellow']
print(fruits.index("green"))

# problem 10
print('\nProblem 10')
list3:list[int]=[10, 20, 30, 40]
def get_last_element(lst:list[int]) :
    print(lst[-1])

get_last_element(list3)

def get_values():
    values:list[int] = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)

get_values()