def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    
    for arr in arr1:
        result = ''
        while arr > 0:
            result += str(arr % 2)
            arr //= 2
    
        listed_num = list(result)
        while len(listed_num) != n:
            listed_num.append(0)
        
        temp = listed_num[::-1]
        temp = list(map(str, temp))
        bin_arr1.append(''.join(temp))
    
    for arr in arr2:
        result = ''
        while arr > 0:
            result += str(arr % 2)
            arr //= 2
    
        listed_num = list(result)
        while len(listed_num) != n:
            listed_num.append(0)
        
        temp = listed_num[::-1]
        temp = list(map(str, temp))
        bin_arr2.append(''.join(temp))
    
    for i in range(n):
        temp = ''
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    
    return answer