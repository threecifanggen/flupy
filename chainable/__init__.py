from chainable.chainable import chainable, Chainable
from typing import Callable, Type

__project__ = 'chainable'
__version__ = '0.1'

__all__ = ['chainable', 'map', 'filter', 'zip', 'enumerate', 'take', 'chunk', 'flatten', 'window']

def map(iterable, func: Callable, *args, **kwargs):
    Chainable.map.__doc__
    return Chainable(iterable).map(func, *args, **kwargs)

def filter(iterable, func: Callable, *args, **kwargs):
    Chainable.filter.__doc__
    return Chainable(iterable).filter(func, *args, **kwargs)

def zip(*iterables):
    Chainable.zip.__doc__
    return Chainable(zip(*iterables))

def enumerate(iterable, start: int=0):
    Chainable.enumerate.__doc__
    return Chainable(iterable).enumerate(start)

def take(iterable, n: int):
    Chainable.take.__doc__
    return Chainable(iterable).take(n)

def chunk(iterable, n: int):
    Chainable.chunk.__doc__
    return Chainable(iterable).chunk(n)

def flatten(iterable, depth: int=1, base_type: Type= None, iterate_strings=False):
    Chainable.flatten.__doc__
    return Chainable(iterable).flatten(depth, base_type, iterate_strings)

def window(iterable, n: int, step: int=1, fill_value: object=None):
    Chainable.window.__doc__
    return Chainable(iterable).window(n, step)
