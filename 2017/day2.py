## https://adventofcode.com/2017/day/2
## https://adventofcode.com/2017/day/2/input -> save as input.txt

with open('input.txt') as file:
    data = file.read().strip()
the_rows = data.split('\n')

## Part 1
val = 0
for xx in the_rows:
  nums = xx.split("\t")
  as_ints = list(map(int,nums)) ## convert to ints
  sorted_list = sorted(as_ints)
  smallest = sorted_list[0]
  largest = sorted_list[len(sorted_list)-1]
  diff = largest - smallest
  val = val+diff

print(val)
# 53460

## Part 2
val = 0
for xx in the_rows:
  #print(xx)
  nums = xx.split("\t")
  as_ints = list(map(int,nums))
  ## placeholder for numerator and denominators that divide evenly per question
  val_num = 0
  val_denom = 0
  sorted_list = sorted(as_ints,reverse=True) ## to start from largest
  for y in range(len(sorted_list)-1): ## -1 for only needing to look at the 2nd to last for numerator
    numerator = sorted_list[y]
    numbers_to_divide = sorted_list[y+1:len(sorted_list)]
    for denom in numbers_to_divide:
      if(numerator%denom == 0):
        val_num = numerator
        val_denom = denom
        row_result = val_num/val_denom
        # print(val_num)
        # print(val_denom)
        # print(row_result)
  val = val+row_result

print(val)
#282
