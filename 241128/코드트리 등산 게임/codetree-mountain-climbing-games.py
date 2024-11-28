def calculate(mountains, idx, num_of_mountains):
    dp = [1 for _ in range(num_of_mountains)]  # 초기값 1로 설정
    max_len = 1  # 현재까지의 최대 길이
    max_idx = 0  # 최대 길이를 가진 인덱스
    
    # tails 배열을 사용한 이진 탐색 방식
    tails = [0] * num_of_mountains
    size = 0
    
    # dp 배열 계산과 동시에 tails 배열 업데이트
    for i in range(num_of_mountains):
        # 이진 탐색으로 위치 찾기
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            if tails[mid] >= mountains[i]:
                right = mid
            else:
                left = mid + 1
                
        tails[left] = mountains[i]
        if left == size:
            size += 1
        dp[i] = left + 1
        
        # 최대 길이와 인덱스 업데이트
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i
    
    print(1000000 * dp[idx] + 1000000 + 1000000 * max_len + mountains[max_idx])

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