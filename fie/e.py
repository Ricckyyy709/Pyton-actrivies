def num(n, i=1):
    if i <= n:
        print(i)
        num(n, i + 1)

number = int(input("Enter a number: "))

num(number)
