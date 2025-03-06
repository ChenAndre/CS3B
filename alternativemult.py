row1 = []
for i in range(1, 11):  
    row1.append(i)

col1 = []
for i in range(1, 11):  #strt from 1 no 0 mult
    col1.append(i)

for r in row1:
    for c in col1:
        print(r * c, end='\t') 
    print()  



