"""Description:

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets, with values between 0..255 (included).

Input to the function is guaranteed to be a single string.
Examples

// valid inputs:
1.2.3.4
123.45.67.89

// invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Note: leading zeros (e.g. 01.02.03.04) are considered not valid in this kata!
"""
def is_valid_IP(strng):
    lst = strng.split(".")
    print(lst)
    if len(strng) < 7 or len(strng) > 15:
        return False
    elif list(strng).count(".") != 3:
        return False
    for each in lst:
        if each.isdigit() and each.startswith("0") == False:
            if int(each) not in range(0, 256):
                return False
        else:
            return False
    return True
print(is_valid_IP('123.045.067.089'))