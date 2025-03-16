def euclid_mod(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1


def euclid_sub(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    
    return num1


def euclid_recursive(num1, num2):
    if num2 == 0:
        return num1
    else:
        return euclid_recursive(num2, num1 % num2)