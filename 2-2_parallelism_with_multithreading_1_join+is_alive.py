"""
1. join, is_alive
"""

# thread 코드와 매우 비슷함

from multiprocessing import Process
import logging
import time


def proc_func(name):
    logging.info("Sub-Process %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Process %s: finishing", name)

def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 함수 인자 확인
    p = Process(target=proc_func, args=('First', ))
    
    logging.info("Main-Process: before creating Process")
    
    # 서브 프로세스 시작
    p.start()
    
    logging.info("Main-Process: During Process")
    
    # 주석 전후 결과 확인   # 즉시 종료됨
    # logging.info("Main-Process: Terminated Process")
    # p.terminate()
    
    logging.info("Main-Process: Joined Process")
    p.join()
    
    # 프로세스 상태 확인
    print(f'Process p is alive: {p.is_alive()}')

if __name__ == '__main__':
    main()


"""
- 실행 결과
    13:18:29: Main-Process: before creating Process
    13:18:29: Main-Process: During Process
    13:18:29: Main-Process: Joined Process
    Process p is alive: False
"""
