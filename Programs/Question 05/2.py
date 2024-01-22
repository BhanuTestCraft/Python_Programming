def is_armstrong(num: int) -> bool:
    str_num = str(num)
    n = len(str_num)
    sum = 0
    for digit in str_num:
        sum += int(digit) ** n
    if sum == num:
        return True
    else:
        return False


num = int(input("Enter the value of number = "))
print(is_armstrong(num))
