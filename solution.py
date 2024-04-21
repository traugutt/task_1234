import urllib.request as urllib

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        else:
            return True

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

# Main function
def main():
    print("Welcome to Legacy Python 2.7 Code")
    num = int(input("Enter a number to calculate factorial: "))
    print("Factorial of {} is: {}".format(num, factorial(num)))

    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print("{} is prime.".format(num))
    else:
        print("{} is not prime.".format(num))

    n = int(input("Enter the length of Fibonacci sequence: "))
    print("Fibonacci sequence:")
    fib_sequence = fibonacci(n)
    for i, fib_num in enumerate(fib_sequence):
        print("Fibonacci({}) = {}".format(i, fib_num))

    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)

    unicode_str = u"Unicode string: \u0394\u03b1\u03b9\u03b6\u03b5\u03b9"
    print(unicode_str.encode("utf-8"))


    response = urllib.urlopen("http://www.example.com")
    print(response.read())

    exec("print('Executing code with exec statement')")

if __name__ == "__main__":
    main()
