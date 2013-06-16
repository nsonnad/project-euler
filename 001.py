def multipleSum(start, end):
    my_sum = 0
    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            my_sum = my_sum + i

    return my_sum

print multipleSum(1, 1000)