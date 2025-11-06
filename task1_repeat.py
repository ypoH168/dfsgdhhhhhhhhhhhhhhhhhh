def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
print(square(5))
