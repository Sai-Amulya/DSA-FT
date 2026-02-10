def main():
    n = int(input())
    fib = [0] * (n+1)
    if n == 0:
        print("Fibonacci series till 0th term is:")
        print(0)
    elif n == 1:
        print("Fibonacci seried till 1st term is:")
        print("0 1")
    else:
        fib[0] = 0
        fib[1] = 1
        for i in range(2,n+1):
            fib[i] = fib[i-1] + fib[i-2]
        print(f"Fibonacci series till {n}th term is:")
        print(" ".join(str(num) for num in fib))

def fibonaccibetter():
    n = int(input())
    if n==0:
        print(f"Fibonacci series till {n}th term is: ")
        print(0)
    else:
        beforelast = 0
        last = 1
        print(f"Fibonacci series for {n}th term is: ")
        print(f"{beforelast} {last}", end = " ")

        for i in range(2,(n+1)):
            num = last + beforelast
            beforelast = last
            last = num
            print(num, end=" ")
            

              
if __name__ == "__main__":
    main()
    fibonaccibetter()


