import re

offset = 0
varRegex = '[a-z_]+: [0-9]+\n*'
isNumberRegex = '[0-9]+\n*'
labelRegex = '[a-z_]+:\n*'
sbnRegex = 'sbn [\w+_0-9]+ [\w+_0-9]+[ ]*[\w+_0-9]*\n*'
specialSbnFormRegex = '[\w_]+[+][1-2]+\n*'
normalFormRegex = '[a-z_]+\n*'

labelP = re.compile(labelRegex)
varP = re.compile(varRegex)
isNumberP = re.compile(isNumberRegex)
sbnP = re.compile(sbnRegex)
specialSbnFormP = re.compile(specialSbnFormRegex)
normalFormP= re.compile(normalFormRegex)

addressesMap = {}

file = open('sic.txt', 'r')

# read all labels:
for l in file.readlines():
    l=l.replace('\n','')
    lableMatcher = labelP.match(l)
    varMatcher = varP.match(l)
    if varMatcher is not None:
        varAndNumber = varMatcher.group(0).split(' ')
        addressesMap[(varAndNumber[0])[:-1]] = str(offset)
        offset += 1
    elif lableMatcher is not None:
        label = lableMatcher.group(0)[:-1]
        addressesMap[label] = str(offset)
    else:
        offset += 3

print(addressesMap)
# translate into a new file
# Read in the file
file.close()
file = open("sic.txt", "r")



final = ""
lines = file.readlines()
offset=0
for i in lines:
    if i != '' :
        splittingIndex=0
        try:
            splittingIndex=i.index(';')
        except ValueError:
            splittingIndex=len(i)-1
        thisline = i[0:splittingIndex].replace('\n', '').split(" ")
        sbnMatcher = sbnP.match(i)
        lableMatcher = labelP.match(i)
        varMatcher = varP.match(i)
        if sbnMatcher is not None:
            for j in thisline:
                numMatcher = isNumberP.match(j)
                specialSbnFormMatcher = specialSbnFormP.match(j)
                normalFormMatcher = normalFormP.match(j)
                if numMatcher is not None:
                    final +=  numMatcher.group(0)+" "
                elif specialSbnFormMatcher is not None:
                    specialForm = specialSbnFormMatcher.group(0).split('+')
                    address = str(int(addressesMap[specialForm[0]])+int(specialForm[1]))
                    final += address + " "
                elif normalFormMatcher is not None:
                    if normalFormMatcher.group(0) != 'sbn':
                        final += addressesMap[normalFormMatcher.group(0)] + " "

            if len(thisline) == 3:
                final += str(offset+3) + " "
            offset += 3
        elif varMatcher is not None:
            final += thisline[1] + " "
            offset += 1


outfile = open("sicTranslation.sic", "w+")

outfile.write(final[:-1])

outfile.close()
file.close()
