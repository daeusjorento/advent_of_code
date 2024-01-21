## https://adventofcode.com/2015/day/4

# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
# For example:
# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

## Cheated... don't want to explore this encoding but wanted to move forward past day 4...
# https://www.reddit.com/r/adventofcode/comments/3vdn8a/day_4_solutions/

from hashlib import md5

puzz_input = 'iwrupvqb'
n = 1
found_five, found_six = False, False

while found_six == False:
    input_hash = md5((puzz_input + str(n)).encode()).hexdigest()
    if found_five != True and input_hash[:5] == '00000':
        print ("5: "+str(n))
        found_five = True
    if input_hash[:6] == '000000':
        print ("6: "+str(n))
        found_six = True
    n += 1

## 346386

### Part 2
# Now find one that starts with six zeroes.

## 9958218
