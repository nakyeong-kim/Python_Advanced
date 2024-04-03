"""
3. ProcessPoolExecutor

    * ProcessPoolExecutor, as_completed, futures, timeout, dict
    
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS = [
    'http://www.daum.net/', 
    'http://www.cnn.com/', 
    'http://naver.com', 
    'http://ruliweb.com', 
    'http://aws.com'
]


# 실행 함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
        
def main():
    # 프로세스풀 Context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드 (실행하는 것이 아님. 예약(적재))
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        
        # 중간 확인
        # print(future_to_url)
        
        # 실행
        for future in as_completed(future_to_url):
            # key 값이 future 객체
            url = future_to_url[future]
            
            try:
                # 결과
                data = future.result()
            except Exception as exc:
                # 예외 처리
                print('%r generated an exception: %s' % (url, exc))
            else:
                # 결과 확인
                print('%r page is %d bytes' % (url, len(data)))
                

if __name__ == '__main__':
    main()


"""
- 실행 결과
    'http://naver.com' page is 255461 bytes
    'http://ruliweb.com' page is 434878 bytes
    'http://aws.com' page is 986182 bytes
    'http://www.daum.net/' page is 684239 bytes
    'http://www.cnn.com/' page is 2433460 bytes
"""
