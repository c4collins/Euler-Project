# Variable declarations
pyramid = []        # To contain the row[]s of numbers

# Function declarations
# removes the random text formatting bits (\r, \n, etc) and returns 0s for them
def formatNums(item):
    try:
        num = int(item)
    except ValueError:
        num = 0
    finally:
        return num
        
# Main operations

with open("euler18_test_lg.txt") as txt:
    for line in txt:        # Open file and split it by spaces
        line_nums = line.split(" ")
        row = [] 
        
        for item in line_nums:
            # retrieve the value of each number
            fNumber = formatNums(item)
            # and store each number in a row[]
            if fNumber > 0:
                row.append(fNumber)
        if (row != []):
            # then save that row to the pyramid
            pyramid.append(row)
                
    
rPyramid = []   # flip the triangle
for row in reversed(pyramid):
    rPyramid.append(row)

pyramid = []    # reset the pyramid variable so I can reuse it


# Calculate which is the larger of the two variables and add it to the next row
#| 6 7 8 | X 7 8 | X X X | X X X | X X X |
#|  4 5  |  4 5  | 11 13 |  X 13 |  X X  |
#|   3   |   3   |   3   |   3   |   16  |
for row_index, row in enumerate(rPyramid):
    new_row = []
    for item_index, item in enumerate(row):
        addItem = 0;
        try:
            addItem = item if item > row[item_index+1] else row[item_index+1]
            new_row.append(addItem + rPyramid[row_index+1][item_index])
        except IndexError:
            try:
                rPyramid[row_index+1] = new_row
            except IndexError:
                pass
            finally:
                pyramid.append(new_row)

print "Largest Total is:", rPyramid[len(rPyramid)-1][0]