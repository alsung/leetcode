def isUniqueChars(str):
    if len(str) > 128:
        return False
    
    char_s = [False] * 128
    for i in range(0, len(str)):
        val = ord(str[i]) # returns ascii code for character i
        if char_s[val]:
            return False
        char_s[val] = True
    return True

in_str = "hi"
print(isUniqueChars(in_str))

