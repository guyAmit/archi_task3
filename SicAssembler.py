import re

offset = 0
labelRegex = '[a-z]+: [0-9]+'

labelP = re.compile(labelRegex)
addressesMap = {}

file = open("sic.txt", "r")

# read all labels:
for l in file.readlines():
    lableMatcher = labelP.fullmatch(str(l))
    if lableMatcher is not None:
        print(l)
        offset += 1
        lablelAndNumber = l.split(' ')
        addressesMap[lablelAndNumber[0][:-1]] = lablelAndNumber[1]
    else:
        offset += 3

print(addressesMap)
# translate into a new file
# Read in the file
file.close()
file = open("sic.txt", "r")


# final = ""
# lines = file.readlines()
# for i in lines:
#     thisline = i.split(" ")
#     for j in thisline:
#         try:
#             int(j)
#             final += j + " "
#         except ValueError:
#             if j != "sbn":
#                 final += addressesMap[j] + " "
#
# outfile = open("sicTranslation.sic", "w+")
#
# outfile.write(final)

# outfile.close()
file.close()
