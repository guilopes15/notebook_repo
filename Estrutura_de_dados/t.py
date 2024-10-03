from functools import cache


a = 'gui'


def teste():
    b = 'lhe'

    def inner():
        nonlocal b
        b = 'lher'
        c = 'me'
        return a + b + c

    return inner()


def sumarr(array, target):
    if array:
        memo = {}
        for index in range(len(array) - 1):
            contains = target - array[index]
            if contains in memo:
                return True
            memo[index] = array[index]
        return False
    return None


class T:
    def __init__(self):
        self.funcs = dict()

    def __call__(self, func):
        def closure():       
            self.funcs[func.__name__] = func()
            return func() 
            
        return closure
        
    
from time import sleep
d = T()


@d
def t1():
    return 'OI'
print(t1())
sleep(1)
print(d.funcs['t1'])






