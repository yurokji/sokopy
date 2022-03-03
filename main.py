from sokopy import *
import os
import time

soko = Sokopy()
soko.prepare(0)

soko.print()

while True:
    os.system('cls')
    soko.print()
    print("      레벨 ", soko.level + 1)
    print("      방향키값을 입력하세요(w,a,s,d), 리셋(0): ", end="")
    key = input().lower()

    isOk = (key == 'w' or key =='a' or key == 's' or key == 'd' or key == '0')
    while not isOk:
        print("      키가 잘못되었습니다.")
        print("      방향키값을 입력하세요(w,a,s,d), 리셋(0): ", end="")
        key = input().lower()
        isOk = (key == 'w' or key =='a' or key == 's' or key == 'd' or key == '0')

    print("키값은: ", key)

    if key == "0":
        print("      현재 레벨:", soko.level)
        soko.reset()

    else:
        # 움직임 또는 밀고 나아가기
        if not soko.move(key):
            if soko.push(key):
                soko.move(key)
    

    # 클리어 확인
    if soko.is_cleared():
        print("      레벨 ", soko.level + 1, "클리어!")
        soko.print()
        if len(soko.all_levels)  < soko.level + 2:
            print("      게임의 끝입니다")
            break
        soko.prepare(soko.level + 1)
        print("      레벨 ", soko.level + 1, "시작!")
        time.sleep(2)

        

