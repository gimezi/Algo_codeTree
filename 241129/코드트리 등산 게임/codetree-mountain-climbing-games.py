import sys
import bisect

def main():
    import sys
    import threading
    def run():
        Q = int(sys.stdin.readline())
        mountains = []
        results = []
        
        # Precompute for each mountain the next higher mountain to the right
        # This helps in traversing climbs efficiently
        next_higher = []
        
        for _ in range(Q):
            command = sys.stdin.readline().strip().split()
            cmd_type = int(command[0])
            
            if cmd_type == 100:
                # 빅뱅 명령어: 지도를 초기화
                n = int(command[1])
                mountains = list(map(int, command[2:2+n]))
            elif cmd_type == 200:
                # 우공이산 명령어: 산 추가
                h = int(command[1])
                mountains.append(h)
            elif cmd_type == 300:
                # 지진 명령어: 가장 오른쪽 산 제거
                if mountains:
                    mountains.pop()
            elif cmd_type == 400:
                # 등산 시뮬레이션 명령어
                m_index = int(command[1]) - 1  # 0-based 인덱스로 변환
                if not mountains:
                    results.append(0)
                    continue
                cable_car_height = mountains[m_index]
                
                score = 0
                # 사용한 케이블 카 횟수
                cable_car_used = 0
                
                # 현재 위치와 높이
                current_height = -1
                for i in range(len(mountains)):
                    if i == m_index:
                        # 케이블 카를 사용할지 결정
                        # 최대 점수를 위해 항상 사용
                        score += 1000000
                        cable_car_used +=1
                        current_height = -1  # 케이블 카를 타고 임의의 산으로 이동할 수 있으므로 초기화
                        continue
                    if mountains[i] > current_height:
                        score += 1000000
                        current_height = mountains[i]
                
                # 최종 산의 높이를 추가
                if current_height != -1:
                    score += current_height
                results.append(score)
        
        # 결과 출력
        for res in results:
            print(res)
                
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()
