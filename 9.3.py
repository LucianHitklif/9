prise = int(input("Сколько нужно заплатить ведьмаку? "))
money = [25, 10, 5, 1]
coins = 0
i = 0
while prise > 0 and i < len(money):
    coin = money[i]
    coins += prise // coin
    prise = prise % coin
    i += 1
print(coins)
