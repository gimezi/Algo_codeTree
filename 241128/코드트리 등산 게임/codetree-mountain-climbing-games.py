class MountainCalculator:
    def __init__(self):
        self.mountains = []
        self.dp = []  # 각 위치의 LIS 길이 저장
        
    def calculate_dp(self, start_idx):
        tails = [0] * len(self.mountains)
        size = 0
        
        # start_idx 이전까지는 이미 계산되어 있음
        for i in range(start_idx, len(self.mountains)):
            if i == 0:
                tails[0] = self.mountains[i]
                size = 1
                continue
                
            if self.mountains[i] > tails[size-1]:
                tails[size] = self.mountains[i]
                self.dp[i] = size
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
                self.dp[i] = left
    
    def init_mountains(self, mountains):
        self.mountains = mountains
        self.dp = [0] * len(mountains)
        self.calculate_dp(0)
    
    def add_mountain(self, height):
        self.mountains.append(height)
        self.dp.append(0)
        self.calculate_dp(len(self.mountains)-1)
    
    def remove_mountain(self):
        if self.mountains:
            self.mountains.pop()
            self.dp.pop()
    
    def calculate(self, idx):
        h_idx = self.dp.index(max(self.dp))
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