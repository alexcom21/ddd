def main(s):
    s = s.replace('\n', ' ')
    d = {}
    k_1 = 0
    data = ''

    for i in range(len(s) - 1):
        if s[i] == "#":
            k = i + 1
            while (s[k] != " "):
                data += s[k]
                k += 1
        if s[i] == '@':
            k_1 = i + 2
        if s[i] == ";":
            k_2 = i - 1

        if s[i:i+3] == ':>,':

            if s[i-1] == ' ':
                d.setdefault(s[k_1:k_2], int(data))
                k_1 = 0
                data = ''
            else:
                d.setdefault(s[k_1:k_2], int(data))
                k_1 = 0
                data = ''

    return d
