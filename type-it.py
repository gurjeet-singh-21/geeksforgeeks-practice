# Type it!

# Input:
# s = abcabca
# Output: 5
# Explanation: a -> ab -> abc -> abcabc -> abcabca
# 
# Input:
# s = abcdefgh
# Output: 8
# Explanation: a -> ab -> abc -> abcd -> abcde -> abcdef -> abcdefg -> abcdefgh
#################################################################################
def minOperation(self, s): 
    for i in range(len(s)//2, 0, -1):
        
        if s[:i] == s[i:2*i]:
            
            return len(s[:i]) + 1 + len(s[2*i:])
    
    else:
        return len(s)
