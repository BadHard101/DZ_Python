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
    def __init__(self, method_name):
        self.method_name = method_name
        super().__init__(f"Method '{method_name}' "
                         f"is not implemented for the current state.")


def test():
    o = MealyMachine()
    try:
        assert o.dash() == MealyError
        assert o.tweak() == 0
        assert o.dash() == 2
        assert o.tweak() == 4
        assert o.dash() == 5
        assert o.dash() == 8
        assert o.tweak() == 4
        assert o.tweak() == 6
        assert o.tweak() == 0
        assert o.mask() == 1
        assert o.dash() == 3
        assert o.dash() == MealyError
        assert o.tweak() == 4
        assert o.dash() == 5
    except MealyError as e:
        print(f"Caught MealyError: Method '{e.method_name}' "
              f"is not implemented for the current state.")

    try:
        assert o.tweak() == 0
        assert o.dash() == 2
        assert o.tweak() == 4
        assert o.dash() == 5
        assert o.mask() == 7
        assert o.dash() == 3
        assert o.dash() == MealyError
        assert o.tweak() == 4
        assert o.dash() == 5
        assert o.dash() == 8
        assert o.tweak() == 4
        assert o.tweak() == 6
    except MealyError as e:
        print(f"Caught MealyError: Method '{e.method_name}' "
              f"is not implemented for the current state.")

def main():
    test()

if __name__ == '__main__':
    test()
