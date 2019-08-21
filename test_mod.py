from mod import *

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 1

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1

def test_fib6():
    # test internal point
    obs = fib(6)
    assert obs == 13

def test_c():
    exp = 6
    obs = c(2)
    assert obs == exp
