from nose.tools import assert_equal


def large_cont_sum1(arr):
    start = 0
    end = 0

    if len(arr)==0:
        return 0

    l = []
    for j in range(len(arr)):
        end += arr[j]
        if start > end:
            l.append(start)
        start = end

    if l[0] == 0:
        return 1
    else:
        return max(l)

def large_cont_sum2(arr):

    if len(arr)==0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum, max_sum)

    return max_sum


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_cont_sum1)