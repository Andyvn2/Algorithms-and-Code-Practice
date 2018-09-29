def amendTheSentence(s):

    a = ''
    
    for x in range(0,len(s)):
        if x == 0:
            a = a + s[x]
        else:
            if s[x].isupper():
                a = a + ' '
            a = a + s[x]
    return a.lower()
        


# You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

# Put a single space between the words.
# Convert the uppercase letters to lowercase.