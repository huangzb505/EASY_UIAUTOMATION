str2 = 'A23467B'

# for st in str2:
#     if st < '6' and st > '0':
#      str2 = str2.replace(st, '0')
#     elif st >= '6' and st < '9':
#      str2 = str2.replace(st, '9')
#
# print(str2)

import re

def change_str(st):
    r = re.findall(r'\d', st)
    for i in r :
        if int(i) > 6:
            st = re.sub(i, '9', st)
        else:
            st = re.sub(i, '0', st)
    return st

new_str = change_str(str2)
print(new_str)