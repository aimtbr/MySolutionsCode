def same_structure_as(original,other,f=0):
    if type(original) == type(other) == list:
        if len(original) == len(other):
            if f <= len(original)-1:
                o = original[f]
                t = other[f]
                if type(o) == list:
                    if type(t) == list:
                        b = same_structure_as(o,t,0)
                        if b is False:
                            return False
                    else:
                        return False
                elif type(o) != list:
                    if type(t) != list:
                        a = same_structure_as(original,other,f+1)
                        if a is False:
                            return False
                    else:
                        return False
        else:
            return False
    else:
        return False
    return True


print(same_structure_as([1,"[","]"],["[","]",1]))