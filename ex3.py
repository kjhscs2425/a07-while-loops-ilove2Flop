def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = 5 #Idc what number u put here it workz :) there is a max recusion depth :(
print(f"The factorial of {n} is: {factorial(n)}")
