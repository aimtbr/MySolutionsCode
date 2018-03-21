def solution(roman):
    pat = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(roman) == 0 or len(list(filter((lambda x: x not in list(pat.keys())), roman))) != 0:
        return 0
    elif len(roman) > 3:
        for i in range(len(roman)):
            if roman[i:i + 4].count(roman[i]) == 4:
                return 0
    o = [pat[x] for x in roman.strip()]
    res, i = 0, 0
    while i <= len(o) - 1:
        if i == len(o) - 1:
            res += o[i]
        elif o[i] >= o[i + 1]:
            res += o[i]
        else:
            res += o[i + 1] - o[i]
            i += 1
        i += 1
    return res

print(solution("X"))
