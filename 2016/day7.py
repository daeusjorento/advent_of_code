# https://adventofcode.com/2016/day/7
# https://adventofcode.com/2016/day/7/input -> save as input.txt

### Part 1
# --- Day 7: Internet Protocol Version 7 ---
# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).
# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.
# For example:
# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
# How many IPs in your puzzle input support TLS?

with open('input.txt') as file:
    data = file.read().split()
    
def check_abba(the_string):
    for i in range(0,len(the_string)-3):
        fourchar = the_string[i:i+4]
        if(fourchar[:2] == fourchar[2:][::-1]) & (fourchar[:2] != fourchar[2:]):
            #print(fourchar) 
            return(True)
            break
    return(False)

def check_tls(the_input):
    the_count = 0
    outcome = False
    for xx in the_input:
        brack_count = xx.count('[')
        brackets = []
        nonbrack = []
        use_string = xx
        for zz in range(0,brack_count):
            bracket = use_string[use_string.find('[')+1:use_string.find(']')]
            brackets.append(bracket)
            start = use_string[0:use_string.find('[')]
            nonbrack.append(start)
            use_string = use_string[use_string.find(']')+1:]
            if(zz == brack_count-1):
                nonbrack.append(use_string)


        for jj in nonbrack:
            if(check_abba(jj)==True):
                outcome = True
                for qq in brackets:
                    if(check_abba(qq)==True):
                        outcome = False
                        break
                break
            else:
                outcome = False

        if(outcome):
            the_count = the_count+ 1
    #         print(xx)
    #         print(outcome)
    return(the_count)

#print(check_tls(data))
#110

### Part 2
# --- Part Two ---
# You would also like to know which IPs support SSL (super-secret listening).
# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.
# For example:
# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
# xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
# How many IPs in your puzzle input support SSL?

def check_aba(the_string):
    the_list = []
    for i in range(0,len(the_string)-2):
        threechar = the_string[i:i+3]
        #print(threechar)
        if(threechar[0] == threechar[2]) & (threechar[0] != threechar[1]):
            the_list.append(threechar)
    if(len(the_list) >= 1):
        return(True,the_list)
    else:
        return(False,'')

def check_ssl(the_input):
    the_count = 0
    for xx in the_input:
        outcome = False
        ## split into bracketed and non-bracketed strings
        brack_count = xx.count('[')
        brackets = []
        nonbrack = []
        use_string = xx
        for zz in range(0,brack_count):
            bracket = use_string[use_string.find('[')+1:use_string.find(']')]
            brackets.append(bracket)
            start = use_string[0:use_string.find('[')]
            nonbrack.append(start)
            use_string = use_string[use_string.find(']')+1:]
            if(zz == brack_count-1):
                nonbrack.append(use_string)

        ## check aba pairs for both
        nb_pairs = []
        for jj in nonbrack:
            out,line = check_aba(jj)
            if(out==True):
                for kk in line:
                    nb_pairs.append(kk)
        outlist = []
        for tt in nb_pairs:
            bab = tt[1]+tt[0]+tt[1]
            outlist.append(bab)

        for qq in outlist:
            for rr in brackets:
                if(qq in rr):
                    outcome = True
                    break

        if(outcome):
            the_count = the_count+ 1
    return(the_count)

#print(check_ssl(data))
# 242
