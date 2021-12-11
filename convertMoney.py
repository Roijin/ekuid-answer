import requests

host = "api.frankfurter.app"

money = [
    {"amount":15000,"currency":"IDR"},
    {"amount":30,"currency":"GBP"}
    ]

answer= []

for i in money:
    amount = i["amount"]
    currency = i["currency"]
    r = requests.get("https://"+host+"/latest?amount="+str(amount)+"&from="+currency+"&to=USD")
    conv = r.json()
    temp = conv['rates']
    USD = temp['USD']
    answer.append(USD)

print(answer)