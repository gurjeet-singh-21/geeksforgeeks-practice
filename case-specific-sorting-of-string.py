# Case-specific Sorting of Strings

# Input:
# N = 12
# S = defRTSersUXI
# Output: deeIRSfrsTUX
# 
# Input:
# N = 6
# S = srbDKi
# Output: birDKs
#########################################
def caseSort(self,s,n):

    s1 = ''
    lower = sorted("".join(i for i in s if i.islower()))
    upper = sorted("".join(i for i in s if i.isupper()))
    c = 0; d = 0

    for i in s:

        if i.islower():
            s1 += lower[c]
            c += 1
        elif i.isupper():
            s1 += upper[d]
            d += 1

    return s1
