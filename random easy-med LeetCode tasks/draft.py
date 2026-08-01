# s = "()[]{}"
# s = "([)]"
# s = "([()]"
# s = "{([]){}}"
s = "(){}}{"

el_dict = {")": "(", "]": "[", "}": "{"}
result = True
i_ok = []
for i in range(len(s)):
    if s[i] in el_dict:
        if i == 0:
            result = False
        for j in range(i-1, -1, -1):
            if j in i_ok:
                continue
            else:
                if s[j] != el_dict[s[i]]:
                    result = False
                    # print("p2", i, j, s[j])
                    break
                else:

                    i_ok.append(i)
                    i_ok.append(j)
                    break
    if not result:
        break
if len(i_ok) != len(s):
    result = False
print(result, i_ok)