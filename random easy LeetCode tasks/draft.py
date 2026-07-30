word = 'ajfhbsdifhbiaafjsdngfosga'

list_word = list(word)
list_word.sort()
print(list_word)

dict_word = {}
for el in list_word:
    if el.isalpha():
        if el in dict_word:
            dict_word[el] += 1
        else:
            dict_word[el] = 1

print(dict_word)

new_list_word = [k for k, v in sorted(dict_word.items(), key=lambda x: (-x[1], x[0]))]
print(new_list_word)

