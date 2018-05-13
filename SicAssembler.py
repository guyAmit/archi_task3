import re

offset = 0
labelRegex = '[a-z]+: [0-9]+'

labelP = re.compile(labelRegex)
addressesMap = {}

file = open("sic.txt", "r")

# read all labels:
for l in file.readlines():
    lableMatcher = labelP.fullmatch(l)
    if lableMatcher.groups() is not None:
        offset += 1
        lablelAndNumber = l.split(' ')
        addressesMap[lablelAndNumber[0][:-1]] = lablelAndNumber[1]
    else:
        offset += 3

# translate into a new file
# Read in the file
final = ""
lines = file.readlines()
for i in lines:
    thisline = i.split(" ")
    for j in thisline:
        try:
            int(s)
            final += s + " "
        except ValueError:
            final += addressesMap[j] + " "

outfile = open("sicTranslation.sic", "w+")

outfile.write(final)

outfile.close()
file.close()
