class MountainCalculator:
    def __init__(self):
        self.mountains = []
        self.dp = []  # 각 위치의 LIS 길이 저장
        
    def init_mountains(self, mountains):
        self.mountains = mountains
        self.dp = [0] * len(mountains)
        # 초기 dp 계산
        for i in range(1, len(mountains)):
            for j in range(0, i):
                if mountains[i] > mountains[j]:
                    self.dp[i] = max(self.dp[i], self.dp[j] + 1)
    
    def add_mountain(self, height):
        self.mountains.append(height)
        self.dp.append(0)
        # 새로 추가된 산에 대해서만 dp 계산
        i = len(self.mountains) - 1
        for j in range(0, i):
            if self.mountains[i] > self.mountains[j]:
                self.dp[i] = max(self.dp[i], self.dp[j] + 1)
    
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