# problem 1
print('\nProblem 1')
anton_age=21
beth_age=anton_age+6
chen_age=beth_age+20
drew_age=chen_age+anton_age
ethan_age=chen_age
print(f'Anton is {anton_age} ')
print (f'Beth is {beth_age} ')
print (f'Chen is {chen_age}')
print(f'Drew is {drew_age}')
print(f'Ethan is {ethan_age}')

# Problem 2
print('\nProblem  2')
name:str = "Alice"
age:int = 30
city:str = "New York"
print (f'{name} is {age} years old and lives in {city}')


# Problem 3
print('\nProblem 3')
s:str = "hElLo WoRlD"
print (s.capitalize())
print(s.upper())
print(s.lower())

# Problem 4
print('\nProblem 4')
s:str ="the quick brown fox jumps over the lazy dog"
print (f"index of 'fox' is {s.find('fox')}")
print (f"'the' appears {s.count('the')} times")

# Problem 5
print('\nProblem 5')
s:str ="I love programming in Python"
print(s.replace('Python','Java'))

# Problem 6
print('\nProblem 6')
s:str ="apple,banana,cherry,dates"
print (s.split(','))
print (s.replace(',', ' '))

# Problem 7
print('\nProblem 7')
s:str ="   Python is fun!   "
print(s)
print(s.strip())
print(s.strip().ljust(20,'*'))
print(s.strip().rjust(20,'*'))

#Problem 8
print('\nProblem 8')
num:int=45
print(f'Binary representation : {bin(num)}')

#Problem 9
print('\nProblem 9')
base:int = 3
exponent:int = 4
print(f'Power result: {base ** exponent}')

#problem 10 
print('\nProblem 10')
value:float = 12.34567

print(f'Rounded to nearest integer: {round(value)}')
print(f'Rounded to two decimal places: {round(value,2)}')

