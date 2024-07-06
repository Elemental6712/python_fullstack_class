def fibonacci_prices():
    a, b = 0, 1
    for i in range(0, 1000000000000):
        yield a
        a, b = b, a + b
        
generator = fibonacci_prices()

print(generator)

