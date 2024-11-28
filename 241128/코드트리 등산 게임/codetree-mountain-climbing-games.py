def calculate(mountains, idx, num_of_mountains):
    dp = [0 for _ in range(num_of_mountains)]  # 원래 코드와 동일하게 0으로 초기화
    tails = [0] * num_of_mountains
    size = 1
    tails[0] = mountains[0]
    positions = [0] * num_of_mountains  # 각 위치의 LIS 길이 저장

    # 첫 번째 원소는 길이 1의 수열
    positions[0] = 0

    # 이진 탐색으로 LIS 구하기
    for i in range(1, num_of_mountains):
        if mountains[i] > tails[size-1]:
            tails[size] = mountains[i]
            positions[i] = size
            size += 1
        else:
            # 이진 탐색으로 위치 찾기
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= mountains[i]:
                    right = mid
                else:
                    left = mid + 1
            tails[left] = mountains[i]
            positions[i] = left

    # dp 배열 채우기 (기존 출력 형식 유지를 위해)
    for i in range(num_of_mountains):
        dp[i] = positions[i]

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