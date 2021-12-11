import statistics

arr1 = [1,2,3,6,12,3,7,8,20,5,8,12,17,20]

total = 0
pos = 0
count = 0
row = []
answer=[]

for i in arr1:
    total += i
    count += 1
    pos +=1
    row.append(i)
    if  pos != len(arr1): 
        if arr1[pos-1]>arr1[pos] :
            mean = total/count
            median = statistics.median(row)
            newDict = {
                "mean" : mean,
                "median" : median
                }
            answer.append(newDict)
            count = 0
            row = []
            total = 0
    else:
        mean = total/count
        median = statistics.median(row)
        newDict = {
            "mean" : mean,
            "median" : median
            }
        answer.append(newDict)
        print(answer)
        break
        