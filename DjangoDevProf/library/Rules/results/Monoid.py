##Source: http://fmota.eu/blog/monoids-in-python.html

class Monoid:
    def __init__(self, null, lift, op):
        self.null = null
        self.lift = lift
        self.op   = op

    def __call__(self, *args):
        result = self.null
        for arg in args:
            arg = self.lift(arg)
            result = self.op(result, arg)
        return result



