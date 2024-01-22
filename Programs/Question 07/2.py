def is_prime(x: int) -> None:
    factors = 0
    if x > 1:
        for i in range(1, x + 1):
            if x % i == 0:
                factors += 1
        if factors == 2:
            print(f"Number {x} is a prime number.")
        else:
            print(f"Number {x} is not a prime number.")


num = int(input("Enter the value of number = "))
is_prime(num)
