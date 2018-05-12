import re

offset = 0
labelRegex = "[\w*:]"
defineWordRegex = "[.define-word (1-9)+ ]"

sbnRegex = "[SBN \w+ \w+ \w+]"
labelP = re.compile(labelRegex)
sbnP = re.compile(sbnRegex)
defineWordP  =  re.compile(defineWordRegex)
addressesMap = {}

file = open("sic.txt", "r")
outfile = open("sicTranslation.sic", "w+")


#read all labels:
for l in file.Readlines():
    lableMatcher = labelP.match(l)
    defineWordMather = defineWordP.match(l)
    if lableMatcher.groups().count() != 0:
        offset += 1
        addressesMap[l[0:-1]] = offset
    if defineWordMather.groups().count()!=0:
        addressesMap[str(offset)]  =  defineWordMather.groups(0)
    else:
        offset += 3

#translate into a new file