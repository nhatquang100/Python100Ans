class Solution:
    def compress(self, chars):
        out = []
        tmp = 1
        for char in chars:
            if (len(out) == 0):
                out.append(char)
            elif (out[len(out) - 1] == char):
                tmp += 1
            else:
                if (tmp == 1):
                    out.append(char)
                else:
                    out.extend(list(str(tmp)))
                    out.append(char)
                tmp = 1
        if (tmp > 1):
            out.extend(list(str(tmp)))
        chars[:len(chars)] = out
        return len(chars)
        