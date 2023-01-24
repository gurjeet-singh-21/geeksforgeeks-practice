#Function to remove pair of duplicates from given string using Stack.
####################
# Input:
# aaabbaaccd
# Output:
# ad
# Explanation:
# Remove (aa)abbaaccd =>abbaaccd
# Remove a(bb)aaccd => aaaccd
# Remove (aa)accd => accd
# Remove a(cc)d => ad
# 
# Input:
# aaaa
# Output:
# Empty String
# Explanation:
# Remove (aa)aa => aa
# Again removing pair of duplicates then (aa)
# will be removed and we will get 'Empty String'.
####################
def removePair(self,s):

    stack = []

    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if stack:
        return "".join(stack)
    else:
        return -1
