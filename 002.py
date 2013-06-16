ls = [1, 2]

while ls[-1] + ls[-2] < 4000000:
    new_val = ls[-1] + ls[-2]
    ls.append(new_val)

even = [x for x in ls if x % 2 == 0]

total = sum(even)