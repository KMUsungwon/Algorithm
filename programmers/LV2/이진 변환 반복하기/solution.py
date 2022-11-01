def solution(s):
    count = 1
    zero_num = 0
    
    while True:
        zn = s.count('0')
        zero_num += zn
        len_s = len(s.replace('0',''))
        temp = bin(len_s)[2::]

        if temp == "1":
            break
        s = temp
        count += 1
        
    return [count, zero_num]
