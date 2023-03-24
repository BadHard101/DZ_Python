def func13(x):
    if x[2] == 1991:
        return func_12(x)
    elif x[2] == 1968:
        return 13


def func_0_1_2(x):
    if x[3] == 'OOC':
        return 0
    elif x[3] == 'R':
        return 1
    elif x[3] == 'NESC':
        return 2


def func_3_4_5(x):
    if x[0] == 'TXL':
        return 3
    elif x[0] == 'JSX':
        return 4
    elif x[0] == 'XPROC':
        return 5


def func_6(x):
    if x[1] == 'SHEN':
        return func_0_1_2(x)
    elif x[1] == 'EQ':
        return func_3_4_5(x)
    elif x[1] == 'RED':
        return 6


def func_7_8_9(x):
    if x[1] == 'SHEN':
        return 7
    elif x[1] == 'EQ':
        return 8
    elif x[1] == 'RED':
        return 9


def func_10_11(x):
    if x[3] == 'OOC':
        return func_7_8_9(x)
    elif x[3] == 'R':
        return 10
    elif x[3] == 'NESC':
        return 11


def func_12(x):
    if x[4] == 2012:
        return func_6(x)
    elif x[4] == 1983:
        return func_10_11(x)
    elif x[4] == 1968:
        return 12


def func(x):
    return func13(x)


def main(x):
    # x = ['XPROC', 'SHEN', 1991, 'NESC', 1983]
    # print(func(x))
    return func(x)

# if __name__ == '__main__':
#     main()
