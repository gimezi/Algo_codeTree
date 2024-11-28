def get_max_score(mountains, cable_car_idx):
    n = len(mountains)
    
    # dp[i]: i번째 산까지의 최장 증가 수열 길이
    dp = [0] * n
    
    # 케이블카 이전까지의 최장 증가 수열 계산
    for i in range(1, n):
        for j in range(i):
            if mountains[i] > mountains[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 케이블카에서 시작하는 최장 증가 수열 중 가장 큰 값 찾기
    max_after = 0  # 케이블카 이후 최대 증가 수열 길이
    max_height = 0  # 최종 도달 가능한 최대 높이
    
    for i in range(cable_car_idx + 1, n):
        current = 0
        for j in range(cable_car_idx, i):
            if mountains[i] > mountains[j]:
                current = max(current, dp[j] + 1)
        if current > max_after:
            max_after = current
            max_height = mountains[i]
        elif current == max_after:
            max_height = max(max_height, mountains[i])
    
    # 점수 계산
    score = 0
    # 최초 등산 점수
    max_first = dp[cable_car_idx]
    if max_first > 0:
        score += 1000000 * max_first
    
    # 케이블카 점수
    if max_after > 0:
        score += 1000000  # 케이블카 이용
        score += 1000000 * max_after  # 케이블카 이후 등산
        max_height = max(max_height, mountains[cable_car_idx])
    else:
        max_height = mountains[cable_car_idx]
    
    # 최종 높이 점수
    score += max_height
    
    return score

n = int(input())
mountains = []

for _ in range(n):
    commands = list(map(int, input().split()))
    if commands[0] == 100:  # 빅뱅
        num_mountains = commands[1]
        mountains = commands[2:]
    elif commands[0] == 200:  # 우공이산
        mountains.append(commands[1])
    elif commands[0] == 300:  # 지진
        if mountains:
            mountains.pop()
    else:  # 등산 시뮬레이션
        m_index = commands[1]
        print(get_max_score(mountains, m_index - 1))