# Wywolywanie obiektu poprzez callable i dodanie metody call. Tworzy się w ten sposob obiekt wywolany
import random
from inspect import signature

class BingCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick ')
    def __call__(self):
        return self.pick()


bingo = BingCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)


print(dir(factorial))

def tag(name, *content, cls=None, **attrs):
    """generowaie znacznika html"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
my_tag = {'name': 'img', 'title': 'Sunse', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

def clip(text, max_len=80):
    pass
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)


from inspect import signature
sig = signature(clip)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

print('--- fact ---')
from functools import reduce
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

print(fact(5))
from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))
print(fact(5))

metro_data = [
    ('Tokyo', 'JP', 36.9),
    ('Delhi NCR', 'IN', 21.923),
    ('Mxico City', 'MX', 20.142),
    ('New York', 'US', 20.104),
    ('Soa Paulo', 'BR', 19.649)
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc = itemgetter(1, 0)
for city in metro_data:
    print(cc(city))
import operator

v = [name for name in dir(operator) if not name.startswith('_')]
print("Funkcje w module operator " + str(v))

import functools
x = [name for name in dir(functools)]
print(functools)
