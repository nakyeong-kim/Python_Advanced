"""
5. Prod vs. Cons Using Queue
    
    * Producer/Consumer Pattern(생산자 소비자 패턴)
        1) Multithread 디자인 패턴의 정석
        2) 서버측 프로그래밍의 핵심        
        3) 주로 허리 역할 (중요)
        
    * Python Event 객체
        1) Flag 초기값(0)
        2) Set() 호출 시 → 1
           Clear() 호출 시 → 0
           Wait(1 → 리턴, 0 → 대기)
           isSet() 호출 시 → 현 flag 값

"""

import logging
import concurrent.futures
import queue
import random
import time
import threading


# 생산자    # I/O(파일 읽기/쓰기 등), 네트워크 작업을 하는 Thread
def producer(queue, event):
    """ 네트워크 대기 상태라 가정(서버) """
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())
    
    logging.info("Consumer received event Exiting")
    
# 소비자    # CPU 작업을 하는 Thread
def consumer(queue, event):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장 """
    while not event.is_set():
        message = random.randint(1, 11)     # 1 ~ 10까지의 무작위의 자연수 생성
        logging.info("Producer get message: %s", message)
        queue.put(message)
    
    logging.info("Producer received event Exiting")

if __name__ == '__main__':
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 큐 설정
    # 사이즈 중요. 무조건 큐가 크다고 좋은 것은 아님.
    # ex) A → QUEUE → B 일 때, QUEUE 크기에 비해 B가 처리(소비)를 제대로 그때그때 하지 못한다면 병목 발생. 성능 하락으로 느껴짐.
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기값은 0임
    event = threading.Event()
    
    # with context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # 지금까지는 각 thread들과 code 영역의 메소드를 공유했음. But, 지금은 각 thread에 생산자, 소비자 메소드를 만들고 queue를 사용.
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    
        # 실행 시간 조정 (test를 위함 - 바로 프로그램이 끝나므로)
        # ※ 실무에서는 프로그램이 계속 떠 있어야 하므로 while True: pass 등 while문 주로 사용
        time.sleep(2)     # n초 동안 실행
    
        logging.info('Main : about to set event')
    
        # 프로그램 종료
        event.set()     # flag 값이 1로 바뀜
        

"""
- 실행 결과
    19:03:24: Consumer storing message: 7 (size=7)
    19:03:24: Producer get message: 10
    19:03:24: Consumer storing message: 4 (size=7)
    19:03:24: Producer get message: 8
    19:03:24: Consumer storing message: 1 (size=7)
    19:03:24: Producer get message: 9
    19:03:24: Consumer storing message: 2 (size=7)
    19:03:24: Producer get message: 11
    19:03:24: Consumer storing message: 5 (size=7)
    19:03:24: Producer get message: 3
    19:03:24: Consumer storing message: 9 (size=7)
    19:03:24: Producer get message: 8
    19:03:24: Consumer storing message: 8 (size=7)
    19:03:24: Producer get message: 11
    19:03:24: Consumer storing message: 2 (size=7)
    19:03:24: Main : about to set event
    19:03:24: Producer get message: 9
    19:03:24: Consumer storing message: 3 (size=7)
    19:03:24: Producer received event Exiting
    19:03:24: Consumer storing message: 10 (size=7)
    19:03:24: Consumer storing message: 8 (size=6)
    19:03:24: Consumer storing message: 9 (size=5)
    19:03:24: Consumer storing message: 11 (size=4)
    19:03:24: Consumer storing message: 3 (size=3)
    19:03:24: Consumer storing message: 8 (size=2)
    19:03:24: Consumer storing message: 11 (size=1)
    19:03:24: Consumer storing message: 9 (size=0)
    19:03:24: Consumer received event Exiting
"""
