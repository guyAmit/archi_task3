import re
labelRegex = '[a-z]+: [0-9]+'
labelP = re.compile(labelRegex)
lableMatcher = labelP.fullmatch('a: 1')
print(lableMatcher)
lableMatcher = labelP.fullmatch('c: 1')
print(lableMatcher)
lableMatcher = labelP.fullmatch('b: 1')
print(lableMatcher)


