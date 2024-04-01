"""
CPU Bound 2 - Multiprocessing
"""

# CPU-Bound Multiprocessing 예제


from multiprocessing import current_process, Array, Manager, Process, freeze_support
import time
import os

# 실행함수 : 계산
def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    
    # Process 정보 출력
    print(f'Process ID : {process_id}, Process Name : {process_name}')
    
    total_list.append(sum(i * i for i in range(number)))

def main():
    numbers = [3_000_000 + x for x in range(30)]    # 파이썬에서 3_000_000 == 3000000
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 매니저
    manager = Manager()
    
    # 리스트 획득(프로세스 공유)
    total_list = manager.list()
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 프로세스 생성 및 실행
    for i in numbers:   # 1~100 적절히 조절
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))
        
        # 배열에 담기
        processes.append(t)
        
        # 시작
        t.start()
    
    # Join
    for process in processes:
        process.join()

    # 결과 출력
    print(f'\nTotal List : {total_list}')
    print(f'Sum : {sum(total_list)}')
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 수행 시간
    print(f'\nDuration : {duration} seconds')
    
if __name__ == "__main__":
    # 윈도우 예외 에러 발생 시
    # freeze_support()
    
    main()
    


"""
[실행 결과]

Process ID : 16984, Process Name : 3000008
Process ID : 4944, Process Name : 3000000
Process ID : 2104, Process Name : 3000002
Process ID : 16360, Process Name : 3000027
Process ID : 17392, Process Name : 3000025
Process ID : 7000, Process Name : 3000023
Process ID : 1392, Process Name : 3000003
Process ID : 12664, Process Name : 3000004
Process ID : 6832, Process Name : 3000017
Process ID : 16520, Process Name : 3000024
Process ID : 2004, Process Name : 3000026
Process ID : 15480, Process Name : 3000009
Process ID : 2500, Process Name : 3000020
Process ID : 3136, Process Name : 3000012
Process ID : 15952, Process Name : 3000021
Process ID : 4436, Process Name : 3000014
Process ID : 8756, Process Name : 3000001
Process ID : 15784, Process Name : 3000018
Process ID : 10176, Process Name : 3000028
Process ID : 10972, Process Name : 3000015
Process ID : 2676, Process Name : 3000010
Process ID : 2412, Process Name : 3000005
Process ID : 14952, Process Name : 3000007
Process ID : 15404, Process Name : 3000006
Process ID : 15888, Process Name : 3000011
Process ID : 4596, Process Name : 3000016
Process ID : 17036, Process Name : 3000019
Process ID : 16764, Process Name : 3000013
Process ID : 16884, Process Name : 3000029
Process ID : 16060, Process Name : 3000022

Total List : [9000013500006500001, 9000238502106506201, 9000148500816501496, 9000067500168500140, 9000031500036500014, 9000202501518503795, 9000220501800504900, 8999995500000500000, 9000022500018500005, 9000076500216500204, 9000211501656504324, 9000229501950505525, 9000175501140502470, 9000103500396500506, 9000184501260502870, 9000121500546500819, 9000004500000500000, 9000157500918501785, 9000247502268506930, 9000085500270500285, 9000130500630501015, 9000040500060500030, 9000058500126500091, 9000049500090500055, 9000094500330500385, 9000139500720501240, 9000166501026502109, 9000193501386503311, 9000112500468500650, 9000256502436507714]
Sum : 270003780024375058870

Duration : 18.887949228286743 seconds

>> 빠름

"""