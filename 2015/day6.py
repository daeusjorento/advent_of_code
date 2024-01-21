## https://adventofcode.com/2015/day/6

### Part 1
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.
# For example:
# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

yo = input.split('\n')
import numpy as np
s = (1000,1000)
grid = np.zeros(s)
for x in yo:
    #before = grid.sum()
    
    input = 0
    toggle = 0
    if(x[0:8] == 'turn on '):
        ## extract numbers from string
        place = x.replace('turn on ','')
        input = 1
    elif(x[0:8] == 'turn off'):
        ## extract numbers from string
        place = x.replace('turn off','')
        input = 0
    elif(x[0:7] == 'toggle '):
        ## extract numbers from string
        place = x.replace('toggle ','')
        input = 0
        toggle = 1

    the_range = place.split(' through ')

    ## get start and end points
    start = the_range[0].split(',')
    end = the_range[1].split(',')

    ## x and y axis start and end ints
    start_x = int(start[0])
    end_x = int(end[0])+1
    start_y = int(start[1])
    end_y = int(end[1])+1

    if toggle == 0:
        grid[start_x:end_x,start_y:end_y] = input
    elif toggle == 1:
        extract_grid = grid[start_x:end_x,start_y:end_y]
        
        loc_1 = np.where(extract_grid==1)
        loc_0 = np.where(extract_grid==0)
        extract_grid[loc_1] = 0
        extract_grid[loc_0] = 1
        grid[start_x:end_x,start_y:end_y] = extract_grid
        
    #after = grid.sum()
    #change_est = input * ((end_x - start_x) * (end_y - start_y))

    #print(x)
    #print(change_est)
    #print(abs(after-before))
    
print(int(grid.sum()))

## 569999

### Part 2
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
# What is the total brightness of all lights combined after following Santa's instructions?
# For example:
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

s = (1000,1000)
grid = np.zeros(s)

for x in yo:

    input = 0
    toggle = 0
    if(x[0:8] == 'turn on '):
        ## extract numbers from string
        place = x.replace('turn on ','')
        input = 1
    elif(x[0:8] == 'turn off'):
        ## extract numbers from string
        place = x.replace('turn off ','')
        input = -1
    elif(x[0:7] == 'toggle '):
        ## extract numbers from string
        place = x.replace('toggle ','')
        input = 2
        toggle = 1

    the_range = place.split(' through ')

    ## get start and end points
    start = the_range[0].split(',')
    end = the_range[1].split(',')

    ## x and y axis start and end ints
    start_x = int(start[0])
    end_x = int(end[0])+1
    start_y = int(start[1])
    end_y = int(end[1])+1

    #print(toggle,input)
    
    if(toggle == 0) & (input == 1):
        grid[start_x:end_x,start_y:end_y] = grid[start_x:end_x,start_y:end_y]+1
    elif(toggle == 0) & (input == -1):
        newgrid = grid[start_x:end_x,start_y:end_y]-1
        newgrid[np.where(newgrid<0)]=0
        grid[start_x:end_x,start_y:end_y] = newgrid
    elif toggle == 1:
        grid[start_x:end_x,start_y:end_y] = grid[start_x:end_x,start_y:end_y]+2
    
print(int(grid.sum()))

## 17836115
