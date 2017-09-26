from nose.tools import assert_equal

def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                print(perm, i)
                out += [let + perm]
    return out

class TestPerm(object):
    def test(self, solution):
        assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('All test cases passed.')


# Run Tests
t = TestPerm()
t.test(permute)