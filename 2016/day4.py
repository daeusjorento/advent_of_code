## https://adventofcode.com/2016/day/4
## https://adventofcode.com/2016/day/4/input -> save as input.txt

### Part 1
# --- Day 4: Security Through Obscurity ---
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.
# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.
# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
# a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
# not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not.
# Of the real rooms from the list above, the sum of their sector IDs is 1514.

# What is the sum of the sector IDs of the real rooms?

with open('input.txt') as file:
    data = file.read()
lines = data.split('\n')

sector_sum = 0
for xx in lines:
    num = 0 ## needed since the last value is ''...
    z = xx.split('-')
    ldict = {}
    val = []
    for a in z:
        for l in a:
            if(l.isalpha()):
                if(l in ldict.keys()):
                    ldict[l] = ldict[l]+1
                else:
                    ldict[l] = 1
            elif(l.isnumeric()):
                val.append(l)
            else:
                num = int(''.join(val))
                break
    checksum = a[a.find('[')+1:a.find(']')]
    sorted_items = sorted(ldict.items(), key=lambda item:(-item[1],item[0]))
    dict_list = sorted_items[:5]
    dict_5 = dict(dict_list).keys()
    actual_sum = ''.join(dict_5)
    if(actual_sum == checksum):
        sector_sum = sector_sum + num
        
#     print(z)
#     print(num)
#     print(checksum)
#     print(sorted_items)
#     print(actual_sum)
#     print(sector_sum)
    
#print(sector_sum)
# 361724

### Part 2
# --- Part Two ---
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
# What is the sector ID of the room where North Pole objects are stored?

import string

## extract sector ID
def extract_sector_id(linestr):
    z = linestr.split('-')
    val = []
    for a in z:
        for l in a:
            if(l.isnumeric()):
                val.append(l)
    num = int(''.join(val))
    return(num)

## shift cipher
def cesar_cipher(input_str):
    sect_id = extract_sector_id(input_str)
    forward = sect_id % 26
    alphalist = list(string.ascii_lowercase)
    newstring = str(input_str)
    for i,x in enumerate(input_str):
        if(x=='-'):
            newstring = newstring[0:i] + ' ' + newstring[i+1:] # since strings are immutable...
        elif(x.isalpha()):
            pos = alphalist.index(x)
            newpos = (pos + forward) % 26
            newval = alphalist[newpos]
            newstring = newstring[0:i] + newval + newstring[i+1:]
        elif(x.isnumeric()):
            newstring = newstring[0:i-1]
            break
    return(newstring, sect_id)

# print(q)
# transl,num = cesar_cipher(q)
# print(transl)
# print(num)

for xx in lines:
    transl,num = cesar_cipher(xx)
    if('north' in transl):
        print(transl)
        print(num)
        break
# northpole object storage
# 482
