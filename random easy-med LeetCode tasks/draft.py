s = "abcabcbb"

s_list = list(s)
symbols = []
best_result = 1
result = 0
i = 0
for el in s_list:
    if el in symbols:
        symbols = symbols[i-1:]
        result -= (i-1)
        i = 0
    else:
        i += 1
        symbols.append(el)
        result += 1
    if result > best_result:
        best_result = result
print(best_result)