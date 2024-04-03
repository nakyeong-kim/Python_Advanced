"""
1. Threading Basic
"""

import logging
import threading
import time

# subthread 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)

# 메인 thread 영역
if __name__ == "__main__":      # descriptor
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")      # print보다 logging 클래스를 사용하는 것이 좋음
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', ))
    
    logging.info("Main-Thread: before running thread")
    
    # sub thread 시작
    x.start()
    
    # 주석 전후 결과 확인
    x.join()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("all done")

"""
- 총 2개의 thread가 실행됨
- 실행 결과
    16:53:35: Main-Thread: before creating thread
    16:53:35: Main-Thread: before running thread
    16:53:35: Sub-Thread First: starting
    16:53:35: Main-Thread: wait for the thread to finish
    16:53:35: all done      # sleep(3) 동안 main thread는 끝나버림
    16:53:38: Sub-Thread First: finishing
- 즉, main thread 영역의 실행이 끝난다 해도, sub thread는 맡은 일을 끝까지 함
"""
