import math


def main(n, x, b, a):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += 36 * pow(math.log2(53 * pow(i, 2) + 95 * i), 7) \
                + 53 * pow(x, 3)

    sum2 = 0
    for k in range(1, a + 1):
        pr1 = 1
        for i in range(1, n + 1):
            sum3 = 0
            for c in range(1, b + 1):
                sum3 += pow(math.ceil(31 * k + pow(i, 2)), 2) -\
                        10 * pow(c, 4)
            pr1 *= sum3
        sum2 += pr1

    return sum1 + sum2
