s = "III"

Roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = reversed(s)
s_list = list(s)
result = 0
i = 0
while i < len(s_list):
    if i != len(s_list) - 1:
        if ((s_list[i] == "V" or s_list[i] == "X") and s_list[i+1] == "I") or\
           ((s_list[i] == "L" or s_list[i] == "C") and s_list[i+1] == "X") or\
           ((s_list[i] == "D" or s_list[i] == "M") and s_list[i+1] == "C"):
            result += (Roman_numbers[s_list[i]] - Roman_numbers[s_list[i+1]])
            print(result)
            i += 2
        else:
            result += Roman_numbers[s_list[i]]
            i += 1
    else:
        result += Roman_numbers[s_list[i]]
        i += 1

print(result)