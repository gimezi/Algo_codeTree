class MountainCalculator:
    def __init__(self):
        self.mountains = []
        self.dp = []  # 각 위치의 LIS 길이 저장
        
    def calculate_dp(self):
        n = len(self.mountains)
        self.dp = [0] * n
        tails = [0] * n
        size = 0
        
        for i in range(1, n):  # 1부터 시작
            if i == 1:
                if self.mountains[i] > self.mountains[0]:
                    tails[size] = self.mountains[i]
                    self.dp[i] = 1
                    size += 1
                continue
                
            if self.mountains[i] > tails[size-1] and size > 0:
                tails[size] = self.mountains[i]
                self.dp[i] = size + 1
                size += 1
            else:
                # 이진 탐색으로 위치 찾기
                left, right = 0, size
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] >= self.mountains[i]:
                        right = mid
                    else:
                        left = mid + 1
                tails[left] = self.mountains[i]
                self.dp[i] = left + 1
    
    def init_mountains(self, mountains):
        self.mountains = mountains
        self.calculate_dp()
    
    def add_mountain(self, height):
        self.mountains.append(height)
        self.calculate_dp()
    
    def remove_mountain(self):
        if self.mountains:
            self.mountains.pop()
            if self.mountains:  # 산이 남아있으면 다시 계산
                self.calculate_dp()
            else:
                self.dp = []
    
    def calculate(self, idx):
        h_idx = self.dp.index(max(self.dp)) if max(self.dp) > 0 else 0
        print(1000000 * self.dp[idx] + 1000000 + 1000000 * max(self.dp) + self.mountains[h_idx])

calculator = MountainCalculator()
n = int(input())

for _ in range(n):
    commands = list(map(int, input().split()))
    if commands[0] == 100:
        calculator.init_mountains(commands[2:])
    elif commands[0] == 200:
        calculator.add_mountain(commands[1])
    elif commands[0] == 300:
        calculator.remove_mountain()
    else:
        calculator.calculate(commands[1] - 1)