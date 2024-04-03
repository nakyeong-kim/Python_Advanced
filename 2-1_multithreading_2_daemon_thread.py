"""
2. Daemon Thread
    1) background에서 실행
    2) main thread 종료 시 즉시 종료    ※ 일반 thread는 본인 작업 종료 시까지 계속 실행
    3) 주로 background 무한 대기 시 이벤트 발생시키는 부분을 담당  ex) JVM(가비지 컬렉션), 자동 저장 등
    4) 주로 while문과 함께 코딩함
"""

import logging
import threading
import time

# subthread 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    for i in d:
        print(i)
    logging.info("Sub-Thread %s: finishing", name)

# 메인 thread 영역
if __name__ == "__main__":      # descriptor
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")      # print보다 logging 클래스를 사용하는 것이 좋음
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(10000)), daemon=True)
    
    logging.info("Main-Thread: before running thread")
    
    # sub thread 시작
    x.start()
    y.start()
    
    # Daemon Thread인지 확인
    print(x.isDaemon())
    print(y.isDaemon())
    
    # 주석 전후 결과 확인       # daemon으로 설정해놓고 join을 하는 것은 매우 좋지 못한 코드 (끝까지 실행됨)
    # x.join()    
    # y.join()
        
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("all done")
