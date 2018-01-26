"""Write a function

triple_double(num1, num2)

which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
For example:

triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and
                                          // num2 has straight double 99s

triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1

If this isn't the case, return 0
"""

def triple_double(num1, num2):
    list_buff = list(str(num1))
    list_buff2 = list(str(num2))
    for i in range(len(list_buff)-2):
        if list_buff.count(list_buff[i]) >= 3:
            if list_buff[i+1] == list_buff[i+2] == list_buff[i]:
                if list_buff2.count(list_buff[i]) >= 2:
                    for j in range(len(list_buff2)-1):
                        if list_buff2[j] == list_buff2[j+1] == list_buff[i]:
                            return 1
    else:
        return 0
print(triple_double(10560002, 100))