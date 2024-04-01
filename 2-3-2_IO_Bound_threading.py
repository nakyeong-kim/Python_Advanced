"""
I/O Bound - Threading
"""

import concurrent.futures
import threading
import requests
import time

# Threading

# 각 스레드에 생성되는 객체 - 독립된 네임스페이스 영역을 사용함
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):    # hasattr : attribute가 있는지 물어보는 함수
        thread_local.session = requests.Session()
    return thread_local.session

# 실행함수1 : 다운로드
def request_site(url):
    # 세션 획득
    session = get_session()
    
    # 세션 확인
    # print(session)
    # print(session.headers)
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code}] form {url}')
    
        
# 실행함수2 : 요청
def request_all_sites(urls):
    # 멀티 스레드 실행
    # 반드시 max_worker 개수 조절 후 session 객체 확인
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)

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

[Read Contents : 10783, Status Code : 200] form https://www.jython.org
[Read Contents : 10783, Status Code : 200] form https://www.jython.org
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 10783, Status Code : 200] form https://www.jython.org
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 68208, Status Code : 200] form https://realpython.com
[Read Contents : 68208, Status Code : 200] form https://realpython.com
[Read Contents : 68208, Status Code : 200] form https://realpython.com

Downloaded 9 sites in 1.3324263095855713 seconds


>> thread를 사용하였으므로 순서대로 방문 X. 적은 시간 소요됨을 확인할 수 있음.
"""