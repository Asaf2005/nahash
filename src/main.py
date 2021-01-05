from words import classifiedDictionary
code = open("code.nahash", "r").readlines()
for i in classifiedDictionary:
    for k in classifiedDictionary[i]:
        for l, line in enumerate(code):
            code[l] = line.replace(classifiedDictionary[i][k], k)
fullCode = "".join(code)
exec(fullCode)
