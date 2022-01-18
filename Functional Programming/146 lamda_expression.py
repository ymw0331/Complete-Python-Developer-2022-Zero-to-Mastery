# Lambda Expressions (function only used once), onetime anonymous function

from functools import reduce

my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(lambda item: item * 2, my_list)))
print(my_list)
