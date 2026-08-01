strs = ["aca","cba"]
prefix = min(strs, key=len)
for i in range(len(strs)):
    j = 0
    new_prefix = ""
    for sym in prefix:
        if sym == strs[i][j]:
            new_prefix += sym
        else:
            break
        j += 1
    prefix = new_prefix
print(prefix)