# Note: Write a solution that only iterates over the string once and uses O(1) 
# additional memory, since this is what you would be asked to do during a real interview.

def firstNotRepeatingCharacter(s):
    for a in range(len(s)):
        if s.index(s[a]) == s.rindex(s[a]):
            return s[a]
    return '_'


