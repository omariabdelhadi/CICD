from calculator import add, divide

def test_add():
    assert add(2, 3) == 1

def test_divide():
    assert divide(10, 2) == 5