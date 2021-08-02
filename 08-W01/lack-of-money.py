def solution(price, money, count):
    total_price = 0

    for i in range(1, count+1):
        total_price += price*i

    if money > total_price:
        return 0
    return abs(money-total_price)

solution(1, 1, 1)