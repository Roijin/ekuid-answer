bills = [1000,2000,5000,10000,20000,50000,100000]

total = {
    "amount" : 80000,
    "split" : 6}

amount = total["amount"]
count = total["split"]
answer=[]

while amount > 0:    
    for i in range(7):
        current = bills[i]
        if amount > 10000:
            if amount < bills[i]:
                amount -= bills[i-1]
                count -= 1
                answer.append(bills[i-1])
                break
        elif count < total["split"] and count > 1:
            div = amount/count
            if div - bills[i+1] < 0:
                amount -= bills[i]
                count -= 1
                answer.append(bills[i])
                break
        elif count == 1:
            if amount <= bills[i]:
                amount -= bills[i]
                count -= 1
                answer.append(bills[i])
print(answer)
