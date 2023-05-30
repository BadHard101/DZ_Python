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
    checkTest(o, "dash")  # state A -> B
    checkTest(o, "tweak")  # state B -> C
    checkTest(o, "mask")  # state C -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "dash")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "tweak")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> F
    checkTest(o, "dash")  # state F -> D
    checkTest(o, "dash")  # state D -> E
    checkTest(o, "dash")  # state E -> A
    checkTest(o, "mask")  # state A -> B
    checkTest(o, "dash")  # state B -> C
    checkTest(o, "mask")  # state C -> D


test()
