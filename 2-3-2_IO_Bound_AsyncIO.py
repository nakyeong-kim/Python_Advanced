"""
I/O Bound 2 - threading vs. asyncio vs. multiprocessing
"""

# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 → async, await 적절하게 코딩 필요


import asyncio
# import requests     # 동기식이라 다른 패키지 사용 필요
import aiohttp
import time


# 실행함수1 : 다운로드
async def request_site(session, url):
    # 세션 확인
    # print(session)
    # print(session.headers)
    # print(id(session.headers))
    
    async with session.get(url) as response:
        print(f'Read Contents {response.content_length}, form {url}')
    
        
# 실행함수2 : 요청
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:     # with문이랑 쓰므로 await 아님
        # 작업 목록
        tasks = []
        for url in urls:
            # 작업 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        
        # 태스크 확인
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)

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
    # 파이썬 3.7 이상
    asyncio.run(request_all_sites(urls))
    # 파이썬 3.7 미만
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 결과 출력
    print(f'\nDownloaded {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()
    


"""
[실행 결과]

Read Contents 3717, form https://www.jython.org
Read Contents 274, form http://olympus.realpython.org/dice
Read Contents 274, form http://olympus.realpython.org/dice
Read Contents 274, form http://olympus.realpython.org/dice
Read Contents 3717, form https://www.jython.org
Read Contents 3717, form https://www.jython.org
Read Contents None, form https://realpython.com
Read Contents None, form https://realpython.com
Read Contents None, form https://realpython.com

Downloaded 9 sites in 0.8834607601165771 seconds

>> threading, multiprocessing에 비해 asyncio가 훨씬 빠름
>> 적합한 처리 방식을 선택해야 함

"""