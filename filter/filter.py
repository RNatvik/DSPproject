

class Filter:

    def __init__(self, a: list, b: list = None, k: float = 1):
        self.a = a
        self.b = b
        self.k = k
        self.input = [0] * len(self.a)
        if self.b:
            self.output = [0] * len(self.b)
        else:
            self.output = [0]

    def filter_value(self, x_new: float):
        self.input = self._shift_list(self.input, x_new)
        y_new = sum([a*x for a, x in zip(self.a, self.input)]) + sum([b*y for b, y in zip(self.b, self.output)])
        self.output = self._shift_list(self.output, y_new)
        return y_new

    def filter_list(self, xn: list):
        y = []
        for x in xn:
            y.append(self.filter_value(x))
        return y

    def _shift_list(self, lst: list, val: float):
        lst.pop()
        lst.insert(0, val)
        return lst
