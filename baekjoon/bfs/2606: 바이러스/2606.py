import sys

def bfs(b_list):
    count = 0
    queue = [1]
    
    while queue:
        for i in bfs_list[queue.pop()]:
            if not flag[i]:
                count += 1
                flag[i] = 1
                queue.append(i)
    
    return count

num_of_computer = int(sys.stdin.readline())
pair = int(sys.stdin.readline())

flag = [0] * (num_of_computer+1)
flag[1] = 1

bfs_list = [[] for _ in range(num_of_computer+1)] # 0번째 배열은 사용 안함

for _ in range(pair):
    node1, node2 = map(int, sys.stdin.readline().split())
    bfs_list[node1].append(node2)
    bfs_list[node2].append(node1)

result = bfs(bfs_list)
print(result)

        
