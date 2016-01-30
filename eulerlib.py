import os

# Euler library file
# Contain functions that is used in multiple problems

# Sieve of Eratosthenes Manipulation


def export_sieve(sl, filename):
    sieve_file = open(filename, 'w')
    for i in sl:
        sieve_file.write("{}\n".format(str(i)))
    sieve_file.close()


def import_sieve(filename):
    with open(filename) as f:
        sieve_list = [int(line.rstrip('\n')) for line in f]
    return sieve_list


def get_sieve(n, filename):
    os.system('setterm -cursor off')
    counter = 0
    prime_list = import_sieve(filename)

    # check if list empty
    if not prime_list:
        prime_list = [2, 3]

    if n <= prime_list[-1]:
        print("No new prime added")
        return prime_list
    else:
        startval = prime_list[-1]
        print("Prime check: %i" % n)

        for i in range(startval, n, 2):
            if get_smallest_factor(i, prime_list)[0]:
                print("Added prime: %i            \r" % i, end='')
                counter += 1
                prime_list.append(i)

        os.system('setterm -cursor on')
        print("\n{} new prime added".format(counter))
        export_sieve(prime_list, filename)
        return prime_list


# Factorization


def get_smallest_factor(n, pl):
    if n == 1:
        return [True, 1]

    for prime in pl:
        if n % prime == 0:
            return [False, prime]

    return [True, n]


def get_all_factor(n, pl):
    fl = []

    while n != 1:
        divider = get_smallest_factor(n, pl)[1]
        fl.append(int(divider))
        n = n / divider

    return fl
