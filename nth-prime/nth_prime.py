def prime(number):
    if number == 0:
        raise ValueError('Nope') 

    if number==1:
        return 2
    count = 1
    num = 1
    while(count < number):
        num +=2 #optimization
        if is_prime(num):
            count +=1
    return num

def is_prime(num):
    factor = 2
    while (factor * factor <= num):
        if num % factor == 0:
             return False
        factor +=1
    return True

print(prime(6))

print(prime(10001))

