"""
2. Naming, Parallel processing
"""

from multiprocessing import Process, current_process
import os
import random
import time


# 실행
def square(n):
    # 랜덤 sleep
    time.sleep(random.randint(1, 3))
    
    process_id = os.getpid()
    process_name = current_process().name
    
    # 제곱
    result = n * n
    
    # 정보 출력
    print(f'Process ID: {process_id}, Process Name: {process_name}')
    print(f'Result of {n} square: {result}')
    
# 메인
if __name__ == '__main__':
    # 부모 프로세스 id
    parent_process_id = os.getpid()     # 랜덤으로 부여됨
    print(f'Parent process ID {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 생성 및 실행
    # start 후 모아서 join하는 것은 번거로우므로, 리스트에 넣어서 join → 단순하지만 빈번하게 사용되는 패턴 구조
    for i in range(1, 10):      # 1~100 적절히 조절
        # 생성
        t = Process(name=str(i), target=square, args=(i,))
        
        # 배열에 담기
        processes.append(t)
        
        # 프로세스 시작
        t.start()
        
    for process in processes:
        process.join()
    
    # 종료
    print('Main-Processing Done')
    
"""
- 실행 결과
    Parent process ID 27164
    Process ID: 27156, Process Name: 1
    Result of 1 square: 1
    Process ID: 25988, Process Name: 5
    Result of 5 square: 25
    Process ID: 23016, Process Name: 4Process ID: 25480, Process Name: 3

    Result of 4 square: 16Result of 3 square: 9

    Process ID: 29240, Process Name: 6
    Result of 6 square: 36
    Process ID: 27224, Process Name: 8
    Result of 8 square: 64
    Process ID: 28688, Process Name: 2
    Result of 2 square: 4
    Process ID: 26956, Process Name: 7
    Result of 7 square: 49
    Process ID: 29276, Process Name: 9
    Result of 9 square: 81
    Main-Processing Done
"""
