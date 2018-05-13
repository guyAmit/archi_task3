import re

offset = 0
labelRegex = '[a-z]+: [0-9]+\n'
isNumberRegex = '[0-9]+\n*'
labelP = re.compile(labelRegex)
isNumberP = re.compile(isNumberRegex)

addressesMap = {}

file = open('sic.txt', 'r')

# read all labels:
for l in file.readlines():
    lableMatcher = labelP.fullmatch(l)
    if lableMatcher is not None:
        lablelAndNumber = l.split(' ')
        addressesMap[(lablelAndNumber[0])[:-1]] = str(offset)
        offset += 1
    else:
        offset += 3

print(addressesMap)
# translate into a new file
# Read in the file
file.close()
file = open("sic.txt", "r")



final = ""
lines = file.readlines()
for i in lines:
    thisline = i.split(" ")
    for j in thisline:
        j = j.replace('\n', '')
        numberMatcher = isNumberP.fullmatch(j)
        if numberMatcher is not None:
            final += j.replace('\n', '') + " "
        else:
            if j != "sbn" and (not j.__contains__(':')) :
                final+= addressesMap[j] + " "

outfile = open("sicTranslation.sic", "w+")

outfile.write(final[:-1])

outfile.close()
file.close()
