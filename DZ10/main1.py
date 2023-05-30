class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def dash(self):
        if self.state == 'B':
            self.state = 'D'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 5
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise MealyError('dash')

    def tweak(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'A'
            return 6
        else:
            raise MealyError('tweak')

    def mask(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'F':
            self.state = 'C'
            return 7
        else:
            raise MealyError('mask')


class MealyError(Exception):
    pass


def main():
    return MealyMachine()


def checkTest(obj: MealyMachine, method):
    try:
        if method == "dash":
            obj.dash()
        elif method == "tweak":
            obj.tweak()
        elif method == "mask":
            obj.mask()
    except MealyError as e:
        pass


def test():
    o = main()
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "tweak")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    o = main()
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")
    checkTest(o, "dash")

    # A-G
    o = main()
    checkTest(o, "tweak")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-B-C-D-E-G
    o = main()
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "tweak")  # D
    checkTest(o, "tweak")  # error in D
    checkTest(o, "mask")  # error in D
    checkTest(o, "dash")  # E
    checkTest(o, "tweak")  # error in E
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-B-C-F-G
    o = main()
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "mask")  # F
    checkTest(o, "dash")  # error in F
    checkTest(o, "tweak")  # error in F
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-B-C-D-E-F-G
    o = main()
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "tweak")  # D
    checkTest(o, "tweak")  # error in D
    checkTest(o, "mask")  # error in D
    checkTest(o, "dash")  # E
    checkTest(o, "tweak")  # error in E
    checkTest(o, "dash")  # F
    checkTest(o, "dash")  # error in F
    checkTest(o, "tweak")  # error in F
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-A-G
    o = main()
    checkTest(o, "dash")  # A
    checkTest(o, "tweak")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-A-B-C-D-E-G
    o = main()
    checkTest(o, "dash")  # A
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "tweak")  # D
    checkTest(o, "tweak")  # error in D
    checkTest(o, "mask")  # error in D
    checkTest(o, "dash")  # E
    checkTest(o, "tweak")  # error in E
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-A-B-C-F-G
    o = main()
    checkTest(o, "dash")  # A
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "mask")  # F
    checkTest(o, "dash")  # error in F
    checkTest(o, "tweak")  # error in F
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G

    # A-A-B-C-D-E-F-G
    o = main()
    checkTest(o, "dash")  # A
    checkTest(o, "mask")  # B
    checkTest(o, "tweak")  # error in B
    checkTest(o, "mask")  # error in B
    checkTest(o, "dash")  # C
    checkTest(o, "dash")  # error in C
    checkTest(o, "tweak")  # D
    checkTest(o, "tweak")  # error in D
    checkTest(o, "mask")  # error in D
    checkTest(o, "dash")  # E
    checkTest(o, "tweak")  # error in E
    checkTest(o, "dash")  # F
    checkTest(o, "dash")  # error in F
    checkTest(o, "tweak")  # error in F
    checkTest(o, "mask")  # G
    checkTest(o, "dash")  # error in G
    checkTest(o, "tweak")  # error in G
    checkTest(o, "mask")  # error in G


test()
