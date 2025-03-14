import random

def fermat_primality_test(n,k):
    if n <= 3:
        print(f"{n} is  prime.")
        return True
    
    k = min(n,k)
    a_arr = random.sample(range(2,n-1),k)
    
    for a in a_arr:
        if a**(n-1) % n != 1:
            print(f"{n} is composite.")
            return False
    
    print(f"{n} is probably prime.")
    return True