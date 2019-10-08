def encode(text):
    if (len(text) == 0):
        return ""
    result = ""
    c1 = text[0]
    count = 1
    for c2 in text[1:]:
        if c2 == c1:
            count += 1
        else:
            result += str(count) + c1
            c1 = c2
            count = 1
    return result + str(count) + c1


print(encode(""))
print(encode("a"))
print(encode("aaabbbkdbbbbkdkbkbkkkkkkbbbccccsssssssskkkkaaaaakakaakakabc"))
