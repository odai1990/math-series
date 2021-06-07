from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


##### fibonacci ######
def test_one_fibonacci():
    actual=1
    expected=fibonacci(1)
    assert actual==expected

def test_zero_fibonacci():
    actual=0
    expected=fibonacci(0)
    assert actual==expected


def test_less_than_zero_fibonacci():
    actual='invalid intrence'
    expected=fibonacci(-1)
    assert actual==expected

def test_other_type_fibonacci():
    actual='invalid intrence'
    expected=fibonacci("dddd")
    assert actual==expected

    
def test_five_fibonacci():
    actual=5
    expected=fibonacci(5)
    assert actual==expected

#### end of fibonacci ######



##### lucas ######

def test_one_lucas():
    actual=1
    expected=lucas(1)
    assert actual==expected

def test_zero_lucas():
    actual=2
    expected=lucas(0)
    assert actual==expected


def test_less_than_zero_lucas():
    actual='invalid intrence'
    expected=lucas(-1)
    assert actual==expected

def test_other_type_lucas():
    actual='invalid intrence'
    expected=lucas("dddd")
    assert actual==expected

    
def test_five_lucas():
    actual=11
    expected=lucas(5)
    assert actual==expected


#### end of lucas ######


##### lucas ######

def test_one_sum_series():
    actual=1
    expected=sum_series(1)
    assert actual==expected


def test_less_than_zero_sum_series():
    actual='invalid intrence'
    expected=sum_series(-1)
    assert actual==expected

def test_other_type_sum_series():
    actual='invalid intrence'
    expected=sum_series("dddd")
    assert actual==expected




#### end of lucas ######