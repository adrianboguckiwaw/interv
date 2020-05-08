# no requirement regarding input data was show, so i didnt implemented any exception handling


class NumberClass:
    n = int(input("please add 1 number"))
    print(n)
    m = int(input("please add 2 number"))
    print(m)
    print("starts:")
    for i in range(n, m + 1):
        if i > m:
            break
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        print(i)
