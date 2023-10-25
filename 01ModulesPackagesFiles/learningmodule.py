def afunction(x):
    return 2.0 / x


class AClass:
    def __init__(self, x):
        self.x = x

    def afunction(self):
        return afunction(self.x)
