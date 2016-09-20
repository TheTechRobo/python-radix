from numbers import Number

from justbases import Radices
from justbases import Radix

symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

max_base = len(symbol)

def cast(number, old_base, new_base):

    if old_base < 2 or new_base < 2:
        raise Exception('Not a valid base')

    if old_base > max_base or new_base > max_base:
        raise Exception('Not a valid base')

    if isinstance(number, int) and number >= 0:
        (radix, _) = Radices.from_rational(number, new_base)
    elif isinstance(number, str):
        try:
            digits = [symbol.index(f) for f in number.lower()]
        except ValueError:
            raise Exception("Not a valid natural number.")

        if all(d == 0 for d in digits):
            radix = Radix(0, [], [], [], old_base).in_base(new_base)
        else:
            radix = Radix(1, digits, [], [], old_base).in_base(new_base)
    else:
        raise Exception("Not a valid natural number.")

    return "".join([symbol[x] for x in radix.integer_part]) or "0"


class Converter:
    def __init__(self, old_base, new_base):
        self.old_base = old_base
        self.new_base = new_base
    def convert(self, number):
        result = cast(number, self.old_base, self.new_base)
        return result
