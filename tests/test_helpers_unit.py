from ans_pycli.helpers import default, set_val, get_val


def test_default():
    def func(x): return x

    assert default(1, 2, 3) == 1
    assert default(None, 2, 3) == 2
    assert default(None, None, 3) == 3
    assert default(None, 2, None) == 2
    assert default(None, None, None) is None
    assert default(None, None, None, _type=int) is None
    assert default(None, 'string', None, _type=str) == 'string'
    assert default(None, 2, None, _type=int) == 2
    assert default(None, 'string', None, _type=int) is None
    assert default(None, 2, None, _type=str) is None
    assert default(None, 2, None, _type=bool) is None
    assert default(1, 'string', None, True, _type=bool) is True
    assert default(1, 'string', None, False, _type=bool) is False
    assert default(1, 'string', None, True,
                   _type=callable) is None, 'should not accept not callable values'
    assert default(1, 'string', None, True, func,
                   _type=callable) is func, 'should not accept not callable values'


class T:
    a = 1
    b = 'string'
    c = True
    d = False
    e = None


def test_get_val():
    t = T()
    assert get_val(t, 'a') == 1
    assert get_val(t, 'b') == 'string'
    assert get_val(t, 'c') is True
    assert get_val(t, 'd') is False
    assert get_val(t, 'e') is None
    assert get_val(t, 'e', 1) == 1
    assert get_val(t, 'e', 1, _type=int) == 1
    assert get_val(t, 'e', 1, _type=str) is None
    assert get_val(t, 'e', 1, 'string', _type=str) == 'string'

    try:
        get_val(T, 'z')
    except Exception as e:
        assert isinstance(e, AttributeError)


def test_set_val():
    t = T()
    try:
        res = set_val(t, 'z', 2)
    except Exception as e:
        assert isinstance(
            e, AttributeError), "set_val should raise AttributeError if attribute doesn't exist"

    res = set_val(t, 'a', 2)
    assert t.a == 1, 'set_val should not change the value of an existing attribute'
    assert res == t.a, 'set_val should return the current value'

    res = set_val(t, 'a', 2, _type=str)
    assert t.a == 1, 'set_val should not change the value if value is not of the correct type'
    assert res == None, 'set_val should return None if value is not of the correct type'

    res = set_val(t, 'a', 2, _type=int)
    assert t.a == 1, 'set_val should not change existing value if it is of the correct type'
    assert res == t.a, 'set_val should return the current value if it is of the correct type'

    res = set_val(t, 'a', 'string', _type=str)
    assert t.a == 'string', 'set_val should change the value if existing value is not of the correct type'
    assert res == t.a, 'set_val should return the new value if existing value is not of the correct type'

    res = set_val(t, 'e', True)
    assert t.e == True, 'set_val should change the value if existing value is None'
    assert res == t.e, 'set_val should return the new value if existing value is None'
