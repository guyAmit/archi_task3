# import re
# sbnRegex = 'sbn [\w+0-9]+ [\w+0-9]+[ ]*[\w+0-9]*\n*'
# specialSbnFormRegex = '[\w]+[+][1-2]+\n*'
# varRegex = '[a-z]+: [0-9]+\n*'
#
# varP = re.compile(varRegex)
# labelP = re.compile(sbnRegex)
# specialSbnFormP = re.compile(specialSbnFormRegex)
#
# sbnMatcher = labelP.match('sbn guy+2 guy+77 88')
# specialSbnFormMatcher = specialSbnFormP.match('guy+1')
# varMatcher = varP.match('guy: 1')
# print(sbnMatcher.group(0).replace('\n', ''))
# print(specialSbnFormMatcher.group(0).replace('\n', ''))
# print(varMatcher.group(0).replace('\n', ''))


# lableMatcher = labelP.fullmatch('c:\n')
# print(lableMatcher)
# lableMatcher = labelP.fullmatch('bdffd:\n')
# print(lableMatcher)

f = open('sicTranslation.sic','r')
print(len(f.readline().split(" ")))

