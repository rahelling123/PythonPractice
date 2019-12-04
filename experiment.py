
#dont understand why this doesnt work oncodewars, it works fine when i run it...
import itertools
def next_smaller(n):
    digits = list(str(n))
    if len(digits) <=1:
        return -1
    else:
        perms = list(itertools.permutations(digits))
        array = []
        for item in perms:
            value = ''
            for num in item:
                value = value + str(num)
            array.append(int(value))
        array = sorted(array)
        n_index = array.index(n) - 1

        return array[n_index]


value = next_smaller(21)
print(value)






