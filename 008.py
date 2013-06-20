# Find the greatest product of five consecutive digits in
# the 1000-digit number (below)

the_num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# extract strings of desired length from num
def non_zero_consecutives(n, length):
    num_string = str(n)
    non_zero = []
    i = 0
    while i < len(num_string) - length:
        five_dig = num_string[i:i + length]
        # only save those without zeroes
        if not '0' in five_dig:
            non_zero.append(five_dig)
        i += 1
    return non_zero


def multiply_digits(n):
    multiplied = []
    non_zero = non_zero_consecutives(n)
    # multiply digits together
    for s in non_zero:
        num = 1
        for i in s:
            num *= int(i)
        multiplied.append(num)
    return multiplied

print multiply_digits(the_num, 5)