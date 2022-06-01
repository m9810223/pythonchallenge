'http://www.pythonchallenge.com/pc/def/274877906944.html'


data = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


a = ord('a')


for d in data:
    if 'a' <= d <= 'z':
        print(chr(a + (ord(d) + 2 - a) % 26), end="")
    else:
        print(d, end="")


'maketrans'
