"""
I/O Bound 1 - Synchronous
"""

# Synchronous Blocking I/O 예제


import requests
import time

# 실행함수1 : 다운로드
def request_site(url, session):
    # 세션 확인
    # print(session)
    # print(session.headers)
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code}] form {url}')
    
# 실행함수2 : 요청
def request_all_sites(urls):
    with requests.Session() as session:     # session이 살아있는 동안
        for url in urls:
            request_site(url, session)

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
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 68208, Status Code : 200] form https://realpython.com
[Read Contents : 10783, Status Code : 200] form https://www.jython.org
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 68208, Status Code : 200] form https://realpython.com
[Read Contents : 10783, Status Code : 200] form https://www.jython.org
[Read Contents : 274, Status Code : 200] form http://olympus.realpython.org/dice
[Read Contents : 68208, Status Code : 200] form https://realpython.com

Downloaded 9 sites in 3.1362287998199463 seconds


>> 순서대로 반복하는 것을 확인할 수 있음
"""