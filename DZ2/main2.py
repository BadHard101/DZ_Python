import math


def main(y):
    if y < -3:
        return 39 * math.floor(y) + pow(y, 7) / 56 + pow(y, 3)
    elif y < 31:
        return 1 + math.tan(4 * pow(y, 2))
    elif y < 46:
        return pow(y, 2) - 1 - 91 * math.log2(y)
    elif y < 104:
        return 32 * (1 - pow(y, 3)) + \
            pow(y, 6) + pow(pow(y, 3) + pow(y, 2), 7) / 35
    else:
        return pow(pow(y, 3) + 88, 2) - \
            85 * pow(y, 5) - \
            61 * pow(math.tan(81 - pow(y, 2)), 6)

