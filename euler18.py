# Variable declarations
numOfRows = 0       # For keeping track of stats
maxValue = 0        # To help calculating larger sets
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
        numOfRows += 1
        row = [] 
        
        for item in line_nums:
            # retrieve the value of each number
            fNumber = formatNums(item)
            # check if it's the biggest number ever
            maxValue = fNumber if fNumber > maxValue else maxValue
            # and store each number in a row[]
            if fNumber > 0:
                row.append(fNumber)
            else:       # until you hit an end of line, then onto the next row
                numOfRows -=1
        if (row != []):
            # then save that row to the pyramid
            pyramid.append(row)
                
print "\n\nmaxValue is: ", maxValue
print "numOfRows is: ", numOfRows
    
rPyramid = []   # flip the triangle
for row in reversed(pyramid):
    rPyramid.append(row)

for row in rPyramid:    
    print row    
    
pyramid = []    # reset the pyramid variable so I can reuse it

for row_index, row in enumerate(rPyramid):
    new_row = []
    for item_index, item in enumerate(row):
        addItem = 0;
        try:
            addItem = item if item > row[item_index+1] else row[item_index+1]
            new_row.append(addItem + rPyramid[row_index+1][item_index])
        except IndexError:
            print "D", row_index
            try:
                rPyramid[row_index+1] = new_row
            except IndexError:
                print "Done!"
            finally:
                pyramid.append(new_row)
            
    
print pyramid
print rPyramid