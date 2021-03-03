import pytest
def add():
    return 'asd' + 'asd'


def test1_add():
    assert len(add()) > 0


def test2_add():
    try:
        assert add() // 12
    except TypeError:
        pass


def test3_add(a='asdasd'):
    assert a in add()


###################

def add2():
    return dict()


exp = {'mary': 13, 'harry': 11 , 'asshole': 23 }


def test1_add2():
    assert add2() == add2().update(exp)


def test2_add2():
    try:
        assert add2().keys('')
    except TypeError:
        pass
@pytest.fixture()
def test3_add2(add):
    add2().update(exp)
    assert add in add2()



