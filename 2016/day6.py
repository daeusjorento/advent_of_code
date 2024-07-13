## https://adventofcode.com/2016/day/6
## skipped day 5 like day 4 of 2015. MD5 Hash...

### Part 1
# --- Day 6: Signals and Noise ---
# Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.
# In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.
# All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.
# Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

with open('input.txt') as file:
    data = file.read().strip()
inp = data.split('\n')

import pandas as pd
df = pd.DataFrame(inp)
df_split = df[0].apply(list)
df_l = pd.DataFrame(df_split.tolist())

message = str()
for x in range(df_l.shape[1]):
    alpha_counts = {}
    let = df_l[x]
    for y in let:
        if(y in alpha_counts.keys()):
            alpha_counts[y] = alpha_counts[y]+1
        else:
            alpha_counts[y] = 1
        #print(alpha_counts)
    
    sorted_items = sorted(alpha_counts.items(), key=lambda item:(-item[1]))
    top = sorted_items[:1][0][0]
    #print(top)
    message = message + top
# print(message)
# gyvwpxaz

### Part 2
# --- Part Two ---
# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
# In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.
# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.
# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

message2 = str()
for x in range(df_l.shape[1]):
    alpha_counts = {}
    let = df_l[x]
    for y in let:
        if(y in alpha_counts.keys()):
            alpha_counts[y] = alpha_counts[y]+1
        else:
            alpha_counts[y] = 1
        #print(alpha_counts)
    
    sorted_items = sorted(alpha_counts.items(), key=lambda item:(item[1])) ## Only change from part 1.
    top = sorted_items[:1][0][0]
    #print(top)
    message2 = message2 + top
#print(message2)
#jucfoary
