"""
I/O Bound 2 - threading vs. asyncio vs. multiprocessing
"""

# I/O Bound Multiprocessing 예제


import multiprocessing
import requests
import time

# 각 프로세스 메모리 영역에 생성되는 객체 (독립적)
# 함수 실행 때마다 객체 생성은 좋지 않음 → 각 프로세스마다 할당
session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

# 실행함수1 : 다운로드
def request_site(url):
    # 세션 확인
    # print(session)
    # print(session.headers)
    
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} -> Read Contents : {len(response.content)}, Status Code : {response.status_code}] form {url}')
    
        
# 실행함수2 : 요청
def request_all_sites(urls):
    # 멀티 프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)

def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org", 
        "http://olympus.realpython.org/dice", 
        "https://realpython.com"
    ] * 3   # 총 9개
    
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 실행
    request_all_sites(urls)
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 결과 출력
    print(f'\nDownloaded {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()
    


"""
[실행 결과]

[SpawnPoolWorker-2 -> Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[SpawnPoolWorker-2 -> Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[SpawnPoolWorker-4 -> Read Contents : 10783, Status Code : 200] form https://www.jython.org
[SpawnPoolWorker-1 -> Read Contents : 10783, Status Code : 200] form https://www.jython.org
[SpawnPoolWorker-4 -> Read Contents : 10783, Status Code : 200] form https://www.jython.org
[SpawnPoolWorker-3 -> Read Contents : 68208, Status Code : 200] form https://realpython.com
[SpawnPoolWorker-1 -> Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[SpawnPoolWorker-2 -> Read Contents : 68208, Status Code : 200] form https://realpython.com
[SpawnPoolWorker-4 -> Read Contents : 68208, Status Code : 200] form https://realpython.com

Downloaded 9 sites in 2.612433671951294 seconds


>> thread를 사용하였으므로 순서대로 방문 X. 적은 시간 소요됨을 확인할 수 있음.
"""