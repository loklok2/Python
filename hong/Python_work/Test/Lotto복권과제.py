#100장을 먼저 만들고 리스트에 저장하고, 그 리스트에서 당첨번호가 있는지 찾아라
#1. 복권 100장 발행 하고 리스트에 저장하고 정렬 낮은 숫자부터~ + 보너스 번호 를 또 리스트에 저장하고 당첨번호 비교>for문돌리기
# 당첨확인 할때 함수로 구현해라
#기존 코드는 함수 돌리는 것을 이해하는게 목표임 이해하고 과제 실행

import random
##당첨번호 뽑기
def generate_winning_numbers():                             
    numbers = random.sample(range(1, 46), 6)    #1~46까지범위에서 6개 뽑기 random.sample 사용해서 중복 거르기
    numbers.sort()                                       ##낮은숫자부터 정렬
    bonus_number = random.randint(1, 45)                   ##1~45까지 보너스번호 생성
    return numbers, bonus_number                            ##당첨번호랑 보너스 번호 반환
##100장뽑기
def generate_lotto_tickets(num_tickets=100):       ##로또 100개 디폴드값으로 생성 
    lotto_tickets = []                               ##생성된거 담을 빈 리스트
    for _ in range(num_tickets):                       ## 반복문
        numbers = random.sample(range(1, 46), 6)        ## 1~46까지 범위에서 6개 뽑기
        numbers.sort()                                  ## 정렬
        bonus_number = random.randint(1, 45)            ## 1~45사이 보너스 생성
        lotto_tickets.append((numbers, bonus_number))      ## 로또랑 보너스번호 리스트에 추가
    return lotto_tickets                                    ## 생성된 로또 반환
##당첨확인
def check_lotto_result(winning_numbers, winning_bonus_number, lotto_tickets):        ##winning_numbers는 당첨번호 리스트 winning_bonus_number는 당첨보너스번호 lotto_tickets는 확인할 로또 리스트
    for idx, ticket in enumerate(lotto_tickets, 1):   ##idx는 인덱스값 1부터 시작
        lotto_numbers, lotto_bonus_number = ticket    ##enumrate()함수 튜플반환 알아두기
        
        if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
            print(f"{idx}번째 로또 복권: 1등 당첨!")
        elif lotto_numbers == winning_numbers:
            print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
        elif lotto_bonus_number == winning_bonus_number:
            print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
        elif len(set(lotto_numbers).intersection(winning_numbers)) == 5:
            print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
        elif len(set(lotto_numbers).intersection(winning_numbers)) == 4:
            print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
        else:
            print(f"{idx}번째 로또 복권: 꽝")

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_winning_numbers()
print("당첨 번호:", sorted(winning_numbers), "보너스 번호:", winning_bonus_number)

# 로또 티켓 생성
lotto_tickets = generate_lotto_tickets()

# 결과 확인
check_lotto_result(sorted(winning_numbers), winning_bonus_number, lotto_tickets)