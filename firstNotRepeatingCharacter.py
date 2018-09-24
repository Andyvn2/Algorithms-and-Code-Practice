

def firstNotRepeatingCharacter(s):
    for a in range(len(s)):
        if s.index(s[a]) == s.rindex(s[a]):
            return s[a]
    return '_'


