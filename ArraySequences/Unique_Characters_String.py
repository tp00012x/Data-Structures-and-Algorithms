from nose.tools import assert_equal


def uni_char1(s):
    if sorted(set(s)) == sorted(s):
        return True
    return False

def uni_char2(s):
    length = len(s)
    i = 1

    while i < length:
        if s[i] == s[i-1]:
            return False
        i += 1
    return True

def uni_char3(s):
    return len(set(s)) == len(s)

def uni_char4(s):

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(uni_char4)