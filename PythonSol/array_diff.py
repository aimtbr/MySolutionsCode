"""Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""
def array_diff(a, b):
    if len(a)== 0 or len(b) == 0:
        return a
    else:
        for i in b:
            counter = a.count(i)
            while counter != 0:
                a.remove(i)
                counter -= 1
    return a
print(array_diff([1,2,3],[3]))