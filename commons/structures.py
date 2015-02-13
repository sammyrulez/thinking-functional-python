class FunList(object):

    def __init__(self, it):
        self.iter = it

    def __iter__(self):
        for x in self.iter:
            yield x

    def filter(self, f):
        return FunList(filter(f, self))

    def map(self, f):
        return FunList(map(f, self))

    def iterate(self, f):
        for k in self:
            f(k)

    def join(self, delimiter):
        return delimiter.join(self)

    def __str__(self):
        return str(list(self))
