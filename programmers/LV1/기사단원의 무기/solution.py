def solution(number, limit, power):
    answer = 0
    nums = [i for i in range(1, number+1)]
    
    temp = []
    for n in nums:
        count = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                count += 1
                if i ** 2 != n:
                    count += 1
        temp.append(count)
    
    for i in range(number):
        if temp[i] > limit:
            temp[i] = power
    return sum(temp)