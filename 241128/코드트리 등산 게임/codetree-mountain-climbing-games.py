def calculate(mountains, idx, num_of_mountains):
    dp = [0 for _ in range(num_of_mountains)]
    for i in range(1, num_of_mountains):
        for j in range(0, i):
            if mountains[i] > mountains[j]:
                dp[i] = max(dp[i], dp[j] + 1)

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
        calculate(mountains, commands[1] - 1, num_of_mountains)
