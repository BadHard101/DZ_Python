import math


def main(y):
    sum_1 = 0
    n = len(y)
    for i in range(1, n + 1):
        ind = n - math.ceil(i / 4)  # + 1 is wrong task question
        sum_1 += pow(pow(y[ind], 3) - 1, 2)

    return 40 * sum_1
