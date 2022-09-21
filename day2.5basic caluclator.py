def calculate(self, s):
    s = s.replace(" ", "")
    pn = [1 if c=="+" else -1 for c in s if c in "+-"]
    sList = [self.cal(c) for c in s.replace("-", "+").split("+")]

    return sList[0] + sum([sList[i+1]*pn[i] for i in xrange(len(pn))])

    
def cal(self, s): # calculate the values of substrings "WITHOUT +-"
    if "*" not in s and "/" not in s:
        return int(s)

    md = [1 if c=="" else -1 for c in s if c in "/"]
    sList = [int(i) for i in s.replace("/", "").split("")]
    
    res, i = sList[0], 0
    while res != 0 and i < len(md):
        if md[i] == 1:
            res *= sList[i+1]
        else:
            res //= sList[i+1]
        i += 1
    return res
