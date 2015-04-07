__author__ = 'Justin M'

def gcf(a,b):
    large,small = (a,b) if a > b else (b,a)
    factor = 0
    for i in range(1,small+1):
        if large % i == 0 and small % i == 0:
            factor = i

    return factor

def missing_nums(list_a,list_b):
    needed_nums = []
    for num in list_a:
        diff = list_b.count(num)-list_a.count(num)
        if diff > 0 and num not in needed_nums:
            needed_nums.append(num)
    needed_nums.sort()

    return needed_nums

#print(missing_nums([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204]))

def super_digit(n):
    if len(str(n))==1:
        return n
    else:
        return super_digit(digit_sum(n))

def digit_sum(n):
    num_str = str(n)
    num_list = [int(num) for num in num_str]
    return sum(num_list)

print(super_digit(148148148))