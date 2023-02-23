import math


def first_numerator(x, y, z):
    return 71 * math.pow((36 - math.pow(z, 2) - 35 * math.pow(z, 3)), 7) - \
        math.pow(math.pow(y, 2) + math.pow(x, 3), 4)


def first_denumerator(x, y, z):
    return 46 * math.pow(math.pow(z, 3) + math.pow(y, 2) + 66 * y, 6) - \
        65 * math.pow(math.floor(x), 5)


def second_numerator(x, y, z):
    return math.pow(64 * math.pow(x, 3) + math.pow(z, 2) + 1, 5) / 63 + \
        math.pow(math.atan(y), 4) / 13


def second_denumerator(x, y, z):
    return math.pow(math.ceil(79 * y - 80 * math.pow(z, 2) -
                              math.pow(x, 3) / 50), 4)


def main(x, y, z):
    return first_numerator(x, y, z) / first_denumerator(x, y, z) + \
        math.sqrt(second_numerator(x, y, z) / second_denumerator(x, y, z))
