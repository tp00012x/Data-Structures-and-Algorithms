from nose.tools import assert_equal
from collections import OrderedDict

def compress(s):
    tup = sorted(set(s))
    list = []
    for i in tup:
        list.append(i)
        list.append(str(s.count(i)))
    return "".join(list)


def compress2(s):
    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s + "1"
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)
            cnt = 1
        i += 1

    r = r + s[i - 1] + str(cnt)
    return r

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress2)