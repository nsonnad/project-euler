# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def reverse_num(n):
    reverse = str(n)[::-1]
    return int(reverse)

def palindrome_products(low, high):
    ls = []
    for i in range(low, high):
        for j in range(low, high):
            n = i * j
            if n == reverse_num(n):
                ls.append(n)
    return ls