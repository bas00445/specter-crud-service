def add(x, y):
    return x + y

def multipy(x, y):
    return x * y

def divi(x, y):
    return x / y

def minus(x, y):
    return x - y


def main():
    assert 5 == add(3,2)
    assert 12 == add(6,6)
    assert 6 == multipy(3,2)
    assert 10 == minus(20,10)
    assert 5 == divi(10,2)
  
main()