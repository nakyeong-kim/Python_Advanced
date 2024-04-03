"""
4. Lock, DeadLock
    
    * Semaphore(세마포어)
        - 프로세스 간 공유된 자원에 접근 시 문제 발생 가능성이 있으므로, 한 개의 프로세스만 접근 처리하도록 고안하는 것 → 경쟁 상태 예방

    * Mutex(뮤텍스)
        - 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 → 경쟁 상태 예방
    
    * Lock(락)
        - 상호 배제를 위한 잠금(lock) 처리 → 데이터 경쟁
        
    * Deadlock(데드락)
        - 프로세스가 자원을 획득하지 못해 다음 처리를 하지 못하는 무한 대기 상태 = 교착 상태
        
    * Thread Syschronization(스레드 동기화)
        - 스레드 동기화를 통해서 안정적으로 동작하도록 처리 (동기화 메소드, 동기화 블럭)
        
    * Semaphore와 Mutex의 차이?
        - mutex 개체는 단일 thread가 리소스 또는 중요 섹션 소비 허용
          ex) 화장실 1개에 1명만 들어갈 수 있도록 함. 1명이 키를 들고 들어갔다가 나와서 대기 줄의 1명에게 키를 줌.
        - semaphore는 리소스에 대한 제한된 수의 동시 액세스 허용
          ex) 화장실 3개에 1명씩 들어갈 수 있도록 함.
        >> semaphore와 mutex 개체는 모두 병렬 프로그래밍 환경에서 상호 배제를 위해 사용 = 둘 다 경쟁 상태를 예방하기 위한 동기화 작업을 일컫는 말
        >> semaphore는 mutex가 될 수 있지만, mutex는 semaphore가 될 수 없다.
        
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

# ※ thread는 stack만 별도 할당! 나머지 code, data, heap 영역은 공유
# 클래스를 전역으로 생성 → code 영역에 저장됨 → 각각의 thread들이 code 영역에 접근하여 실행
class FakeDataStore:
    
    # 공유 변수(value)  # ex) 화장실
    def __init__(self):
        self.value = 0      # 공유되는 변수     # data 영역에 저장됨
    
    # 변수 업데이트 함수
    def update(self, n):
        logging.info("Thread %s: starting update", n)
    
        # Mutex & Lock 등 동기화(Thread synchronization) 필요   # 이 파일에서는 안함
        local_copy = self.value     # local_copy의 stack 영역에 value 값을 저장함
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        
        logging.info("Thread %s: finishing update", n)

if __name__ == '__main__':
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info('Testing update. Starting value is %d', store.value)
    
    # with context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)
    
    logging.info('Testing update. Ending value is %d', store.value)

"""
- 실행 결과
    18:30:44: Testing update. Starting value is 0
    18:30:44: Thread First: starting update
    18:30:44: Thread Second: starting update
    18:30:44: Thread Second: finishing update
    18:30:44: Thread First: finishing update
    18:30:44: Thread Third: starting update
    18:30:44: Thread Third: finishing update
    18:30:44: Testing update. Ending value is 2
>> 3이 나와야 하지만 결과는 2가 나옴. 제대로 update가 안됨.
>> 즉, 동기화가 안된 것
"""
