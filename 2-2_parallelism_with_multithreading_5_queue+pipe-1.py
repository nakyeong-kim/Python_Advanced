"""
5. Queue, Pipe

    * Queue, Pipe, Communications between processes
    
"""

# 1. 프로세스 통신 구현 Queue

from multiprocessing import Process, Queue, current_process
import os
import time


# 실행 함수
def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 누적
    sub_total = 0
    
    # 계산
    for i in range(baseNum):
        sub_total += 1
    
    # Produce
    q.put(sub_total)
    
    # 정보 출력
    print(f'Process ID: {process_id}, Process Name: {process_name} ID: {id}')
    print(f'Result : {sub_total}')
    
# 메인
def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()
    print(f'Parent process ID {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 시작 시간
    start_time = time.time()
    
    # Queue 선언
    q = Queue()
    
    for i in range(5):      # 1~100 적절히 조절
        # 생성
        t = Process(name=str(i), target=worker, args=(i, 100000000, q))
        
        # 배열에 담기
        processes.append(t)
        
        # 프로세스 시작
        t.start()
    
    # Join
    for process in processes:
        process.join()
        
    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))

    # 종료 플래그
    q.put('exit')
    
    total = 0
    
    # 대기
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp    # 5억이 되어야 함
            
    print()
    
    print('Main-Processing Total Count={}'.format(total))
    print('Main-Processing Done!')
        
if __name__ == '__main__':
    main()

    
'''
- 실행 결과
    Parent process ID 8976
    Process ID: 27540, Process Name: 0 ID: 0
    Result : 100000000
    Process ID: 14440, Process Name: 1 ID: 1
    Result : 100000000
    Process ID: 28848, Process Name: 4 ID: 4
    Result : 100000000
    Process ID: 28452, Process Name: 3 ID: 3
    Result : 100000000
    Process ID: 3104, Process Name: 2 ID: 2
    Result : 100000000
    --- 21.16368055343628 seconds ---

    Main-Processing Total Count=500000000
    Main-Processing Done!
'''
