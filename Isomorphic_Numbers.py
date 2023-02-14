s = "egg"
t = "add"
temp = ""

dict_word = {}

for i in range(2):
    for i in range(len(s)):
        if not dict_word.get(s[i]):
            dict_word[s[i]] = t[i]
        else:
            if t[i] != dict_word[s[i]]:
                print(False)
    temp = s
    s = t
    t = temp
    dict_word = {}

track = True
