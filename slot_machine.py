# slot machine 문제
import random
import time
import os

while True :
    print("<Slot Machine Game>")
    try:
        num = int(input("1.게임시작 // 2.나가기 >>"))
    except:
        print("잘못 입력하셨습니다")
        continue
    if(num == 2) :
        print("게임을 종료합니다")
        time.sleep(1)
        break
    elif(num == 1) :
        while True :
            print("\n")
            try:
                coin = int(input("코인을 넣어주세요!(1. 코인넣기 // 2. 그만하기)"))
            except :
                print("잘못 입력하셨습니다")
                continue
            if (coin == 1) :
                slot1 = random.randint(33, 39)
                slot2 = random.randint(33, 39)
                slot3 = random.randint(33, 39)

                print("\n")
                print("        [SLOT]")
                print("┌──────┬──────┬──────┐")
                print("│ (%c)  │ (%c)  │ (%c)  │" %(slot1, slot2, slot3))
                print("└──────┴──────┴──────┘")

                if (slot1 == slot2 == slot3) :
                    print("축하합니다! ^o^ (%c)" %slot1)
                else :
                    print("다음 기회에..")
                    
            elif (coin == 2) :
                print("슬롯머신을 나갑니다")
                time.sleep(1)
                break
            else :
                print("잘못 입력하셨습니다1")
    else :
        print("잘못 입력하셨습니다")


#a = 35
# print("%c" %103)