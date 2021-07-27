import csv
import statistics as st

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
Data = []

for i in range(len(fileData)):
    n_num = fileData[i][1]
    Data.append(float(n_num))


#mean 
m = len(Data)
total = sum(Data)
mean = total/m
print(mean)


# 2nd step 

#diff = []
#for difference in Data:
 #   a = float(difference) - mean(Data)
  #  diff.append(a)
    
#print(diff)

# 3rd step

#for squares in range(m):
 #   m[squares] = m[squares]**2

#print(squares)


# 4th step 

#print(squares.sum())


# 5th step 

#subtract = 1
#n = len(m) - 1
#print(n)


sd = st.stdev(Data)
print(sd)