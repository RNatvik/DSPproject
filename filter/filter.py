

class Filter:

    def __init__(self, a: list, b: list, k: float = 1):
        self.a = a
        self.b = b
        self.k = k

        self.prev_in = [0]*len(a)
        self.prev_out = [0]*len(b)

    def filter_value(self, x):
        pass

    def filter_list(self, xn):
        pass

    def _shift_list(self, lst: list, val: float):
        pass
