"""
CPU Bound 1 - Synchronous
"""

# CPU-Bound 예제


import time

# 실행함수1 : 계산
def cpu_bound(number):
    return sum(i * i for i in range(number))

# 실행함수2
def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]    # 파이썬에서 3_000_000 == 3000000
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 실행
    total = find_sums(numbers)
    
    # 결과 출력
    print(f'\nTotal List : {total}')
    print(f'Sum : {sum(total)}')
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 수행 시간
    print(f'\nDuration : {duration} seconds')
    
if __name__ == "__main__":
    main()
    


"""
[실행 결과]

Total List : [8999995500000500000, 9000004500000500000, 9000013500006500001, 9000022500018500005, 9000031500036500014, 9000040500060500030, 9000049500090500055, 9000058500126500091, 9000067500168500140, 9000076500216500204, 9000085500270500285, 9000094500330500385, 9000103500396500506, 9000112500468500650, 9000121500546500819, 9000130500630501015, 9000139500720501240, 9000148500816501496, 9000157500918501785, 9000166501026502109, 9000175501140502470, 9000184501260502870, 9000193501386503311, 9000202501518503795, 9000211501656504324, 9000220501800504900, 9000229501950505525, 9000238502106506201, 9000247502268506930, 9000256502436507714]
Sum : 270003780024375058870

Duration : 40.54652643203735 seconds

>> 오래 걸림

"""