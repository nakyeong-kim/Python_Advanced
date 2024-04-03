"""
4. Sharing state
    
    * Memory Sharing, Array, Value
    
"""

# 프로세스 메모리 공유 예제 - 1. 공유하지 않음

from multiprocessing import Process, current_process
import os


# 실행 함수
def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print(current_process().name, "data", v)


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()
    print(f'Parent process ID {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 메모리 공유 변수
    share_value = 0
    
    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        
        # 배열에 담기
        processes.append(p)
        
        # 프로세스 시작
        p.start()
        
    # join
    for process in processes:
        process.join()
    
    # 최종 프로세스 부모 변수 확인
    print('Final Data in parent process', share_value)
    
# 메인
if __name__ == '__main__':
    main()

    
'''
- 실행 결과
    Parent process ID 23208
    Process-1 data 50
    Process-3 data 50
    Process-5Process-7 data 50Process-4
    data 50
    data 50
    Process-2 data 50
    Process-6 data 50
    Process-8 data 50
    Process-9 data 50
    Final Data in parent process 0
>> 제대로 값 공유가 안되고 있음 (최종적으로 450이 나와야 함)
>> process는 thread과 달리 모든 영역(stack, heap, data, code)이 독립적이므로 (thread는 stack만 독립)
'''
