"""
Your module description
"""
from funcion1 import numero_menor

def test_numero_menor():
    assert numero_menor([3,6,7,4,2])==2
    assert numero_menor([3,10,20,4,15])==3
    assert numero_menor([2,5,6,9,1])==1