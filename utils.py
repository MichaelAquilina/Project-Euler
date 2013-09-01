def is_palindrome(n):
    n = str(n)

    for i in xrange(len(n)):
        if n[i] != n[-i - 1]:
            return False

    return True


def is_prime(n):

    for i in xrange(2, n - 1):
        if n % i == 0:
            return False

    return True


# A bit inefficient ... but it works
def factorise(n):

    factors = []

    while True:

        if is_prime(n):
            factors.append(n)
            return factors

        # Find the next number to divide by
        for i in xrange(2, n - 1):
            if n % i == 0:
                n /= i
                factors.append(i)
                break

    return None
