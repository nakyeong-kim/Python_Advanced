"""
I/O Bound 2 - Asyncio basic

* 동시 프로그래밍 패러다임 변화
    1. 싱글 코어 시절 → 처리 향상 미미, 저하
    2. 비동기 프로그래밍 대두 → CPU 연산, DB 연동, API 호출 대기 시간이 늘어남
    >> asyncio가 비동기 non-blocking임

* 파이썬 3.4에서 비동기(asyncio) 표준라이브러리 등장
    1. 동기(sync)
        def func():
            pass
        
    2. 비동기(async)
    
        async def func1():
            pass

    3. async 함수 안에서 다른 비동기 함수를 실행할 때에 await을 붙이는 규칙 기억
    붙이지 않으면 예외가 발생하거나, 동기 처리가 됨
        async def func2():
            await func1()

"""

# I/O Bound Asyncio 기초 예제


import time
import asyncio

# 비동기 함수 1
async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calculating...')
        # time.sleep(1)   # 동기 함수임. await을 붙여도 동기 함수므로 쓸 수가 없음.
        await asyncio.sleep(1)      # 비동기 함수 사용하고 await 붙임.
    print(f'{name} - {n} working done!')

# 비동기 함수 2
async def process_async():
    start = time.time()
    
    task1 = asyncio.create_task(
        exe_calculate_async('One', 3)
    )
    task2 = asyncio.create_task(
        exe_calculate_async('Two', 2)
    )
    task3 = asyncio.create_task(
        exe_calculate_async('Three', 1)
    )
    
    await task1
    await task2
    await task3

    end = time.time()
    
    print(f'>>> total seconds : {end - start}')

# 동기 함수 1
def exe_calculate_sync(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')

# 동기 함수 2
def process_sync():
    start = time.time()
    
    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)

    end = time.time()
    
    print(f'>>> total seconds : {end - start}')
    
if __name__ == '__main__':
    # Sync 실행
    # process_sync()
    
    # Async 실행
    # 파이썬 3.7 이상
    asyncio.run(process_async())
    # 파이썬 3.7 미만
    # asyncio.get_event_loop().run_until_complete(process_async())



"""
[실행 결과]

# 동기
One -> 1 of 3 is calculating...
One -> 2 of 3 is calculating...
One -> 3 of 3 is calculating...
One - 3 working done!
Two -> 1 of 2 is calculating...
Two -> 2 of 2 is calculating...
Two - 2 working done!
Three -> 1 of 1 is calculating...
Three - 1 working done!
>>> total seconds : 6.00937557220459

# 비동기
One -> 1 of 3 is calculating...
Two -> 1 of 2 is calculating...
Three -> 1 of 1 is calculating...
One -> 2 of 3 is calculating...
Two -> 2 of 2 is calculating...
Three - 1 working done!
One -> 3 of 3 is calculating...
Two - 2 working done!
One - 3 working done!
>>> total seconds : 3.0211994647979736

>> 비동기가 더 빠름. 순서 다름.

"""