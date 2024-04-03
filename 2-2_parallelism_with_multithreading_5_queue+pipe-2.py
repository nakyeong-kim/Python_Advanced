"""
5. Queue, Pipe

    * Queue, Pipe, Communications between processes
    
"""

# 2. 프로세스 통신 구현 Pipe

from multiprocessing import Process, Pipe, current_process
import os
import time


# 실행 함수
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 누적
    sub_total = 0
    
    # 계산
    for i in range(baseNum):
        sub_total += 1
    
    # Produce
    conn.send(sub_total)
    conn.close()
    
    # 정보 출력
    print(f'Process ID: {process_id}, Process Name: {process_name} ID: {id}')
    print(f'Result : {sub_total}')
    
# 메인
def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()
    print(f'Parent process ID {parent_process_id}')
    
    # 시작 시간
    start_time = time.time()
    
    # Pipe 선언
    parent_conn, child_conn = Pipe()
    
    # 생성
    t = Process(name=str(1), target=worker, args=(1, 500000000, child_conn))
        
    # 프로세스 시작
    t.start()
    
    # Join
    t.join()
        
    # 순수 계산 시간
    print("--- %s seconds ---" % (time.time() - start_time))
            
    print()
    
    print('Main-Processing Total Count={}'.format(parent_conn.recv()))
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
