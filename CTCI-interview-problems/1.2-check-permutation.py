def permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

str1 = "hello"
str2 = "lloeh"

print(permutation(str1, str2))