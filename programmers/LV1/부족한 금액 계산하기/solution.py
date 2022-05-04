def solution(price, money, count):
    li = []
    for i in range(count):
        li.append(price*(i+1))

    return 0 if (money-sum(li))>=0 else sum(li)-money