#targeting 2d Array

#list comprehension vs multiplication


''''Class ourmult:
    def __init__(self,start,end,shape = 0):
        self.start = start
        self.end = end
        self.shape = shape '''


#test cases: make sure it work for ints that are positive numbers and raise value err if float or negative number
#should raise a ValueError start = 10,end = 0; 
#ValueError if start > end
'''
Print multiplication table.
:param start: the inclusive start of the table
:param end: the exclusive end of the table
:param shape: if 0, print the whole square; if 1, print lower triangle
:return: None 




'''

'''row1 = []
for i in range(1, 11):  
    row1.append(i)
col1 = []
for i in range(1, 11):  #strt from 1 no 0 mult
    col1.append(i)'''

def printmulttable(start, end, shape =0):
    row1 = []
    for i in range(start,end):
        row1.append(i)

    col1 = []
    for i in range(start,end):
        col1.append(i)
    for r in row1:
        for c in col1:
            print(r * c, end='\t') 
        print()  
    
    if start < end:
        raise ValueError("Err, start is greater than end ")


print(printmulttable(1,10))


#now we need to raise the value Error


        
        