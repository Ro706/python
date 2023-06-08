
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    n = int(input("Enter the number of terms: "))
    print("The Fibonacci series is: ")
    for i in range(n):
        print(fib(i), end=" ")

if __name__ == "__main__":
    main()
