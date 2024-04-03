"""
4. Sharing state
    
    * Memory Sharing, Array, Value
    
"""

# 프로세스 메모리 공유 예제 - 2. 공유함

from multiprocessing import Process, current_process, Value, Array
import os


# 실행 함수
def generate_update_number(v: int):
    for _ in range(50):
        # v += 1
        v.value += 1       # 1.과 다른 부분     # Value 객체이므로 값에 접근할 때에는 .value 필요
    print(current_process().name, "data", v.value)      # 1.과 다른 부분     # Value 객체이므로 값에 접근할 때에는 .value 필요


def main():
    # 부모 프로세스 id
    parent_process_id = os.getpid()
    print(f'Parent process ID {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 메모리 공유 변수     # 1.과 다른 부분
    # share_value = 0   # 공유하지 않을 때
    share_value = Value('i', 0)     # type(int형)까지 엄격하게 선언해야 함
    # list를 공유하고 싶을 때 → share_numbers = Array('i', range(50))
    # 이 외에도, 
    # from multiprocess import shared_memory 사용 가능(파이썬 3.8)
    # from multiprocess import Manager 사용 가능
    # (참고) https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes
    # But, 이렇게 명시적으로 형 선언한는 것을 추천
    
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
    print('Final Data in parent process', share_value.value)  # 1.과 다른 부분     # Value 객체이므로 값에 접근할 때에는 .value 필요
    
# 메인
if __name__ == '__main__':
    main()

    
'''
- 실행 결과
    Parent process ID 19528
    Process-1 data 50
    Process-2 data 100
    Process-4Process-3 data  150
    data 200
    Process-5 data 250
    Process-6 Process-8dataProcess-7  300data
    350
    data 400
    Process-9 data 450
    Final Data in parent process 450
>> 정상적으로 값 공유함
'''
