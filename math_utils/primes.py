def isprime(x):

    # Edge case
    if x <= 1:
        return False

    # Other cases
    i=2
    while i <= x**0.5:

        if (x%i == 0):
            return False
        else:
            i+=1

    return True