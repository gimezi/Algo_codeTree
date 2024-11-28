def calculate(mountains, idx, num_of_mountains):
    dp = [0 for _ in range(num_of_mountains)]
    tails = [0] * num_of_mountains
    size = 0
    
    for i in range(num_of_mountains):
        # 이진 탐색으로 위치 찾기
        if i == 0:
            tails[0] = mountains[i]
            size = 1
            continue
            
        if mountains[i] > tails[size-1]:
            tails[size] = mountains[i]
            dp[i] = size
            size += 1
        else:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= mountains[i]:
                    right = mid
                else:
                    left = mid + 1
            tails[left] = mountains[i]
            dp[i] = left

    h_idx = dp.index(max(dp))
    print(1000000 * dp[idx] + 1000000 + 1000000 * max(dp) + mountains[h_idx])

n = int(input())
mountains = []
num_of_mountains = 0
for _ in range(n):
    commands = list(map(int, input().split()))
    if commands[0] == 100:
        num_of_mountains = commands[1]
        mountains = commands[2:]
    elif commands[0] == 200:
        mountains.append(commands[1])
    elif commands[0] == 300:
        mountains.pop()
    else:
        calculate(mountains, commands[1] - 1, len(mountains))