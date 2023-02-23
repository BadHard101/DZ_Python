import math


def main(n):
    if n == 0:
        return - 0.81
    elif n >= 1:
        return pow(math.sin(main(n - 1)), 2) +\
            pow(math.exp(main(n - 1)), 3) / 47 + 0.01
