def pattern(n):
    for i in range (1, n + 1):
        for j in range(i):
            print(i,end="")
        print()

n = int(input("Enter the value of n: "))
pattern(n)
